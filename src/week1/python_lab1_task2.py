def greet_user(name):
    """Return a greeting message after cleaning and capitalizing the name."""
    clean_name = name.strip().capitalize()
    return f"Hello, {clean_name}! Welcome to Python!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    message = greet_user(name)
    print(message)
