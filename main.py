from src.read_csv_xlsx_files import read_csv_file, read_excel_file


def main() -> None:
    print(read_csv_file('data/example.csv'))
    print(read_excel_file('data/example.xlsx'))
    pass


if __name__ == "__main__":
    main()
