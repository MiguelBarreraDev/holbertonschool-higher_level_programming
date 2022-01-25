#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    text is the text to evaluate
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines, start, end = ([], 0, 0)
    for c in text:
        if c in ['.', '?', ':']:
            lines.append(text[start:end + 1])
            start = end + 1
        end += 1

    lines.append(text[start:])

    lines = list(map(lambda line: line.strip(), lines))
    for line in lines:
        print(line)
        if line != lines[-1]:
            print()
