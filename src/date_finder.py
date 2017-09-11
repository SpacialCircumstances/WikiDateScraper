import re
import regexes
from date_context import DateContext

#simple date finder

regex = re.compile(regexes.FULL_PATTERN, re.IGNORECASE)

def find_dates(text):
    dates = []
    for match in regex.finditer(text):
        datestring = match.group()
        sentence = match.string
        if len(sentence) > 2000:
            sentence = match.string[:2000]
        context = DateContext(text, datestring)
        dates.append(context)
    return dates


def test():
    pass

test()