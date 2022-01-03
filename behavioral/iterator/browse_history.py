from behavioral.iterator.iterator import Iterator


class BrowseHistory:
    def __init__(self):
        self._urls = list()

    def _get_urls(self) -> list:
        return self._urls

    def push(self, url: str):
        self._urls.append(url)

    def pop(self) -> str | None:
        if len(self._urls) > 0:
            return self._urls.pop()
        return None

    def create_iterator(self) -> Iterator:
        return ListIterator(self)

    urls = property(_get_urls)


class ListIterator(Iterator):
    def __init__(self, history: BrowseHistory):
        self.history = history
        self.index = 0

    def has_next(self):
        return self.index < len(self.history.urls)

    def current(self):
        return self.history.urls[self.index]

    def next(self):
        self.index += 1
