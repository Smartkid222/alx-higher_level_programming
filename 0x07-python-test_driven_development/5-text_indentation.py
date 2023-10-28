#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = 0
    while s < len(text) and text[s] == ' ':
        s += 1

    while s < len(text):
        print(text[s], end="")
        if text[s] == "\n" or text[s] in ".?:":
            if text[s] in ".?:":
                print("\n")
            s += 1
            while s < len(text) and text[s] == ' ':
                s += 1
            continue
        s += 1
