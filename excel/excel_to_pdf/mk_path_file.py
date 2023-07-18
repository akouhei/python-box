import pandas as pd


def mk_sample_config_file(config_file_name="Excel_to_PDF.conf", encoding="UTF-8"):
    # configファイル作成
    data = {
        "filepath": ["./sample.xlsx", "./sample2.xlsx"],
        "sheet_name": ["Sheet1", "Sheet2"],
        "print_area": ["None", "A1:G20"]
    }
    df = pd.DataFrame(data)
    df.to_csv(config_file_name, encoding=encoding, index=False)


mk_sample_config_file()

