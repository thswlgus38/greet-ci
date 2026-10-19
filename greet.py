import sys


def greet(name: str) -> str:
    return f"Hello, {name}!"


def test_greet() -> None:
    assert greet("Hee") == "Hello, Hee!"


if __name__ == "__main__":
    name_arg = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name_arg))