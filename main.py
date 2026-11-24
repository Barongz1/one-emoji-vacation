"""One Emoji, One Dream Vacation — entry for make.fun.

Writes one emoji to /output/entry.txt.
The emoji is exactly one emoji for our dream vacation, and nothing else.
"""
import os

EMOJI = "🏝️"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI + "\n")

if __name__ == "__main__":
    main()
