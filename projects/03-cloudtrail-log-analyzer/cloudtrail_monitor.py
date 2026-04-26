import boto3
import json
from datetime import datetime, timedelta
client= boto3.client('cloudtrail', region_name='us-east-1')
def getevent(client):
    end_time = datetime.utcnow()
    start_time= datetime.utcnow() - timedelta(hours=24)
    response = client.lookup_events(
        StartTime = start_time,
        EndTime = end_time
    )
    all_events = []
    all_events.extend(response["Events"])
    while "NextToken" in response:
        response = client.lookup_events(
            StartTime = start_time,
            EndTime = end_time,
            NextToken = response["NextToken"]
        )
        all_events.extend(response["Events"])
    return all_events
def parse_events(event):
    raw = event["CloudTrailEvent"]
    parsed = json.loads(raw)
    return parsed
def is_failed_login(event):
    if event.get("eventName") == "ConsoleLogin" and event.get("errorMessage") == "Failed authentication":
        return True
    else:
        return False
def is_root_usage(event):
    userIdentity = event.get("userIdentity", {})
    user_type = userIdentity.get("type")
    if user_type == "Root":
        return True
    else:
        return False    
def is_unusual_region(event):
    expected_regions =["us-east-1", "us-west-2", "eu-west-1"]
    region = event.get("awsRegion")
    if region not in expected_regions:
        return True
    else:
        return False   
def save_to_json(flagged_events):
    with open("flagged_events.json", "w") as file:
        json.dump(flagged_events, file, indent=4, default=str)   
all_events = getevent(client)  
flagged_events = []
for event in all_events:
    parsed_event = parse_events(event)

    if is_failed_login(parsed_event):
       parsed_event["flag_reason"] = "Failed Login Attempt"
       flagged_events.append(parsed_event)
    if is_root_usage(parsed_event):
        parsed_event["flag_reason"] = "Root account usage"
        flagged_events.append(parsed_event)
    if is_unusual_region(parsed_event):
        parsed_event["flag_reason"] = "Unusual region"      
        flagged_events.append(parsed_event)
print(len(flagged_events), "suspicious events found")
save_to_json(flagged_events)