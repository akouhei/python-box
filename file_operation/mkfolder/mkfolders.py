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

FILE_ENCODE = "UTF-8"


def mkfolders(root_path, csv_name="folder_list.csv"):
    


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
