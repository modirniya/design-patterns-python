class Filter:
    def apply(self, filename: str):
        raise NotImplementedError()


class BlackAndWhite(Filter):
    def apply(self, filename: str):
        print('B&W filter applied')


class Bright(Filter):
    def apply(self, filename: str):
        print('Bright filter applied')
