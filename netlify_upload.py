import os
import time
import shutil
import requests
import dotenv

dotenv.load_dotenv()

BUILD_DIR = os.environ.get("BUILD_DIR", "build")
NETLIFY_AUTH_TOKEN = os.environ.get("NETLIFY_AUTH_TOKEN")
NETLIFY_SITE = os.environ.get("NETLIFY_SITE")


def main():
    print("Zipping build...")
    shutil.make_archive("build", 'zip', BUILD_DIR)

    print("Uploading...")
    with open("build.zip", 'rb') as f:
        r = requests.post(f"https://api.netlify.com/api/v1/sites/{NETLIFY_SITE}/deploys", data=f.read(), headers={
            "Content-Type": "application/zip",
            "Authorization": f"Bearer {NETLIFY_AUTH_TOKEN}",
        })
        data = r.json()

        deploy_id = data["id"]

        while True:
            r = requests.get(f"https://api.netlify.com/api/v1/deploys/{deploy_id}", headers={
                "Authorization": f"Bearer {NETLIFY_AUTH_TOKEN}",
            })
            data = r.json()
            status = (data["summary"]["status"])
            print(f"Status is {status}...")
            if status == "ready":
                break
            else:
                time.sleep(0.1)


if __name__ == "__main__":
    main()
