import csv
import io
from typing import List, Dict, Tuple, NamedTuple


class CsvColumn(NamedTuple):
    name: str
    data: List[str]


class CsvProcessor:
    def __init__(self, file_path: str, delimiter: str = ',', headers_row: int = 0):
        self.file_path = file_path
        self.delimiter = delimiter
        self.headers_row = headers_row
        self.headers = []
        self.data = []
        self._read_csv()

    def _read_csv(self) -> None:
        with open(self.file_path, 'r', encoding="UTF-8") as file:
            csv_reader = csv.reader(file, delimiter=self.delimiter)
            # ヘッダー行まで読み飛ばす
            for _ in range(self.headers_row):
                next(csv_reader)
            # ヘッダー行を読み込む
            self.headers = next(csv_reader, [])
            # データ行を読み込む
            for row in csv_reader:
                self.data.append(row)

    def _write_csv(self) -> None:
        with open(self.file_path, 'w', encoding="UTF-8") as file:
            csv_writer = csv.writer(file, delimiter=self.delimiter)
            # ヘッダーとデータ行を行単位で書き込み
            csv_writer.writerow(self.headers)
            csv_writer.writerows(self.data)

    def _get_column_index(self, column_name: str) -> int:
        try:
            # 指定したヘッダ名の列番号を返却する
            return self.headers.index(column_name)
        except ValueError:
            raise ValueError(f"Column '{column_name}' does not exist in CSV file")

    def extract_column(self, column_name: str) -> List[str]:
        # データから指定列を抽出
        column_index = self._get_column_index(column_name)
        return [row[column_index] for row in self.data]

    def insert_column(self, column_name: str, values: List[str]) -> None:
        # 挿入する列の行数確認
        if len(values) != len(self.data):
            raise ValueError("The number of values does not match the number of rows in CSV file")
        # 挿入する列が重複してないことを確認
        if column_name in self.headers:
            raise ValueError(f"Column '{column_name}' already exists in CSV file")

        # 新たに列を追加
        self.headers.append(column_name)
        # データの行リストを取り出し挿入
        for i, row in enumerate(self.data):
            row.append(values[i])
        self._write_csv()

    # この部分要注意
    def calculate_columns(self, calculation: Dict[str, str]) -> None:
        for i, row in enumerate(self.data):
            for header, expression in calculation.items():
                column_index = self._get_column_index(header)
                values = {self.headers[j]: float(row[j]) for j in range(len(self.headers))}
                result = str(eval(expression, values))
                row[column_index] = result
        self._write_csv()
