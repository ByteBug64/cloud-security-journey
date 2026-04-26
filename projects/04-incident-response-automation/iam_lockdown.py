import boto3
import json
from datetime import datetime

iamClient = boto3.client('iam')
user_name = 'victim-user'
def lockdown_user(user_name):
    response = iamClient.list_access_keys(UserName=user_name)
    for access_key in response['AccessKeyMetadata']:
        access_key_id = access_key['AccessKeyId']
        iamClient.update_access_key(UserName=user_name, AccessKeyId=access_key_id, Status='Inactive')


def isolate_user(instance_id):
    ec2Client = boto3.client('ec2')
    response = ec2Client.describe_instances(InstanceIds=[instance_id])
    security_group_id = response['Reservations'][0]['Instances'][0]['SecurityGroups']
    vpc_id = response['Reservations'][0]['Instances'][0]['VpcId']
    print("Current security groups:", security_group_id)
    print("VPC ID:", vpc_id)
    try:
        sg_id = ec2Client.create_security_group(
            GroupName='quarantine-sg',
            Description='isolation group - no inbound or outbound traffic allowed',
            VpcId = vpc_id
        )
        quarantine_sg_id = sg_id['GroupId']
    except:
        existing_sg = ec2Client.describe_security_groups(
            Filters=[{'Name': 'group-name', 'Values': ['quarantine-sg']}]
        )
        quarantine_sg_id = existing_sg['SecurityGroups'][0]['GroupId']
    print("Quarantine sg id:", quarantine_sg_id)
    ec2Client.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=[quarantine_sg_id]
    )
    ec2Client.create_tags(
        Resources = [instance_id],
        Tags = [
            {
                'Key': 'Status',
                'Value': 'QUARANTINED'
            }
        ]
    )
    return quarantine_sg_id

def log_incident(username, instance_id, quarantine_sg_id):
    incident = {
        "user_name":username,
        "instance_id":instance_id,
        "quatantine_sg_id":quarantine_sg_id,
        "timestamp": datetime.now().isoformat()
    }
    with open('incident_log.json', 'w') as f:
        json.dump(incident, f)
def send_alert(message):
    snsclient = boto3.client('sns')
    snsclient.publish(
        TopicArn='arn:aws:sns:us-east-1:886375649091:security-alerts',
        Message = message,
        Subject = 'Security Alert: Potential Compromise Detected'
    )
def  respond_to_incident(username, instance_id):
    lockdown_user(username)
    quarantine_sg_id = isolate_user(instance_id)
    log_incident(username, instance_id, quarantine_sg_id)
    send_alert(f'User {username} has been locked down and instance {instance_id} has been isolated. Quarantine SG ID: {quarantine_sg_id}')
    return    

respond_to_incident(user_name, 'i-04737d2f22cf6c7b9')