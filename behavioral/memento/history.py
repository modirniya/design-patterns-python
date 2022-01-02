from behavioral.memento.editor_state import EditorState


class History:
    def __init__(self):
        self._states = list()

    def push(self, state: EditorState):
        self._states.append(state)

    def pop(self):
        return self._states.pop()
