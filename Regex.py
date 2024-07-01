import regex as re
from Pattern import BasePattern, PatternFactory
from Matcher import Matcher, MatchedEntity

class Regex():
    def __init__(self, text: str) -> None:
        self.text = text
        self.detectors = ["Phone", "CNIC", "Age", "Email"]

    def process(self) -> dict[str, list[MatchedEntity]]:
        extracted = {}
        for detector in self.detectors:
            pattern: BasePattern = PatternFactory(detector)
            string = " ".join(self.text.split("\n"))
            matcher: Matcher = Matcher(string, pattern)
            results = matcher.process()
            extracted[detector] = results
        return extracted