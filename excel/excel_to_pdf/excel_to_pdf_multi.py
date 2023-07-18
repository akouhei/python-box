"""
configファイルから読み込み => List
正規表現で指定 => List
"""

import excel_to_pdf as ex
import glob
import argparse
import pandas as pd

KEYWORD_CONFIG = "config"
KEYWORD_REGEX = "regex"
CONFIG_FILENAME = "Excel_to_PDF.conf"


def main(mode, regex_key, config_path, print_area, save_path, sheet_name):
    file_paths = []
    sheet_names = []
    print_areas = []

    # 設定の読み込み処理
    if mode == KEYWORD_CONFIG:
        # 設定ファイルの読み込み
        (file_paths, sheet_names, print_areas) = load_from_config_file()
    elif mode == KEYWORD_REGEX:
        # ディレクトリから読み込み
        file_paths = load_from_directory(regex_key)
        sheet_names = [sheet_name] * len(file_paths)
        print_areas = [print_area] * len(file_paths)
    else:
        raise ValueError("処理モードは適切に選択してください")

    # ExcelファイルのPDF化
    excel_to_pdf_mult(file_paths, sheet_names, print_areas, save_path)


def load_from_config_file():
    # 設定読み込み(どんな文字列も欠損値として扱わない)
    df = pd.read_csv(CONFIG_FILENAME, na_filter=False)
    # 文字列 "None" は Noneに変換してから返却
    return [list(df["filepath"]), list(df["sheet_name"]), [None for t in list(df["print_area"]) if t == "None"]]


def load_from_directory(regex):
    # 正規表現を利用した読み込み
    file_paths = glob.glob(regex, recursive=True)
    return file_paths


def excel_to_pdf_mult(file_paths, sheet_names, print_areas, save_path=None):
    for (file_path, sheet_name, print_area) in zip(file_paths, sheet_names, print_areas):
        # ExcelファイルをPDFに変換
        ex.excel_to_pdf(file_path, sheet_name, print_area, save_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Excel to PDF")
    parser.add_argument("-m", "--mode", type=str, default=KEYWORD_CONFIG,
                        help="mode=regexならば、globメソッド対応の正規表現でPDF化するファイルを指定。"
                        "mode=configならば設定ファイルに記載されたファイルをPDF化する。")
    # mode = regex 特有設定項目
    parser.add_argument("-r", "--regex", type=str, help="正規表現、mode=regexのときのみに利用")
    parser.add_argument("-p", "--print_range", type=str, default=None,
                        help="印刷範囲指定、mode=regexのときのみに使用,")
    parser.add_argument("-n", "--sheet_name", type=str, default="Sheet1",
                        help="変換対象のExcelシート名、mode=regexのときのみに使用")
    # mode = config 特有設定項目
    parser.add_argument("-c", "--config_path", type=str, default=CONFIG_FILENAME,
                        help="設定ファイル名、mode=configのときのみに利用")
    parser.add_argument("-s", "--save_path", type=str, default=None, help="保存先のパス")

    args = parser.parse_args()

    main(args.mode, args.regex, args.config_path, args.print_range, args.save_path, args.sheet_name)

