class Title:
    def __init__(self, title: str, text: str, level: int) -> None:
        self.title = title
        self.level = level
        self.text = text
    
    def __str__(self):
        return f'{self.title}: {self.text[:40]}...'