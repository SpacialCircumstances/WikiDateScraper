import re
import regexes
from date_context import DateContext

#simple date finder

regex = re.compile(regexes.FULL_PATTERN, re.IGNORECASE)
not_null = re.compile(regexes.NOT_NULL_PATTERN, re.IGNORECASE)

def find_dates(text):
    dates = []
    for match in regex.finditer(text):
        datestring = match.group()
        if not_null.search(datestring) != None:
            sentence = match.string
            if len(sentence) > 2000:
                sentence = match.string[:2000]
            context = DateContext(text, datestring)
            dates.append(context)
    return dates


def test():
    pass

test()