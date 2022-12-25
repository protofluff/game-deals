class Deal:
    def __init__(self, title: str, time: int, source: str):
        self.title = title
        self.time = time
        self.source = source

    def __hash__(self):
        return hash((self.title, self.time, self.source))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False

        return (
            self.title == other.title and 
            self.time == other.time and 
            self.source == other.source
        )