from behavioral.state.tool import Tool


class SelectionTool(Tool):
    def mouse_down(self):
        print('Selection Icon')

    def mouse_up(self):
        print('Draw a dashed rectangle')