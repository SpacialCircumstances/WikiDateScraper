import wikidate
import re
import regexes

year_finder = re.compile(".*?(" + regexes.YEAR_PATTERN + ")")
num_finder = re.compile("\d+")
month_name_finder = re.compile(regexes.MONTHS_PATTERN, re.IGNORECASE)
month_map = {"jan" : 1,
            "feb" : 2,
            "mar" : 3,
            "apr" : 4,
            "may" : 5,
            "jun" : 6,
            "jul" : 7,
            "aug" : 8,
            "sep" : 9,
            "oct" : 10,
            "nov" : 11,
            "dec" : 12
            }

def parse_date(datestring):
    date = wikidate.WikiDate()
    moy = year_finder.search(datestring)
    if moy:
        yearstring = moy.group(1)
        is_bc = ("BC" in yearstring) or ("BCE" in yearstring)
        yearn = num_finder.search(yearstring).group()
        if is_bc:
            date.year = -int(yearn)
        else:
            date.year = int(yearn)
        
    else:
        date.year = 0

    #Find months
    #Easy try: month names
    mnm = month_name_finder.search(datestring)
    if mnm:
        mn = mnm.group()[:3].lower()
        date.month = month_map[mn]

    else:
        #Try to find numbers
        pass

    return date