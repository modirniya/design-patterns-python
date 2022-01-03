class Compressor:
    # Interface
    def compress(self, filename: str):
        raise NotImplementedError


class JPEGCompressor(Compressor):
    def compress(self, filename: str):
        print('Compressing JPEG')


class PNGCompressor(Compressor):
    def compress(self, filename: str):
        print('Compressing PNG')
