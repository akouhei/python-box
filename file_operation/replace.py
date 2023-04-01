"""
ToDo : バックアップファイルが上書きされないようになど工夫が必要か？

"""
import re
import shutil
import glob
import os
import argparse


def __main(filepaths, old_string, new_string, backup, recursive):
    replace_string_in_files(filepaths, old_string, new_string, backup, recursive)


def replace_string_in_files(paths, old_string, new_string, backup=False, recursive=False):
    """
        指定したファイルの文字列を置換する。（複数ファイルに対応。正規表現で指定）
        Parameters
        ----------
        paths : str
            ファイル名
        old_string : str
            変換対象の文字列
        new_string : str
            変換後の文字列
        backup : bool
            メタデータバックアップをとるか否か
        recursive : bool
            再帰的にファイルを指定するか否か

        Returns
        -------

        """
    # ファイルパスの取得
    filepaths = [path for path in glob.glob(paths, recursive=recursive) if os.path.isfile(path)]

    # ファイル内の文字列変換
    for filepath in filepaths:
        replace_string_in_file(filepath, old_string, new_string, backup=backup)


def replace_string_in_file(filepath, old_string, new_string, backup=False):
    """
    指定したファイルの文字列を置換する。
    Parameters
    ----------
    filepath : str
        ファイル名
    old_string : str
        変換対象の文字列
    new_string : str
        変換後の文字列
    backup : bool
        メタデータバックアップをとるか否か

    Returns
    -------

    """
    replaced_lines = []
    pattern = re.compile(old_string)

    if not os.path.isfile(filepath):
        print("指定されたファイルは存在しません")
        exit()

    # 置換後文字列の取得
    with open(filepath, 'r', encoding="UTF-8") as file:
        for line in file.readlines():
            replaced_lines.append(pattern.sub(new_string, line))

    # バックアップファイルの作成
    if backup:
        shutil.copy2(filepath, filepath + ".back")

    # 書き込み
    with open(filepath, 'w', encoding="UTF-8") as file:
        file.writelines(replaced_lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="replace string in files")
    parser.add_argument("filepaths", type=str, help="filepaths(regular expression)")
    parser.add_argument("old_string", type=str, help="old string")
    parser.add_argument("new_string", type=str, help="new string")
    parser.add_argument("-b", "--backup", action='store_true', default=False, help="True of False about auto backup")
    parser.add_argument("-r", "--recursive", action='store_true', default=False, help="True of False about reading files recursively")

    args = parser.parse_args()

    __main(args.filepaths, args.old_string, args.new_string, args.backup, args.recursive)

"""
* w : 上書き
* a : 末尾
* x : 排他処理、既にファイルが存在するとFileExistError
"""


"""
write, writelinesの違い
* write : 単純に書き込み
* writelines : 文字列のリストをまとめて書き込み

"""



"""
read, readline, readlinesの違い
* read
  指定サイズのデータを読み込む。引数省略で内容すべてを読み込む
* readline
  1行だけ読みだす。
* readlines
  1行ごとのリストに変換して、すべてを読み込む。
"""


"""
re.sub(pattern, repl, string, count=0, flags=0)
    正規表現パターンにマッチした文字列を、別の文字列に置換するPythonの組み込み関数です。
    
    引数の意味は以下の通りです。
    * pattern: 正規表現パターンを表す文字列です。
    * repl: 置換に使用する文字列です。
    * string: 置換対象の文字列です。
    * count: 置換を行う最大の回数です。デフォルト値は0で、すべてのマッチを置換します。
    * flags: 正規表現のコンパイルフラグです。デフォルト値は0です。

re.compileを用いた置換
    pattern = re.compile(正規表現)関数で、正規表現オブジェクトを作成できる。
    result = pattern.sub(repl, string)　で置換後の文字列を生成。
"""


"""
import re
import os

def replace_in_file(filename, pattern, replacement):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    content = re.sub(pattern, replacement, content)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def replace_in_files(file_pattern, pattern, replacement):
    for root, dirs, files in os.walk('.'):
        for file in files:
            if re.match(file_pattern, file):
                replace_in_file(os.path.join(root, file), pattern, replacement)

"""