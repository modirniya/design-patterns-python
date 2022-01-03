from behavioral.iterator.browse_history import BrowseHistory
from behavioral.iterator.iterator import Iterator


class IteratorPattern:
    def __init__(self):
        self.history = BrowseHistory()
        self.play()

    def play(self):
        self.history.push('url-1')
        self.history.push('url-2')
        self.history.push('url-3')
        self.iterate()

    def iterate(self):
        it: Iterator = self.history.create_iterator()
        while it.has_next():
            url = it.current()
            print(url)
            it.next()
