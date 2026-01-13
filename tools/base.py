class Tool:
    name: str

    def execute(self, input: str) -> str:
        raise NotImplementedError