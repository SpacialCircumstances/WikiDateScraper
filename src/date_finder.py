import re

#simple date finder#
YEAR_PATTERN = r"\d?\d?\d\d ?(BCE?|AD)?"
MONTHS_PATTERN = r"(january|february|march|april|may|june|july|august|september|october|december|jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)"
DAY_PATTERN = r"[0-3]?[0-9][.]?"
MONTH_NUM_PATTERN = r"[0-1]?[0-9][.]?"
DMY_1_PATTERN = DAY_PATTERN + r" " + MONTHS_PATTERN + r" " + YEAR_PATTERN
DMY_2_PATTERN = MONTHS_PATTERN + r" " + DAY_PATTERN + r",?" + r" " + YEAR_PATTERN
DMY_3_PATTERN = DAY_PATTERN + r" ?" + MONTH_NUM_PATTERN + r" ?" + YEAR_PATTERN
DMY_4_PATTERN = r"[0-1]?[0-9]/ ?[0-3]?[0-9]/ ?" + YEAR_PATTERN

MY_1_PATTERN = MONTHS_PATTERN + r" " + YEAR_PATTERN
MY_2_PATTERN = MONTH_NUM_PATTERN + r" " + YEAR_PATTERN
MY_3_PATTERN = r"[0-1]?[0-9]/ ?" + YEAR_PATTERN

def find_dates(text):
    return []

def test():
    pass

test()