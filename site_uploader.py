import time
import shutil
import requests
import logging

def netlify_upload(build_dir, netlify_site, netlify_auth_token):
    logging.info("Uploading to Netlify...")
    logging.info("Zipping build...")
    shutil.make_archive("build", 'zip', build_dir)

    logging.info("Deploying...")
    with open("build.zip", 'rb') as f:
        r = requests.post(f"https://api.netlify.com/api/v1/sites/{netlify_site}/deploys", data=f.read(), headers={
            "Content-Type": "application/zip",
            "Authorization": f"Bearer {netlify_auth_token}",
        })
        data = r.json()

        deploy_id = data["id"]

        while True:
            r = requests.get(f"https://api.netlify.com/api/v1/deploys/{deploy_id}", headers={
                "Authorization": f"Bearer {netlify_auth_token}",
            })
            data = r.json()
            status = (data["summary"]["status"])
            logging.info(f"Deploy status is \"{status}\"...")
            if status == "ready":
                break
            else:
                time.sleep(0.1)

    logging.info("Finished uploading site.")
