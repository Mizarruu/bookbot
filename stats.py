def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict:
    text = text.lower().replace("\ufeff", "")
    char_counts = {}  # <- DICTIONARY HEISST char_counts !!!

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts