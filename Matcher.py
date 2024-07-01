from Pattern import BasePattern
import regex as re
from dataclasses import dataclass

@dataclass
class MatchedEntity():
    index: int
    matched: str
    length: int

class Matcher():
    def __init__(self, string: str, pattern: BasePattern) -> None:
        self.string: str = string
        self.pattern: BasePattern = pattern
    
    def process(self) -> list[MatchedEntity]:
        results: list[MatchedEntity] = []
        for match in re.finditer(self.pattern.pattern, self.string):
            print("Match", match)
            index = match.start()
            matched = match.group()
            length = match.end() - match.start()
            matchedEntity: MatchedEntity = MatchedEntity(index, matched, length)
            results.append(matchedEntity)
        return results
            
