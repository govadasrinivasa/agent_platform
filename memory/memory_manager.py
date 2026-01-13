class MemoryManager:
    def __init__(self):
        self.short_term = []

    def store(self, entry: str):
        self.short_term.append(entry)

    def recall(self):
        return self.short_term[-5:]