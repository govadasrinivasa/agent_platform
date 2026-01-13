from tools.base import Tool

class CalculatorTool(Tool):
    name ="calculator"

    def execute(self, input: str) -> str:
        return str(eval(input))