from behavioral.memento.editor import Editor
from behavioral.memento.history import History


class MementoPattern:
    def __init__(self):
        self.editor = Editor()
        self.history = History()
        self.play()

    def play(self):
        self.editor.content = "a"
        self.save_changes()
        self.editor.content = "b"
        self.save_changes()
        self.editor.content = "c"
        self.save_changes()
        self.undo()
        print(self.editor)
        self.undo()
        print(self.editor)
        self.undo()
        print(self.editor)

    def undo(self):
        self.editor.restore(self.history.pop())

    def save_changes(self):
        self.history.push(
            self.editor.create_state())
