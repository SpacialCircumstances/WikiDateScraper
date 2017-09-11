class WikiDate:
    def __init__(self):
        self.days = 0
        self.month = 0
        self.year = 0

    def test_values(self):
        return self.days <= 31 and self.days >= 0 and self.month <= 12 and self.month >= 0 