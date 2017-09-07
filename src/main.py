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

language_identifier = starting_article[starting_article.find("//") + 2:starting_article.find(".")]

log = logger.Logger(logging_location)

def main():
    #Prepare logfile
    log.log("Logging started")
    log.log("Database saving in " + database_location)
    log.log("Articles max: " + str(MAX_ARTICLES))
    log.log("Language: " + language_identifier)

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
    log.log("Requesting " + clear_name)
    return queue

def remove_protocol(link):
    end = link.find("//") + 2
    return link[:end]

def link_to_identifier(link):
    url_part = language_identifier + ".wikipedia.org/wiki/"
    start = link.find(url_part) + len(url_part)
    return link[start:]

main()