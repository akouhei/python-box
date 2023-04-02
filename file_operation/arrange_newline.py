import argparse
from make_filename import make_filename


def main(filepath, keyword, rows_per_page):
    rows = 0
    ans_lines = []

    with open(filepath, "r", encoding="UTF-8") as file:
        lines = file.readlines()

    for line in lines:
        rows += 1
        ans_lines.append(line)

        if keyword in line:
            ans_lines.extend(["\n"]*(rows_per_page - rows))
            # 次のページ
            rows = 0

        if rows >= rows_per_page:
            # 次のページ
            rows = 0

    output_filename = make_filename("output.txt")

    with open(output_filename, "w", encoding="UTF-8") as file:
        file.writelines(ans_lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="replace string in files")
    parser.add_argument("filepath", type=str, help="file path")
    parser.add_argument("keyword", type=str, help="keyword")
    parser.add_argument("-n", "--lines_per_page", type=int, default=20, help="lines per page")

    args = parser.parse_args()

    main(args.filepath, args.keyword, args.lines_per_page)
