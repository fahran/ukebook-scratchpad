from unittest import TestCase

import main
from main import song_converter
import unittest

class SongConverterTest(unittest.TestCase):
    def test_title_and_artist(self):
        expected = "<section class='title-line'>A Little Respect - Erasure</section>\n\n"
        self.assertEqual(song_converter.to_html("A Little Respect", "Erasure", ""), expected)

    def test_sections_are_wrapped(self):
        expected = (
                    "<section class='title-line'>title - artist</section>\n\n"
                    "<section class='song-section'>hello</section>"
                )

        self.assertEqual(song_converter.to_html("title", "artist", "hello"), expected)

    def test_sections_escape_html(self):
        expected = (
                    "<section class='title-line'>&lt;b&gt;title&amp;&lt;/b&gt; - &lt;b&gt;artist&amp;&lt;/b&gt;</section>\n\n"
                    "<section class='song-section'>&lt;b&gt;hello&amp;&lt;/b&gt;</section>"
                )

        self.assertEqual(song_converter.to_html("<b>title&</b>", "<b>artist&</b>", "<b>hello&</b>"), expected)

    def test_sections_separated_by_whitespace(self):
        raw_song_body = (
            "hello\n"
            "\n"
            "world"
        )

        expected = (
            "<section class='title-line'>title - artist</section>\n\n"
            "<section class='song-section'>hello</section>\n"
            "<section class='song-section'>world</section>"
        )

        self.assertEqual(song_converter.to_html("title", "artist", raw_song_body), expected)

    def test_new_lines_are_not_new_sections(self):
        raw_song_body = (
            "hello\n"
            "world"
        )

        expected = (
            "<section class='title-line'>title - artist</section>\n\n"
            "<section class='song-section'>hello\n"
            "world</section>"
        )

        self.assertEqual(expected, song_converter.to_html("title", "artist", raw_song_body))

    def test_basic_chord_identification(self):
        expected = (
            "<section class='title-line'>title - artist</section>\n\n"
            "<section class='song-section'>hello <span class='chord'>(C)</span>world</section>"
        )
        raw_song_body = "hello (C)world"

        self.assertEqual(song_converter.to_html("title", "artist", raw_song_body), expected)


    def test_lone_chord_identification(self):
        raw_song_body = "(C)"
        expected = (
            "<section class='title-line'>title - artist</section>\n\n"
            "<section class='song-section'><span class='chord'>(C)</span></section>"
        )
        self.assertEqual(song_converter.to_html("title", "artist", raw_song_body), expected)

    def test_chords_not_identified_in_title(self):
        expected = (
            "<section class='title-line'>title(C) - artist</section>\n\n"
            "<section class='song-section'>hello <span class='chord'>(C)</span>world</section>"
        )
        raw_song_body = "hello (C)world"

        self.assertEqual(song_converter.to_html("title(C)", "artist", raw_song_body), expected)

    def test_lone_section_tag_identification(self):
        raw_song_body = "[intro]"
        expected = (
            "<section class='title-line'>title - artist</section>\n\n"
            "<section class='song-section'><span class='section-tag'>[intro]</span></section>"
        )

        self.assertEqual(song_converter.to_html("title", "artist", raw_song_body), expected)

if __name__ == '__main__':
    unittest.main()
