from unittest import TestCase

import main
from main import chord_extractor
import unittest
import random

class SongConverterTest(unittest.TestCase):
    def test_basic_chord_detection(self):
        expected = ["A", "B", "C"]
        self.assertEqual(chord_extractor.extract_chords("(A)Hello (B) World\n(C)"), expected)

    def test_chords_only_appear_once(self):
        expected = ["A", "B", "C"]
        self.assertEqual(chord_extractor.extract_chords("(A)Hello (B) (B)World\n(C)"), expected)

    def test_long_chords(self):
        expected = ["A", "B", "C#MajSus7"]
        self.assertEqual(chord_extractor.extract_chords("(A)Hello (B) World\n(C#MajSus7)"), expected)

    def test_chords_are_sorted_alphabetically(self):
        expected = ["A", "B", "C#MajSus7"]
        self.assertEqual(chord_extractor.extract_chords("(C#MajSus7) (A)Hello \n(B) World"), expected)

    def test_slash_chords_are_identified(self):
        expected = ["A#/C", "A+sus4/G#dim6", "B"]
        self.assertEqual(chord_extractor.extract_chords("(A#/C) (A+sus4/G#dim6)Hello \n(B) World"), expected)

    def test_directions_are_not_chords(self):
        expected = ["A", "B", "C#MajSus7"]
        self.assertEqual(chord_extractor.extract_chords("(A)(oop-do-wee) (B) World\n(C#MajSus7)"), expected)

    def test_all_chords_are_found_using_property_based_testing(self):
        roots = ["A", "B", "C", "D", "E", "F", "G"]
        pitch_modifiers = ["", "#", "b"]
        augmentations = ["", "+", "sus4", "sus7", "sus5", "dim3", "dim3", "Maj7", "Maj", "m", "add"]

        generated_chords = [random.choice(roots) + random.choice(pitch_modifiers) + random.choice(augmentations) for i in range(100)]
        common_words = ["a","about","all","also","and","as","at","be","because","but","by","can","come","could",
        "day","do","even","find","first","for","from","get","give","go","have","he","her","here","him","his","how",
        "I","if","in","into","it","its","just","know","like","look","make","man","many","me","more","my","new","no",
        "not","now","of","on","one","only","or","other","our","out","people","say","see","she","so","some","take","tell",
        "than","that","the","their","them","then","there","these","they","thing","think","this","those","time","to","two",
        "up","use","very","want","way","we","well","what","when","which","who","will","with","would","year","you","your",
        "feel" "love", "take", "time", "never", "life", "die", "eye", "back", "day", "world", "heart", "man", "night", 
        "girl", "mind", "away", "live", "dream", "again"]
        
        generated_song = ""
        for chord in generated_chords:
            line = f"({chord}){random.choice(common_words)} ({random.choice(generated_chords)}) {random.choice(common_words)} {random.choice(common_words)}"
            generated_song += (line + "\n")

        found_chord_result = chord_extractor.extract_chords(generated_song)

        self.assertEqual(sorted(found_chord_result), sorted(set(generated_chords)))

    

