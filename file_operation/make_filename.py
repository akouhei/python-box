import os


def make_filename(text_name):
    cnt = 1
    name, ext = os.path.splitext(text_name)
    suffix = ""

    while True:
        if not os.path.isfile(text_name):
            return text_name

        # ファイル名の更新
        suffix = "_(" + str(cnt) + ")"
        text_name = name + suffix + ext
        cnt += 1
