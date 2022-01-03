from behavioral.strategy.compressor import Compressor
from behavioral.strategy.filter import Filter


class ImageStorage:
    def __init__(self, _compressor: Compressor, _filter: Filter):
        self.compressor = _compressor
        self.filter = _filter

    def store(self, filename: str):
        self.compressor.compress(filename)
        self.filter.apply(filename)
