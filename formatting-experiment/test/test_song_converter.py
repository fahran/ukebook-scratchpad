import sys, os
from unittest import TestCase

import main
from main import song_converter
import unittest

class SongConverterTest(unittest.TestCase):
    def test_sections_are_wrapped(self):
        self.assertEqual("<section class='song-section'>hello</section>", song_converter.to_html("hello"))

    def test_sections_escape_html(self):
        self.assertEqual("<section class='song-section'>&lt;b&gt;hello&amp;&lt;/b&gt;</section>", song_converter.to_html("<b>hello&</b>"))

    def test_sections_separated_by_whitespace(self):
        raw = (
            "hello\n"
            "\n"
            "world"
        )

        expected = (
            "<section class='song-section'>hello</section>\n"
            "<section class='song-section'>world</section>"
        )

        self.assertEqual(expected, song_converter.to_html(raw))

    def test_new_lines_are_not_new_sections(self):
        raw = (
            "hello\n"
            "world"
        )

        expected = (
            "<section class='song-section'>hello\n"
            "world</section>"
        )

        self.assertEqual(expected, song_converter.to_html(raw))

    def test_basic_chord_identification(self):
        raw = "hello (C)world"
        self.assertEqual("<section class='song-section'>hello <span class='chord'>(C)</span>world</section>", song_converter.to_html(raw))

    def test_lone_chord_identification(self):
        raw = "(C)"
        self.assertEqual("<section class='song-section'><span class='chord'>(C)</span></section>", song_converter.to_html(raw))

    def test_lone_section_tag_identification(self):
        raw = "[intro]"
        self.assertEqual("<section class='song-section'><span class='section-tag'>[intro]</span></section>", song_converter.to_html(raw))

if __name__ == '__main__':
    unittest.main()
