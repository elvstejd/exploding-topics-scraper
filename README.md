
# Exploding Topics Scraper

Scrape trend data from [Exploding Topics](https://explodingtopics.com). Educational purposes only. 


## Running the scraper

Clone repo

```bash
  git clone https://github.com/elvstejd/exploding-topics-scraper.git
  cd exploding-topics-scraper
```

Create and activate virtual env

```bash
    py -m venv venv
    .\venv\Scripts\activate
```

Install dependencies and run
```bash
    pip install -r requirements.txt
    py main.py
```

When it finishes, the output will be saved in `output/trends_[date].json`.
The script will create the output folder if it doesn't exist.
## Suggested reading

Be sure to take a look at their [Terms of Service](https://explodingtopics.com/terms) if you plan on using this.

