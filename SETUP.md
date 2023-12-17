# Setup

## Ubuntu

### Create Netlify site

Go to Netlify and create a site.

### Install depedendencies

```
pip3 install -r "requirements.txt"
```

```
npm install netlify-cli -g
```

### Bootstrap script

Bootstrap script with:

```
cd /<PATH>/<TO>/<REPO> && ./run.sh
```

You will have to login to Netlify and select the site on first run.

### Set up cronjob

Open crontab:

```
crontab -e
```

Add cronjob on a new line:

```
0 0 * * * cd /<PATH>/<TO>/<REPO> && ./run.sh
```

