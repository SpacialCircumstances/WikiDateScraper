import sqlite3
import sys
import requests
import logger
from bs4 import BeautifulSoup

starting_article = "https://en.wikipedia.org/wiki/Constellation"
database_location = "data/wikiscraper.db"
logging_location = "logs/logfile.txt"

MAX_ARTICLES = 50
if len(sys.argv) > 1:
    starting_article = sys.argv[1]

if len(sys.argv) > 2:
    database_location = sys.argv[2]

log = logger.Logger(logging_location)

def main():
    #Prepare logfile
    log.log("Logging started")
    log.log("Database saving in " + database_location)
    log.log("Articles max: " + str(MAX_ARTICLES))

    queued_articles = [starting_article]
    article_count = 0
    running = True
    log.log("Starting with " + starting_article)
    log.log("##############################")

    while running:
        if article_count < MAX_ARTICLES and len(queued_articles) > 0:
            article_count += 1
            article = queued_articles.pop()
            queued_articles = parse_article(queued_articles, article)

        else:
            running = False

    log.close()

def parse_article(queue, article):
    clear_name = link_to_identifier(article)
    log.log("Requesting " + article)
    return queue

def link_to_identifier(link):
    return link

main()