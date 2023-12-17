import os
from pathlib import Path
import shutil
import json
from datetime import datetime
import dotenv
from jinja2 import Environment, PackageLoader, select_autoescape

dotenv.load_dotenv()

BUILD_DIR = os.environ.get("BUILD_DIR", "build")


def code2category(code):
    return f"{int(code / 100)}xx"


def main():
    with open(Path(BUILD_DIR, "report.json"))as f:
        report = json.load(f)

    env = Environment(
        loader=PackageLoader("build_site"),
        autoescape=select_autoescape()
    )

    template = env.get_template("index.html")
    html = template.render(
        verdict="Yes" if all(
            [site.get("code") == 200 for site in report["sites"]]) else "No",
        sites=report["sites"],
        last_modified=datetime.fromtimestamp(report['created_at'] / 1000),
        code2category=code2category,
    )
    with open(Path(BUILD_DIR, "index.html"), "w") as f:
        f.write(html)

    shutil.copy2('style.css', BUILD_DIR)

    with open(Path(BUILD_DIR, ".nojekyll"), "w") as f:
        pass


if __name__ == "__main__":
    main()
