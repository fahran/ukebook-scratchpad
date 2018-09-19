import html
import re

def to_html(title, artist, raw_song_body):
    title = f"<section class='title-line'>{html.escape(title)} - {html.escape(artist)}</section>\n\n"
    return title + _body_to_html(raw_song_body)

def _body_to_html(raw):
    raw_sections = raw.split("\n\n")
    sections = []
    for section in raw_sections:
        if section != "":
            sections.append("<section class='song-section'>" + html.escape(section) + "</section>\n")

    song = "".join(sections).strip("\n")
    return _wrap_section_tags(_wrap_chords(song))


def _wrap_chords(string):
    chord_regex = r"(\((.*?)\))"
    replacement = r"<span class='chord'>\1</span>"
    return re.sub(chord_regex, replacement, string)

def _wrap_section_tags(string):
    section_tag_regex = r"(\[(.*?)\])"
    replacement = r"<span class='section-tag'>\1</span>"
    return re.sub(section_tag_regex, replacement, string)