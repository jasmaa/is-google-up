# Setup

## Ubuntu

### Create Netlify site

Create Netlify site and copy your site's URL. This will be `NETLIFY_SITE`.

Generate a Netlify [personal access
token](https://app.netlify.com/user/applications#personal-access-tokens). This
value will be `NETLIFY_AUTH_TOKEN`.

### Install depedendencies

```
pip3 install -r "requirements.txt"
```

### Bootstrap script

```
Create `.env` from `sample.env` and fill with correct values.
```

Test script with:

```
cd /<PATH>/<TO>/<REPO> && ./run.sh
```

### Set up cronjob

Open crontab:

```
crontab -e
```

Add cronjob on a new line:

```
0 0 * * * cd /<PATH>/<TO>/<REPO> && ./run.sh
```

