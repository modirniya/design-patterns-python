class Iterator:
    # An interface for iterator pattern.
    def has_next(self) -> bool:
        raise NotImplementedError()

    def current(self) -> any:
        raise NotImplementedError()

    def next(self):
        raise NotImplementedError()
