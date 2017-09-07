import time

class Logger:
    def __init__(self, filename):
        self.file = open(filename, "w")
    
    def log(self, text):
        self.file.write(str(time.time()) + ": " + text + "\n")
        self.file.flush()
    
    def close(self):
        self.file.close()