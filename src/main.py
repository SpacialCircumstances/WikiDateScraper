import sqlite3
import sys
import time
import requests
import logger
import date_finder
import date_parser
from bs4 import BeautifulSoup

starting_article = "https://en.wikipedia.org/wiki/Augustus"
database_location = "data/wikiscraper.db"
logging_location = "logs/logfile.txt"

MAX_ARTICLES = 50
if len(sys.argv) > 1:
    starting_article = sys.argv[1]

if len(sys.argv) > 2:
    database_location = sys.argv[2]

language_identifier = starting_article[starting_article.find("//") + 2:starting_article.find(".")]

log = logger.Logger(logging_location)
db = sqlite3.connect(database_location)

con = db.cursor()

article_table_name = language_identifier + "_articles"
date_table_name = language_identifier + "_dates"

def main():
    #Prepare logfile
    log.log("Logging started")
    log.log("Database saving in " + database_location)
    
    #Create tables in db
    con.execute("CREATE TABLE IF NOT EXISTS " + article_table_name + " (id INTEGER PRIMARY KEY NOT NULL, wiki_id VARCHAR(512), date VARCHAR(16), clearname VARCHAR(512))")
    con.execute("CREATE TABLE IF NOT EXISTS " + date_table_name + " (id INTEGER PRIMARY KEY NOT NULL, wiki_id VARCHAR(512), date VARCHAR(16), sentence VARCHAR(2048))")
    db.commit()
    log.log("Database successfully prepared")

    log.log("Articles max: " + str(MAX_ARTICLES))
    log.log("Language: " + language_identifier)

    queued_articles = [starting_article]
    article_count = 0
    running = True
    log.log("Starting with " + starting_article)
    log.log("##############################")

    while running:
        if article_count < MAX_ARTICLES and queued_articles:
            article_count += 1
            article = queued_articles.pop(0)
            queued_articles = parse_article(queued_articles, article)

        else:
            running = False

    log.close()

def parse_article(queue, article):
    wiki_id = link_to_identifier(article)
    log.log("Requesting " + wiki_id)
    wikipage = requests.get(article)
    log.log("Response: " + str(wikipage.status_code))
    soup = BeautifulSoup(wikipage.content, "html.parser")

    #Get the heading
    heading_html = soup.find_all(id = "firstHeading")[0]
    heading = heading_html.get_text()
    timestamp = str(int(time.time()))
    save_article_info(wiki_id, heading, timestamp)
    log.log("Article info saved")

    #Find links
    article_content = soup.find_all(class_ = "mw-parser-output")[0]
    possible_links = strip_wiki_links(article_content)
    new_links = ["http://" + language_identifier + ".wikipedia.org" + i for i in possible_links if (not i in queue) and (not article_is_parsed(i))]
    log.log("Links found: " + str(len(possible_links)) + " New are: " + str(len(new_links)))

    queue.extend(new_links)

    #Find dates
    dates = []
    subp = article_content.find_all("p")
    for paragraph in subp:
        for quote in paragraph.find_all("a"):
            quote.extract()
        dates.extend(date_finder.find_dates(paragraph.get_text()))
    
    log.log("Dates found: " + str(len(dates)))

    for date in dates:
        save_date(date_parser.parse_date(date.date), date, wiki_id)

    db.commit()
    log.log("###### Finished")
    return queue

def remove_protocol(link):
    end = link.find("//") + 2
    return link[:end]

def link_to_identifier(link):
    url_part = language_identifier + ".wikipedia.org/wiki/"
    start = link.find(url_part) + len(url_part)
    return link[start:]

def save_date(date, context, wiki_id):
    params = (wiki_id, date.get_date_string(), context.sentence)
    con.execute("INSERT INTO " + date_table_name + " (wiki_id, date, sentence) VALUES (?, ?, ?)", params)
    #print(date.get_date_string())

def article_is_parsed(wiki_id):
    par = (wiki_id,)
    con.execute("SELECT clearname FROM " + article_table_name + " WHERE wiki_id = ?", par)
    return con.fetchone() != None

def save_article_info(wiki_id, clearname, timestamp):
    params = (wiki_id, timestamp, clearname)
    con.execute("INSERT INTO " + article_table_name + "(wiki_id, date, clearname) VALUES(?, ?, ?)", params)
    db.commit()

def strip_wiki_links(main_content):
    links = []
    subp = main_content.find_all("p")
    for paragraph in subp:
        potential_links = paragraph.find_all("a")
        for link in potential_links:
            if link.has_attr("href"):
                if is_internal_link(link["href"]):
                    links.append(link["href"])

    return links

def is_internal_link(link):
    return (link[:6] == "/wiki/") and (link[6:11] != "File:")

main()
