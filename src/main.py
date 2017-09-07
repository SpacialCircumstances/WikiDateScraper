import sqlite3
import sys
from bs4 import BeautifulSoup

starting_article = "https://en.wikipedia.org/wiki/Constellation"
database_location = "data/wikiscraper.db"

if len(sys.argv) > 1:
    starting_article = sys.argv[1]

if len(sys.argv) > 2:
    database_location = sys.argv[2]