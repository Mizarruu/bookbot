def get_book_text(filepath: str) -> str:
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
def count_words(text: str) -> int:
    words = text.split()
    return len(words)
def main() -> None:
    path = "./books/frankenstein.txt"  # relativer Pfad in deinem Repo
    text = get_book_text(path)
    num_words = count_words(text)
    print(f"Found {num_words} total words")
if __name__ == "__main__":
    main()

