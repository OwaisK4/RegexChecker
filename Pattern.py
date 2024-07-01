class BasePattern():
    def __init__(self) -> None:
        self.pattern = ""

    def show(self) -> str:
        return self.pattern
    
class PhonePattern(BasePattern):
    def __init__(self) -> None:
        super().__init__()
        self.pattern = r"(\+?92|0)?([.-]?)3(\d{2})([.-]?)(\d{3})([.-]?)(\d{4})"

class AgePattern(BasePattern):
    def __init__(self) -> None:
        super().__init__()
        self.pattern = r"(?<=age.{0,50})(?<!\d)\d{1,3}(?!\d)|(?<!\d)\d{1,3}(?!\d)(?=.{0,50}age)"

class CNICPattern(BasePattern):
    def __init__(self) -> None:
        super().__init__()
        self.pattern = r"4\d{4}[.-]?\d{7}[.-]?\d"

class EmailPattern(BasePattern):
    def __init__(self) -> None:
        super().__init__()
        self.pattern = r"[A-Za-z0-9\._%+\-]+@[A-Za-z0-9\.\-]+\.[A-Za-z]{2,}"

def PatternFactory(type: str) -> BasePattern:
    generator = {"phone": PhonePattern, "age": AgePattern, "cnic": CNICPattern, "email": EmailPattern}
    pattern = generator.get(type.lower(), None)
    if pattern:
        return pattern()
    else:
        return None
    # if type.lower() == "phone":
    #     return PhonePattern()
    # elif type.lower() == "age":
    #     return AgePattern()
    # elif type.lower() == "cnic":
    #     return CNICPattern()
    # elif type.lower() == "email":
    #     return EmailPattern()
    # else:
    #     return None