from Regex import Regex
from Matcher import MatchedEntity

if __name__ == "__main__":
    text = "owais19alikhanage"
    regex: Regex = Regex(text)
    extracted: dict[list[MatchedEntity]] = regex.process()
    for key, value in extracted.items():
        print(key)
        for i in range(len(value)):
            match: MatchedEntity = value[i]
            print(str(i + 1) + ". Group = ", match.matched + ", Index = " + str(match.index) + " Length = " + str(match.length))
        print()