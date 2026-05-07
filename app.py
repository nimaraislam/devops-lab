from config import APP_NAME, VERSION
def main():
    name = input("What is your name? ")
    print(f"Welcome to the app, {name}!")
    print(f"Welcome to {APP_NAME} v{VERSION}")

if __name__ == "__main__":
    main()