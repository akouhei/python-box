"""
学習用：xlwingsの基礎
title : 【図解！】xlwingsの使い方 | pythonでExcelを操作①アクティブブックの操作編
url : https://www.yutaka-note.com/entry/xlwings_active
yrl : Sheets : https://www.yutaka-note.com/entry/xlwings_sheet#%E4%BD%BF%E7%94%A8%E4%B8%AD%E3%81%AE%E3%82%BB%E3%83%AB%E7%AF%84%E5%9B%B2%E3%81%AE%E5%8F%96%E5%BE%97shtused_range
"""

import xlwings as xw


def main():
    book_test()
    sheet_test()
    cell_test()


def book_test():
    # 既存ブックの読み込み
    wb = xw.Book("book1.xlsx")
    # 既存ブックの読み込み2
    with xw.Book("book2.xlsx") as wb2:
        # 現在開いているbookを取得
        print("xw.books = ", xw.books)
        # アクティブ状態のブックを確認。
        print("xw.books.active.name = ", xw.books.active.name)
        # ブック名を取得
        print("wb.name = ", wb.name)
        # ブックをアクティブにする。
        wb.activate()
    # ブックを指定して変数化
    wb_test = xw.books["book1.xlsx"]
    print(wb_test)
    # ブックの保存
    wb.save()
    # 名前を付けて保存
    wb.save("book3.xlsx")
    # ブックを閉じる
    wb.close()


def sheet_test():
    with xw.Book("book1.xlsx") as wb:
        # シートの追加
        wb.sheets.add()
        # シートの一覧を確認
        print("wb.sheets = ", wb.sheets)
        # アクティブシートの確認
        print("wb.sheets.active = ", wb.sheets.active)
        # シートを指定
        sht_test = wb.sheets["sheet1"]
        print("wb.sheets['Sheet1'] = ", sht_test)
        # シートを指定
        sht_test = wb.sheets[0]
        print("wb.sheets[0] = ", sht_test)

        wb.save()


def cell_test():
    with xw.Book("book3.xlsx") as wb:
        # データの書き込み
        sht = wb.sheets.active
        # 行列を書き込み
        sht.range("A1").value = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
        # 保存
        wb.save()

    with xw.Book("book3.xlsx") as wb:
        # シート選択
        sht = wb.sheets.active
        # 選択を行方向拡張
        print('sht.range("A1").expand("right").value', sht.range("A1").expand("right").value)
        # 選択を列方向拡張
        print('sht.range("A1").expand("down").value', sht.range("A1").expand("down").value)
        # 選択をテーブル拡張
        print('sht.range("A1").expand("table").value', sht.range("A1").expand("table").value)


main()
