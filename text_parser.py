from io import BufferedReader

class Parser():
    def __init__(self, text: str = None, file: BufferedReader = None) -> None:
        self.text: str = None
        # self.file: BufferedReader = None
        assert not text or not file, "Error. Only one input stream allowed."
        # assert text or file, "Error. At least one input stream must be provided."
        if text:
            self.text = text
        elif file:
            self.text = file.read()
    
    def getText(self) -> str:
        return self.text