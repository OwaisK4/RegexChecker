import regex as re
from regex import Match

class Regex():
    def __init__(self, text: str) -> None:
        self.text = text

    def detect(self) -> list[str]:
        types = ["Phone", "CNIC", "Age"]
        result = [[f"{types[i]} entities:"] for i in range(len(types))]
        for type in types:
            iterator = self.detect_entity(self.text, type)
            if iterator:
                # result.append(f"Detected {type} entities:")
                for match in iterator:
                    answer = f"Detected\"{match.group()}\"" + " starting at index: " + str(match.start())
                    result[types.index(type)].append(answer)
        
        return result

    def detect_entity(self, text: str, type: str):
        pattern = None
        if type == "Phone":
            pattern = r"(\+?92|0)([.-]?)3(\d{2})([.-]?)(\d{3})([.-]?)(\d{4})"
        elif type == "CNIC":
            pattern = r"4\d{4}[.-]?\d{7}[.-]?\d"
        else:
            pattern = r"(?<=age.{0,50})(?<!\d)\d{1,3}(?!\d)|(?<!\d)\d{1,3}(?!\d)(?=.{0,50}age)"
        matched = re.finditer(pattern, text)
        return matched

    """
    def detect_phone(self, text: str):
        # Explanation: A number beginning with either 92 (optionally preceded by a +) or 0, followed by a 3
        # followed by 9 digits (2 + 3 + 4) with optional separators after the prefix, 2 digits after 3, and 5 digits after 3.
        pattern = r"(\+?92|0)(.?)3(\d{2})(.?)(\d{3})(.?)(\d{4})"
        matched = re.finditer(pattern, text)
        return matched
    
    def detect_CNIC(self, text: str):
        pattern = r"4\d{4}.?\d{7}.?\d"
        matched = re.finditer(pattern, text)
        return matched
    
    def detect_age(self, text: str):
        pattern = r"(?<=age.{0,50})\d{1,3}|\d{1,3}(?=.{0,50}age)"
        matched = re.finditer(pattern, text, flags=re.IGNORECASE)
        return matched
    """