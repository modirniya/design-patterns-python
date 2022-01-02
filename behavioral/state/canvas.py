from behavioral.state.tool import Tool


class Canvas:
    def __init__(self, tool: Tool | None = None):
        self._current_tool = tool

    def mouse_down(self):
        self.current_tool.mouse_down()

    def mouse_up(self):
        self.current_tool.mouse_up()

    def _set_tool(self, tool: Tool):
        self._current_tool = tool

    def _get_tool(self) -> Tool | None:
        return self._current_tool

    current_tool = property(_get_tool, _set_tool)
