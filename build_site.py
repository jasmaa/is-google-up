import json
from datetime import datetime


def generate_html(report):
    html = "<html>"
    html += "<style>table, th, td { border: 1px solid black; }</style>"
    html += "<body>"
    html += "<table>"
    html += "<tr><th>Name</th><th>Status</th><th>Latency (ms)</th></tr>"
    for site in report["sites"]:
        html += f"<tr><td><a href=\"{site['url']}\">{site['name']}</a></td><td>{site['code']}</td><td>{site['latency']}</td></tr>"
    html += "</table>"
    html += f"<p><em>Last generated at: {datetime.fromtimestamp(report['created_at'] / 1000)}</em></p>"
    html += "</body>"
    html += "</html>"
    return html


def main():
    with open("build/report.json")as f:
        report = json.load(f)
    html = generate_html(report)
    with open("build/index.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
