# WikiDateScraper
WikiDateScraper is a python script that maps wikipedia articles to dates mentioned in them. This way, it is possible to find the context of a special date or the dates related to an event by searching the Sqlite database created by WikiDateScraper.

WikiDateScraper is licensed under the MIT License. More information can be found in the LICENSE.md file.

## Installation
WikiDateScraper is written in Python 3, so you will need that first. It was developed with Python 3.6.2, but it should be usable in most of the lower versions as long as they are compatible with the dependencies.
WikiDateScraper needs [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) as well as the [requests](http://docs.python-requests.org/en/master/) library.
You can install all the dependencies with:

    pip install beautifulsoup4
    pip install requests

Now clone this repository with:

    git clone https://github.com/SpacialCircumstances/WikiDateScraper.git

And run with:
    cd WikiDateScraper
    python src/main.py

You can find more details in the **Usage** section.

## Usage
Run `src/main.py` to run the script in default mode.
This will create the database in the `data/` directory and the logfiles in `logs/`.
It will start with the article about [Augustus](https://en.wikipedia.org/wiki/Augustus) and read the first 250 articles.

    python src/main.py [Starting Article link] [Database name and location]
You can modify this behaviour by:

#### Articles count
At the moment, this limit is 250.
Modify the `MAX_ARTICLES` constant in `src/main.py`.
In the future, this will be possible using the command line.

#### Starting article
Supply the full wikipedia link of the article (English only supported at the moment) as the first argument when running the script.

#### Database name
The second argument when running the script.

## Database usage
WikiDateScraper will create two tables in the sqlite database.
The first one is named en_articles and saves data about the heading of the article and the date when it was saved.
The second one (en_dates) saves the dates that are scraped from the articles.
The `wiki_id` column saves the identifier of the article (the last part of the URL). The `sentence` column saves the context the date is in (max. 2048 characters). This is the paragraph the date was found in.
The `date` column saves the detected date in a special format (see: **Date format**).

The dates saved in the article can be read programmatically using one of the sqlite libraries that are available for almost every programming language out there. 
You can also run arbitrary SQL queries on the database or use one of the available database browsers.

#### Table formats
    _articles: (id INTEGER PRIMARY KEY NOT NULL, wiki_id VARCHAR(512), date VARCHAR(16), clearname VARCHAR(512))
    _dates: (id INTEGER PRIMARY KEY NOT NULL, wiki_id VARCHAR(512), date VARCHAR(16), sentence VARCHAR(2048))

#### Date formats
WikiDateScraper tries its best to identify all dates in the Wikipedia articles and parse them correctly. If one of the components of the date is 0, that means this component was either not given in the article or could not be identified.

    DD:MM:+YYYY

So `January 1, 1970` becomes `01:01:+1970`.

If the date is before AD, the `+` before `YYYY` becomes a minus.
The date is a string, so it will have a length of 11. WikiDateScraper will fail for dates outside the range of 9999BCE and 9999AD.

This special format makes searching for dates using SQL `LIKE` queries very easy.