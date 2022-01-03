from behavioral.strategy.compressor import JPEGCompressor
from behavioral.strategy.filter import BlackAndWhite
from behavioral.strategy.image_storage import ImageStorage


class StrategyPattern:
    def __init__(self):
        self.image_storage = ImageStorage(
            _compressor=JPEGCompressor(),
            _filter=BlackAndWhite())
        self.play()

    def play(self):
        pass
