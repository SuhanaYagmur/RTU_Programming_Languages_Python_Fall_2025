def welcome_user(person):
    formatted = person.strip().title()
    greeting = f"Hey {formatted}, glad to see you learning Python!"
    return greeting

if __name__ == "__main__":
    username = input("What's your name? ").strip()
    print(welcome_user(username))

