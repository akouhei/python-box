import argparse
import os
import subprocess
from subprocess import PIPE
import codecs


def sdiff(file1, file2, is_encoding=True):
    # まだ完成してない。
    if not os.path.isfile(file1):
        print(f"ファイル {file1} は存在しません。")
        exit(1)
    if not os.path.isfile(file2):
        print(f"ファイル {file2} は存在しません。")
        exit(2)

    file1 = os.path.abspath(file1)
    file2 = os.path.abspath(file2)

    if is_encoding:
        with open("/tmp/tmp_file1", "w") as tmp_file1, open("/tmp/tmp_file2", "w") as tmp_file2:
            subprocess.run(['nkf', '-wx -Lu', file1], stdout=tmp_file1)
            subprocess.run(['nkf', '-wx -Lu', file2], stdout=tmp_file2)

    print(f"sdiff {file1} vs {file2}")

    result = subprocess.run(['sdiff', '-w', '200', "/tmp/tmp_file1", "/tmp/tmp_file2"], stdout=PIPE)
    print(result.stdout.decode("UTF-8"))

    subprocess.run(['rm', '-f', "/tmp/tmp_file1", "/tmp/tmp_file2"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sdiff command for Linux OS")
    parser.add_argument("file1", type=str, help="path to the first file")
    parser.add_argument("file2", type=str, help="path to the second file")
    parser.add_argument("--encoding", type=str, help="compare file after encoding to UTF-8")
    args = parser.parse_args()

    sdiff(args.file1, args.file2)
