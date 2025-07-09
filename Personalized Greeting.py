def get_user_name():
    first_name = input("Enter your first name: ").strip().capitalize()
    last_name = input("Enter your last name: ").strip().capitalize()
    return f"{first_name} {last_name}"


def main():

    full_name = get_user_name()
    print(f"Hello, {full_name}! Welcome to Python program")

if __name__ == "__main__":
    main()