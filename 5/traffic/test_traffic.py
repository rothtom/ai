import pytest
import traffic

def main():
    test_load_data()


def test_load_data():
    assert traffic.load_data("gtsrb/") == NotImplementedError


if __name__ == "__main__":
    main()