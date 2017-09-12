import wikidate
import re
import regexes

year_finder = re.compile(".*?(" + regexes.YEAR_PATTERN + ")")

def parse_date(datestring):
    date = wikidate.WikiDate()
    moy = year_finder.search(datestring)
    if moy:
        print(moy.group(1))
    return date