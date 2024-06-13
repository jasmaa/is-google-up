from pathlib import Path
import shutil
import json
from datetime import datetime
import logging
from jinja2 import Environment, PackageLoader, select_autoescape

def code2category(code):
    return f"{int(code / 100)}xx"


def build_site(report_dir, build_dir):
    logging.info("Building site...")
    logging.info("Loading report...")
    with open(Path(report_dir, "report.json"))as f:
        report = json.load(f)

    env = Environment(
        loader=PackageLoader("site_builder"),
        autoescape=select_autoescape()
    )

    logging.info("Writing site artifacts...")
    template = env.get_template("index.html")
    html = template.render(
        verdict="Yes" if all(
            [site.get("code") == 200 for site in report["sites"]]) else "No",
        sites=report["sites"],
        last_modified=datetime.fromtimestamp(report['created_at'] / 1000),
        code2category=code2category,
    )
    with open(Path(build_dir, "index.html"), "w") as f:
        f.write(html)

    shutil.copy2('style.css', build_dir)

    with open(Path(build_dir, ".nojekyll"), "w") as f:
        pass

    logging.info("Finished building site.")