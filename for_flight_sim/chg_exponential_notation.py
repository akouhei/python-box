from decimal import Decimal, ROUND_HALF_UP
import re


def chg_exponential_notation(num, dec_format="0.0000001"):
    """
    見切れた数値を正確に四捨五入したうえで、指数表記文字列を返却する。
    :param num: 数値もしくは数値文字列
    :param dec_format: 小数点の表示形式
    :return: 指数表記文字列
    """

    # 数字判定
    if not is_decimal(num):
        return None

    # 変数定義
    str_num = str(num)
    dec_num = Decimal(num)

    # 符号と数字に分離する。
    signal, str_num = (str_num[0], str_num[1:]) if str_num[0] == "-" else ("", str_num)
    # 桁数を取得(len(format)の理由 => 表示したい桁よりも大きい桁を設定する必要がある。)
    exp = f"{dec_num:.{len(dec_format)}E}".split('E')[1]
    # 小数点の位置を取得
    point_index = str_num.find(".")

    # 数字の桁 修正
    if point_index == -1:
        # 整数の場合
        str_num = str_num[:1] + "." + str_num[1:]
    else:
        # 小数点を含む場合
        tmp = str_num.replace(".", "")
        str_num = (tmp[:(point_index - int(exp))] + "." + tmp[(point_index - int(exp)):]).lstrip("0")

    # 指定桁で四捨五入処理
    str_num = str(Decimal(str_num).quantize(Decimal(dec_format), rounding=ROUND_HALF_UP))

    # 1.2353476E-04 の形式で返却
    return f"{signal}{str_num}E" + ('+' if int(exp) >= 0 else '-') + f"{abs(int(exp)):0>2}"


def is_decimal(num):
    """
    数字であることを判定する（小数点、整数であればTrueを返す）
    :param num:
    :return: True or False
    """
    str_num = str(num).lstrip("-")
    pattern = re.compile(r'^\d+(\.\d+)?$')
    # 一致 => MatchObject, 不一致 => None
    return bool(pattern.match(str_num))


main()

# 文字列が数値かどうか
# https://science-log.com/python%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0tips%E9%9B%86/%E3%80%90python%E3%80%91%E6%96%87%E5%AD%97%E5%88%97%E3%81%8C%E6%95%B0%E5%80%A4%E3%81%8B%E3%81%A9%E3%81%86%E3%81%8B%E5%88%A4%E5%AE%9A%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/

# int float関数の定義
# https://gammasoft.jp/support/python-error-str-convert-to-int/