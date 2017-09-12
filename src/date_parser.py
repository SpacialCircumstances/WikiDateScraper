import wikidate
import re
import regexes

year_finder = re.compile(".*?(" + regexes.YEAR_PATTERN + ")")
num_finder = re.compile("\d+")

def parse_date(datestring):
    date = wikidate.WikiDate()
    moy = year_finder.search(datestring)
    if moy:
        yearstring = moy.group(1)
        is_bc = ("BC" in yearstring) or ("BCE" in yearstring)
        yearn = num_finder.search(yearstring).group()
        print(yearn)
        if is_bc:
            date.year = -int(yearn)
        else:
            date.year = int(yearn)
        
    else:
        date.year = 0
    return date