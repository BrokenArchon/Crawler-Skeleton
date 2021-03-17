# Crawler-Skeleton
This code provide simple logic for crawling and parsing web pages.

Install Virtual Environment

```
sudo pip3 install virtualenv
cd {{ project dir }}
virtualenv venv
```

Install requirements

```
source venv/bin/activate
pip install -r requirements.txt
```

Start scrapers

```
source venv/bin/activate
python app.py
python app.py --search "search string"
```

Note: Don't forget download webdriver like chromedriver for selenium package.