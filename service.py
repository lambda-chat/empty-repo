from dotenv import load_dotenv


if __name__ == "__main__":
    import os

    load_dotenv()
    print(os.environ["USER_NAME"])
    print(os.environ["PASSWORD"])
