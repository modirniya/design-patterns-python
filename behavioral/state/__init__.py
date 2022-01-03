from behavioral.state.tools.brush_tool import BrushTool
from behavioral.state.canvas import Canvas
from behavioral.state.tools.selection_tool import SelectionTool


class StatePattern:
    def __init__(self):
        self.canvas = Canvas()
        self.play()

    def play(self):
        self.canvas.current_tool = SelectionTool()
        self.perform_canvas_actions()
        self.canvas.current_tool = BrushTool()
        self.perform_canvas_actions()

    def perform_canvas_actions(self):
        self.canvas.mouse_down()
        self.canvas.mouse_up()
