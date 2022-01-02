class User:
    def __init__(self, name=None):
        print('User initiated')
        self.name: str | None = name
