def analyze_sentence(text):
    """Analyze a sentence: count characters, words, and check for 'Python'."""
    text = text.strip()
    total_chars = len(text)
    total_words = len(text.split())
    has_python = "python" in text.lower()
    return total_chars, total_words, has_python


if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    chars, words, contains = analyze_sentence(user_input)

    print(f"Total characters: {chars}")
    print(f"Word count: {words}")
    print(f"Contains 'Python': {contains}")

