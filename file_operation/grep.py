"""
Version = 1.0
参考URL：dataclass : https://zasshoku-ds.com/dataclass/#toc4
参考URL：コメントの書き方：https://qiita.com/simonritchie/items/49e0813508cad4876b5a
"""
from colorama import Fore, Style
import colorama
import re
import dataclasses


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
    filename : dict
        ファイル名。
    """
    row: int
    line: str
    filename: str


def grep(pattern, filename, is_print=False, is_color=True):
    """
    指定したファイルから特定のキーワードを含む文字列を取得する。

    Parameters
    ----------
    pattern : str
        検索キーワード。
    filename : str
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

    # ファイルを一括読み込み
    with open(filename, 'r', encoding="UTF-8") as file:
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

            line_data_list.append(LineDataClass(row=i + 1, line=ans_line, filename=filename))

    if is_print:
        for data in line_data_list:
            print("{} {:>3d}: {}".format(data.filename, data.row, data.line), end="")

    # 色付きで文字列を返却
    return line_data_list
