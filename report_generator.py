import os
from pathlib import Path
import datetime
import json
import logging
import requests

SITES = [
    {
        "name": "Google",
        "url": "https://google.com",
    },
]


def ping(site):
    logging.info(f"Pinging \"{site['url']}\"...")
    start = datetime.datetime.now()
    r = requests.get(site["url"])
    end = datetime.datetime.now()
    logging.info(f"Finished pinging \"{site['url']}\".")
    return {
        "code": r.status_code,
        "latency": end-start,
    }


def generate_report(build_dir):
    logging.info("Generating report...")
    ping_results = [ping(s) for s in SITES]
    sites = [{
        "name": s["name"],
        "url": s["url"],
        "code": r["code"],
        "latency": round(r["latency"].total_seconds() * 1000, 3)
    } for s, r in zip(SITES, ping_results)]
    now = datetime.datetime.now().timestamp() * 1000
    report = {
        "created_at": now,
        "sites": sites,
    }

    if not os.path.exists(build_dir):
        logging.info("No build directory exists. Creating directory...")
        os.makedirs("build")

    logging.info("Writing report...")
    with open(Path(build_dir, "report.json"), "w") as f:
        json.dump(report, f)

    logging.info("Finished generating report.")
