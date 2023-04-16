import argparse
import os
import subprocess
from subprocess import PIPE


def sdiff(file1, file2, is_encoding, width):
    """

    :param str file1: ファイル1
    :param str file2: ファイル2
    :param bool is_encoding: TrueであればUTF-8にエンコードしてから比較する。
    :param int width: 比較時の標準出力表示幅（sdiff -w オプション）
    :return:
    """
    # まだ完成してない。
    if not os.path.isfile(file1):
        raise Exception(f"ファイル {file1} は存在しません。")
    if not os.path.isfile(file2):
        raise Exception(f"ファイル {file2} は存在しません。")

    # 絶対パスの取得
    abs_file1 = os.path.abspath(file1)
    abs_file2 = os.path.abspath(file2)
    tmp_file1 = "/tmp/tmp_file1"
    tmp_file2 = "/tmp/tmp_file2"

    # UTF-8にエンコードしたファイルを作成
    if is_encoding:
        with open(tmp_file1, "w") as tfp1, open("/tmp/tmp_file2", "w") as tfp2:
            subprocess.run(['nkf', '-wx -Lu', file1], stdout=tfp1)
            subprocess.run(['nkf', '-wx -Lu', file2], stdout=tfp2)
        # 差分処理対象ファイルの更新
        file1 = tmp_file1
        file2 = tmp_file2

    # 差分処理結果の取得
    result = subprocess.run(['sdiff', '-w', str(width), file1, file2], stdout=PIPE)

    # 標準出力
    print("sdiff result")
    print(f"    file1 = {abs_file1}")
    print(f"    file2 = {abs_file2}")
    print("-------------------------------------------------------------------------")
    print(result.stdout.decode("UTF-8"))

    # 作事処理
    if is_encoding:
        os.remove(tmp_file1)
        os.remove(tmp_file2)

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sdiff command for Linux OS")
    parser.add_argument("file1", type=str, help="path to the first file")
    parser.add_argument("file2", type=str, help="path to the second file")
    parser.add_argument("-e", "--is_encoding", action="store_true", help="compare file after encoding to UTF-8")
    parser.add_argument("-w", "--width", type=int, default=200, help="width (sdiff -w オプション)")
    args = parser.parse_args()

    sdiff(args.file1, args.file2, args.is_encoding, args.width)
