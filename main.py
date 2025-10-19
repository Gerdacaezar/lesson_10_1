from src.external_api import convert_to_rub
from src.utils import read_json_file


def main() -> None:
    pass


if __name__ == "__main__":
    main()
    print(convert_to_rub(1, "EUR"))
    print(read_json_file('data/test_json_file.json'))
