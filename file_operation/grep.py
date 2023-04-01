"""
Version = 1.0
参考URL：dataclass : https://zasshoku-ds.com/dataclass/#toc4
参考URL：コメントの書き方：https://qiita.com/simonritchie/items/49e0813508cad4876b5a
"""
from colorama import Fore, Style
import colorama
import re
import dataclasses
import glob
import os
import argparse


# イミュータブル（変更不可）データクラス
@dataclasses.dataclass(frozen=True)
class LineDataClass:
    """
    行情報を保持する。

    Attributes
    ----------
    row : int
        行数。
    line : str
        行に対応する文字列。
    filepath : dict
        ファイル名。
    """
    row: int
    line: str
    filepath: str


def __main(pattern, paths, recursive):
    greps(pattern, paths, recursive=recursive)


def greps(pattern, paths, is_print=True, is_color=True, recursive=False):
    """
    指定したファイルから特定のキーワードを含む文字列を取得する。

    Parameters
    ----------
    pattern : str
        検索キーワード。
    paths : str
        検索対象のファイル名。
    is_print : bool
        検索結果を画面に表示するか否か。
    is_color : bool
        色付けするか否か。
    recursive : bool
        再帰的にファイルを処理するか否か。

    Returns
    -------
    line_data_list : list[LineDataClass]
        検索結果情報のリスト。
    """
    line_data_list = []

    # ファイルパスの取得
    filepaths = [path for path in glob.glob(paths, recursive=recursive) if os.path.isfile(path)]

    # ファイル内の文字列変換
    for filepath in filepaths:
        line_data_list.extend(grep(pattern, filepath, is_print, is_color))

    return line_data_list


def grep(pattern, filepath, is_print=True, is_color=True):
    """
    指定したファイルから特定のキーワードを含む文字列を取得する。

    Parameters
    ----------
    pattern : str
        検索キーワード。
    filepath : str
        検索対象のファイル名。
    is_print : bool
        検索結果を画面に表示するか否か。
    is_color : bool
        色付けするか否か。

    Returns
    -------
    line_data_list : list[LineDataClass]
        検索結果情報のリスト。
    """

    # 色の初期化
    colorama.init()
    line_data_list = []

    if not os.path.isfile(filepath):
        print("指定されたファイルは存在しません")
        exit()

    # ファイルを一括読み込み
    with open(filepath, 'r', encoding="UTF-8") as file:
        lines = file.readlines()

    # Grep
    for i, line in enumerate(lines):
        match = re.search(pattern, line)
        if match:
            # 色付きで文字列を作成する
            if is_color:
                ans_line = line[:match.start()] \
                           + Fore.RED + Style.BRIGHT + match.group() \
                           + Style.RESET_ALL + line[match.end():]
            else:
                ans_line = line

            line_data_list.append(LineDataClass(row=i + 1, line=ans_line, filepath=filepath))

    if is_print:
        for data in line_data_list:
            print("{} {:>3d}: {}".format(data.filepath, data.row, data.line), end="")

    # 色付きで文字列を返却
    return line_data_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="replace string in files")
    parser.add_argument("pattern", type=str, help="pattern(regular expression)")
    parser.add_argument("filepaths", type=str, help="filepaths(regular expression)")
    parser.add_argument("-r", "--recursive", action='store_true', default=False, help="True of False about reading files recursively")

    args = parser.parse_args()

    __main(args.pattern, args.filepaths, args.recursive)
