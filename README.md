# Is Google Up

Have you ever wondered if Google is still up? I sure have. Sometimes I just lie
there in my bed, staring at the ceiling and thinking to myself, "Is Google still
up? Why? Has Google ever returned a 5xx status code or timed out? What happens
if Google experiences a prolonged outage? Will modern society is we know it
crumble; ashes to ashes, dust to dust? And why is it always DNS?"

## Getting Started

### Create Netlify site

Create Netlify site and copy your site's URL. This will be `NETLIFY_SITE`.

Generate a Netlify [personal access
token](https://app.netlify.com/user/applications#personal-access-tokens). This
value will be `NETLIFY_AUTH_TOKEN`.

### Install dependencies

```
pip3 install -r "requirements.txt"
```

```
Create `.env` from `sample.env` and fill with correct values.
```

Test script with:

```
cd /<PATH>/<TO>/<REPO> && python3 main.py
```

### Set up cronjob

Open crontab:

```
crontab -e
```

Add cronjob on a new line:

```
0 0 * * * cd /<PATH>/<TO>/<REPO> && python3 main.py >> /var/log/is-google-up.log 2>&1
```