'''
実現したい機能：
・指定したパスにフォルダを作成する。
・フォルダ名を記載したcsvファイルを読み込み、作成するフォルダを指定
・読み込むCVSファイルは、引数で指定する。（デフォルトフォルダ名も設定する）
・フォルダ作成前に作成するかどうか確認する。

・入力
    ・対象ディレクトリ
        ・ディレクトリが存在するか確認
    ・CSVファイル名
        ・指定のファイル名が存在するか確認
・出力
    ・なし
・処理
    ・CSVから情報読み込み、ファイル名のリストを返却
'''
import os
import csv

FILE_ENCODE = "UTF-8"


def get_folder_name_from_csv(filename, col_num=1):
    """ csvファイルからフォルダ名を取得する。
    :param str filename: csvファイル名
    :param int col_num: ファイル名として抽出する列の指定
    :return: 取得したファイル名のリスト
    """
    # csvからフォルダ名を取得する。
    if not os.path.isfile(filename):
        return []
    with open(filename, mode="r", encoding=FILE_ENCODE) as file:
        return [row[col_num - 1] for row in csv.reader(file)]


def mkfolders(root_path, csv_name="folder_list.csv"):
    """ フォルダを作成する。
    指定したroot_path内に存在するCSVファイルから、ファイル名（もしくはパス）を抽出し
    root_path配下にディレクトリを作成する。
    既に指定フォルダが存在する場合は、無視し、フォルダ作成できなかった旨を標準出力する。
    :param root_path: フォルダ作成の対象ディレクトリ
    :param csv_name: CSVファイル名
    :return:
    """
    # ディレクトリの存在確認
    if not os.path.isdir(root_path):
        raise FileNotFoundError("ディレクトリは存在しません。")

    # csvファイル情報を読み込む
    lines = read_csv(os.path.join(root_path, csv_name))

    # フォルダを作成する
    for line in lines:
        filename = line[0]
        try:
            os.mkdir(path=os.path.join(root_path, filename))
        except FileExistsError as e:
            print(e)


def read_csv(csv_path):
    """ csvファイルをリストに変換する
    :param csv_path:
    :return:
    ※ CSVのセル内の文字列にカンマを利用している場合は、正常に動作しない。
    """
    if not os.path.isfile(csv_path):
        return []
    with open(csv_path, mode="r", encoding=FILE_ENCODE) as file:
        return [f.split(sep=",") for f in file.readlines()]
