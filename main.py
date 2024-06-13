import os
import logging
import dotenv
from site_builder import build_site
from report_generator import generate_report
from site_uploader import netlify_upload

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    dotenv.load_dotenv()

    BUILD_DIR = os.environ.get("BUILD_DIR", "build")
    NETLIFY_AUTH_TOKEN = os.environ.get("NETLIFY_AUTH_TOKEN")
    NETLIFY_SITE = os.environ.get("NETLIFY_SITE")

    generate_report(build_dir=BUILD_DIR)
    build_site(report_dir=BUILD_DIR, build_dir=BUILD_DIR)
    netlify_upload(
        build_dir=BUILD_DIR,
        netlify_site=NETLIFY_SITE,
        netlify_auth_token=NETLIFY_AUTH_TOKEN,
    )
