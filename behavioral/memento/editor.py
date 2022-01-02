from behavioral.memento.editor_state import EditorState


class Editor:
    def __init__(self, content: str | None = None):
        self._content = content

    def create_state(self) -> EditorState:
        return EditorState(content=self.content)

    def restore(self, state: EditorState):
        self._content = state.content

    def _set_content(self, content: str):
        self._content = content

    def _get_content(self) -> str:
        return self._content

    content = property(_get_content, _set_content)

    def __str__(self):
        return 'Content: %s' % self._content
