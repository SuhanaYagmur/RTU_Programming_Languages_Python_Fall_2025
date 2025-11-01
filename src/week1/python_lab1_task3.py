def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    length = len(text)
    word_count = len(text.split())
    contains_python = "python" in text.lower()
    return length, word_count, contains_python

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    length, words, has_python = analyze_sentence(text)
    print(f"Total characters: {length}")
    print(f"Word count: {words}")
    print(f"Contains 'Python': {has_python}")

