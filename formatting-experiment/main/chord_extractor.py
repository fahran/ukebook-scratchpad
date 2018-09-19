import re

def extract_chords(raw_body):
    between_parens_regex = r"\((.*?)\)"
    chord_candidates = set(re.findall(between_parens_regex, raw_body))
    chords = [chord for chord in chord_candidates if _is_chord(chord)]
    return sorted(list(chords))

def _is_chord(input):
    roots = {"A", "B", "C", "D", "E", "F", "G"}
    numbers = {i for i in range(1, 14)}
    extras = {"+", "aug", "/", "dim", "sus", "add"}
    return input[:1] in roots
    

class Chord:

    def __init__(self, string):
        self.root = string[:1]
        self.slash = "/" in string