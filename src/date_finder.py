import re

#simple date finder#
YEAR_PATTERN = r"\d?\d?\d\d ?(BCE?|AD)?"
MONTHS_PATTERN = r"(january|february|march|april|may|june|july|august|september|october|december|jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)"
DAY_PATTERN = r"[0-3]?[0-9][.]?"
MONTH_NUM_PATTERN = r"[0-1]?[0-9][.]?"
MY_1_PATTERN = DAY_PATTERN + r" " + MONTHS_PATTERN + r" " + YEAR_PATTERN
MY_2_PATTERN = MONTHS_PATTERN + r" " + DAY_PATTERN + r",?" + r" " + YEAR_PATTERN
MY_3_PATTERN = DAY_PATTERN + r" ?" + MONTH_NUM_PATTERN + r" ?" + YEAR_PATTERN
MY_4_PATTERN = r"[0-1]?[0-9]/ ?[0-3]?[0-9]/ ?" + YEAR_PATTERN
p1 = re.compile(MY_1_PATTERN, re.IGNORECASE)
p2 = re.compile(MY_2_PATTERN, re.IGNORECASE)
p3 = re.compile(MY_3_PATTERN, re.IGNORECASE)
p4 = re.compile(MY_4_PATTERN, re.IGNORECASE)

def find_dates(text):
    return []

def test():
    print(p1.match("18 March 2017 BC"))
    print(p1.match("3 May 1991"))
    print(p1.match("16 Jul 66"))
    print(p1.match("28. March 2001"))
    print(p2.match("March 28, 2001"))
    print(p2.match("Jan 12 1999AD"))
    print(p3.match("28. 03. 1001"))
    print(p3.match("2 06 2009"))
    print(p4.match("1/2/1999"))
    print(p4.match("12/ 05/ 1651"))

test()