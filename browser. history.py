class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]  # store all visited URLs
        self.curr = 0              # pointer to current page

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        # discard all forward history when visiting new page
        self.history = self.history[:self.curr + 1]
        self.history.append(url)
        self.curr += 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]
