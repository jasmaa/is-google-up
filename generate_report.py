import os
import datetime
import json
import requests

SITES = [
    {
        "name": "Google",
        "url": "https://google.com",
    },
]


def ping(site):
    start = datetime.datetime.now()
    r = requests.get(site["url"])
    end = datetime.datetime.now()
    return {
        "code": r.status_code,
        "latency": end-start,
    }


def main():
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
    if not os.path.exists("build"):
        os.makedirs("build")
    with open("build/report.json", "w") as f:
        json.dump(report, f)


if __name__ == "__main__":
    main()
