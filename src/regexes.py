YEAR_PATTERN = r"\d\d\d\d?|\d\d?\d?\d? (BCE?|AD)|\d\d\w\w century|year \d{1,4}"
MONTHS_PATTERN = r"(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)"
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

NOT_NULL_PATTERN = r"[1-9]"

DAY_FINDER_1 = r"(?P<days>[0-3]?[0-9]) " + MONTHS_PATTERN
DAY_FINDER_2 = MONTHS_PATTERN + r" (?P<days>[0-3]?[0-9])"

FULL_PATTERN = r"(" + DMY_1_PATTERN + r")|(" + DMY_2_PATTERN + r")|(" + DMY_3_PATTERN + r")|(" + DMY_4_PATTERN + r")|(" + MY_1_PATTERN + r")|(" + MY_2_PATTERN + r")|(" + MY_3_PATTERN + r")|(" + DM_PATTERN + r")|(" + YEAR_PATTERN + r")"