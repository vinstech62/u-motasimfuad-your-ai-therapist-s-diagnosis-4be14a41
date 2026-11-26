#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis - make.fun entry.

Writes one single-line diagnosis (1-200 chars, UTF-8) to /output/entry.txt.
The line is fixed text: the program is deterministic, no input, no network.
"""
import os

LINE = (
    "Diagnosis: acute prompt dependency \u2014 you only feel heard "
    "when something with no feelings says 'I understand.'"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
