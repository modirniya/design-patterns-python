class EditorState:
    def __init__(self, content: str):
        self._content = content

    def _get_content(self) -> str:
        return self._content

    content = property(_get_content)

    def __str__(self):
        return 'Content: %s' % self.content
