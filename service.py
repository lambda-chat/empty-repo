from functools import lru_cache

from dotenv import load_dotenv

TAX_RATIO = 1.1


@lru_cache
def fib(n: int) -> int:
    if n <= 0:
        raise ValueError(n)
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def gross(net: float) -> float:
    return net * TAX_RATIO


if __name__ == "__main__":
    import os

    load_dotenv()
    print(".env ファイルから環境変数を読み込みました")
    print(os.environ["USERNAME"])
    print(os.environ["PASSWORD"])

    print(fib(6))
    print(gross(100))
