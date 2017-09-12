import wikidate
import re
import regexes

year_finder = re.compile(r".*?(" + regexes.YEAR_PATTERN + ")")
num_finder = re.compile(r"\d+")
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

day_finder_1 = re.compile(regexes.DAY_FINDER_1, re.IGNORECASE)
day_finder_2 = re.compile(regexes.DAY_FINDER_2, re.IGNORECASE)

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
        #In reality, wikipedia always uses month names.
        date.month = 0

    #Find days
    d1 = day_finder_1.search(datestring)
    if d1:
        days = int(num_finder.search(d1.group()).group())
        date.days = days
        
    else:
        d2 = day_finder_2.search(datestring)
        if d2:
            days = int(num_finder.search(d2.group()).group())
            date.days = days

        else:
            date.days = 0

    return date