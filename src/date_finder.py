import re

#simple date finder#
YEAR_PATTERN = r"\d\d\d\d ?(BCE?|AD)?|\d\d\w\w century"
MONTHS_PATTERN = r"(january|february|march|april|may|june|july|august|september|october|december|jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)"
DAY_PATTERN = r"[0-3]?[0-9][.]?"
MONTH_NUM_PATTERN = r"[0-1]?[0-9][.]?"
DMY_1_PATTERN = DAY_PATTERN + r" " + MONTHS_PATTERN + r" " + YEAR_PATTERN
DMY_2_PATTERN = MONTHS_PATTERN + r" " + DAY_PATTERN + r",?" + r" " + YEAR_PATTERN
DMY_3_PATTERN = DAY_PATTERN + r" ?" + MONTH_NUM_PATTERN + r" ?" + YEAR_PATTERN
DMY_4_PATTERN = r"[0-1]?[0-9]/ ?[0-3]?[0-9]/ ?" + YEAR_PATTERN

DM_PATTERN = DAY_PATTERN + r" +o?f? ?" + MONTHS_PATTERN

MY_1_PATTERN = MONTHS_PATTERN + r" " + YEAR_PATTERN
MY_2_PATTERN = MONTH_NUM_PATTERN + r" " + YEAR_PATTERN
MY_3_PATTERN = r"[0-1]?[0-9]/ ?" + YEAR_PATTERN

FULL_PATTERN = r"(" + DMY_1_PATTERN + r")|(" + DMY_2_PATTERN + r")|(" + DMY_3_PATTERN + r")|(" + DMY_4_PATTERN + r")|(" + MY_1_PATTERN + r")|(" + MY_2_PATTERN + r")|(" + MY_3_PATTERN + r")|(" + DM_PATTERN + r")|(" + YEAR_PATTERN + r")"
print(FULL_PATTERN[160:165])

regex = re.compile(FULL_PATTERN, re.IGNORECASE)

def find_dates(text):
    return regex.findall(text)


def test():
    pass

test()