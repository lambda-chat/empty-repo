from dotenv import load_dotenv


if __name__ == "__main__":
    import os

    load_dotenv()
    print(os.environ["USERNAME"])
    print(os.environ["PASSWORD"])
