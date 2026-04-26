from rich.console import Console
from rich.table import Table
from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime

console = Console()
def print_terminal_report(results):
    table = Table(title="S3 Bucket Security Report")
    table.add_column("Bucket Name")
    table.add_column("Check")
    table.add_column("Status")
    table.add_column("Issues")
    for result in results:
        for finding in result['findings']:
            table.add_row(result['bucket'], finding['check'], finding['status'],",".join(finding['issues']))
    console.print(table)
def generate_htmlreport(results):
    env = Environment(loader = FileSystemLoader(os.path.dirname(__file__)))
    template = env.get_template('template.html')
    html_output = template.render(results=results)
    timestamp = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    output_path = os.path.join('output', timestamp )
    with open(output_path, 'w') as f:
        f.write(html_output)
    print(f"Report saved to {output_path}")