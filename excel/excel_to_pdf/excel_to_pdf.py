"""
 excel_to_pdf
処理：
入力；エクセルパス名、シート名、印刷反映
出力：なし、（内側でpdfの作成）
"""
import os
from platform import system
import xlwings as xw


def main():
    file_path = os.path.abspath("book1.xlx")
    sheet_name = "Sheet1"
    excel_to_pdf(file_path, sheet_name)
    print("処理を終了します。")


def excel_to_pdf(file_path, sheet_name, print_area=None, save_path=None):
    """ エクセルファイルの特定シートをpdf化する
    処理：指定したエクセルファイルのシートを印刷する
    :param str file_path:
    :param str sheet_name:
    :param str print_area:
    :param str save_path:
    :return:
    """
    # OSに適したパス表記にする。
    file_path = convert_path_compatible_with_os(file_path)

    # Excelファイルの存在確認
    if not os.path.isfile(file_path):
        raise FileNotFoundError("file '{}' dose not exist!!".format(file_path))
    # 保存先の設定
    if None is save_path:
        save_path = os.path.dirname(file_path)
    # 保存先の存在確認
    if not os.path.isdir(save_path):
        raise FileNotFoundError("save path '{}' does not exist!!".format(save_path))

    file_name = os.path.basename(file_path)
    # xlwingsの設定
    # * Excel操作中Excelを画面に表示しない
    xw.App(visible=False)

    # ファイルを開く
    with xw.books.open(file_path) as book:
        # シートオブジェクトを取得
        sheet = book.sheets[sheet_name]
        # 印刷範囲の設定
        set_print_area(sheet, print_area)
        # pdf化
        sheet.to_pdf(path=os.path.join(save_path, file_name) + "_" + sheet_name, show=False)


def convert_path_compatible_with_os(file_path):
    if system() == "Windows":
        return file_path.replace("/", "\\")
    if system() == "Linux":
        return file_path.replace("\\", "/")


def set_print_area(sheet, print_area):
    """印刷範囲のセッティング
    処理：印刷範囲が指定されれば、シートに設定、印刷班が指定されなければ、シートにデフォルトを設定　
    :param xlwings.book.sheet sheet: シートオブジェクト
    :param str print_area: 印刷範囲文字列
    :return:
    """
    if print_area is None:
        print_area = sheet.page_setup.print_area
    sheet.page_setup.print_area = print_area


main()
