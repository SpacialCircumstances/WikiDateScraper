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
It will start with the article about [Augustus](https://en.wikipedia.org/wiki/Augustus) and read the first 50 articles.

    python src/main.py [Starting Article link] [Database name and location]
You can modify this behaviour by:

#### Articles count
Modify the `MAX_ARTICLES` constant in `src/main.py`.
In the future, this will be possible using the command line.

#### Starting article
Supply the full wikipedia link of the article (English only supported at the moment) as the first argument when running the script.

#### Database name
The second argument when running the script.