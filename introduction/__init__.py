from introduction.user import User


class Intro:
    def __init__(self):
        print('Intro Initiated')
        self.user = User(name='Parham')
        self._run_intro()

    def _run_intro(self):
        self.print_user_name_with_title()
        self.user = User()
        self.user.name = 'Neda'
        self.print_user_name_with_title()

    def print_user_name_with_title(self):
        print(self)

    def __str__(self) -> str:
        return 'name: {}'.format(self.user.name)
