"""
 excel_to_pdf
処理：
入力；エクセルパス名、シート名、印刷反映
出力：なし、（内側でpdfの作成）
"""
import os
from platform import system
import xlwings as xw
from enum import Enum


def excel_to_pdf(file_path, sheet_name, print_area=None, save_path=None):
    """ エクセルファイルの特定シートをpdf化する
    処理：指定したエクセルファイルのシートを印刷する
    :param str file_path: エクセルファイルパス
    :param str sheet_name: シート名
    :param str print_area: 印刷範囲
    :param str save_path: 保存先パス
    :return:
    """
    # 前処理
    # * Excelファイルの存在確認
    if not os.path.isfile(file_path):
        raise FileNotFoundError("file '{}' dose not exist!!".format(file_path))
    # * 保存先の設定
    if None is save_path:
        save_path = os.path.dirname(file_path)
    # * 保存先の存在確認
    if not os.path.isdir(save_path):
        raise FileNotFoundError("save path '{}' does not exist!!".format(save_path))

    # OSに適したパス表記にする。
    file_path = convert_path_compatible_with_os(file_path)
    file_name = os.path.basename(file_path)

    # xlwingsの設定
    # * Excel操作中Excelを画面に表示しない
    xw.App(visible=False)

    # ファイルオブジェクトを開く
    with xw.books.open(file_path) as book:
        # シートの存在確認
        if sheet_name not in [sheet.name for sheet in book.sheets]:
            raise NameError("Excelファイルにシート {} は存在しません".format(sheet_name))
        # シートオブジェクトを取得
        sheet = book.sheets[sheet_name]
        # 印刷範囲の設定
        set_print_area(sheet, print_area)
        # pdf化
        sheet.to_pdf(path=os.path.join(save_path, file_name) + "_" + sheet_name, show=False)


class OsType(Enum):
    AUTO = 1
    WINDOWS = 2
    LINUX = 3


def convert_path_compatible_with_os(file_path, os_type=OsType.AUTO):
    """ OSに応じたパス文字列に変換する。

    :param str file_path: ファイルパス
    :param str os_type: 処理モード
         *->OsType.AUTO: OSを自動判別し、処理を実行...
         *->OsType.WINDOWS: Windows用の処理を実行...
         *->OsType.LINUX: Linux用の処理を実行...
    :return: 変換のファイルパス
    """

    if os_type == OsType.AUTO:
        if system() == "Windows":
            return file_path.replace("/", "\\")
        if system() == "Linux":
            return file_path.replace("\\", "/")
    elif os_type == OsType.WINDOWS:
        return file_path.replace("/", "\\")
    elif os_type == OsType.LINUX:
        return file_path.replace("\\", "/")


def set_print_area(sheet, print_area):
    """印刷範囲のセッティング
    処理：印刷範囲が指定されれば、シートに設定、印刷班が指定されなければ、シートにデフォルトを設定　
    :param xlwings.book.sheet sheet: シートオブジェクト
    :param str print_area: 印刷範囲 [例) A1:C4]、Noneを指定するとExcelファイルに設定された印刷範囲を使用する。
    :return:
    """
    if print_area is None:
        print_area = sheet.page_setup.print_area
    sheet.page_setup.print_area = print_area

