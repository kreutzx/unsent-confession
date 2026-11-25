import os

# Unsent: The Micro-Confession Sprint — To: line + the unsent message, nothing after.
# Genuinely unsent, not a joke: the promotion is the felt reason it stayed in drafts.
ENTRY_TEXT = "To: my old boss\nI found the resignation I wrote in March. I never sent it because you promoted me in April — and I still don't know which one of us was wrong."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
