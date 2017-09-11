class WikiDate:
    def __init__(self):
        self.days = 0
        self.month = 0
        self.year = 0

    def test_values(self):
        return self.days <= 31 and self.days >= 0 and self.month <= 12 and self.month >= 0 

    def get_date_string(self):
        days = ""
        if self.days < 10:
            days = "0" + str(self.days)
        else:
            days = str(self.days)

        months = ""
        if self.month < 10:
            months = "0" + str(self.month)
        else:
            months = str(self.month)
        
        year = "+"
        if self.year < 0:
            year = "-"

        if self.year < 1000:
            year += "0"

        if self.year < 100:
            year += "0"

        if self.year < 10:
            year += "0"

        year += self.year 
        return days + ":" + months + ":" + year