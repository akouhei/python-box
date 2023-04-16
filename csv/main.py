import csvprocessor


def main():
    csvpro = csvprocessor.CsvProcessor(file_path="test.csv", headers_row=0)
    print(csvpro.extract_column("a"))
    print(csvpro.calculate_columns({"time * a": "cod"}))

main()