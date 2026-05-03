VERSES = [
    ["This is the house that Jack built.", "that lay in the house that Jack built."],
    ["This is the malt", "that ate the malt"],
    ["This is the rat", "that killed the rat"],
    ["This is the cat", "that worried the cat"],
    ["This is the dog", "that tossed the dog"],
    ["This is the cow with the crumpled horn", "that milked the cow with the crumpled horn"],
    ["This is the maiden all forlorn", "that kissed the maiden all forlorn"],
    ["This is the man all tattered and torn", "that married the man all tattered and torn"],
    ["This is the priest all shaven and shorn", "that woke the priest all shaven and shorn"],
    ["This is the rooster that crowed in the morn", "that kept the rooster that crowed in the morn"],
    ["This is the farmer sowing his corn", "that belonged to the farmer sowing his corn"],
    ["This is the horse and the hound and the horn", ""],
]


def recite(start_verse, end_verse):
    return [
        " ".join([VERSES[i][int(index != 0)] for index, i in enumerate(list(range(start, -1, -1)))])
        for start in list(range(start_verse - 1, end_verse))
    ]
