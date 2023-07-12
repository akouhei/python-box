import argparse
import os
import re


def main():
    repfile = RepFile(path="result.rep")
    #for dic in repfile.dicts:
    #    for line in dic["optimized"]:
    #        print(line, end="")
    #    print("----------------")



class RepFile:
    def __init__(self, path):
        self.path = path
        self.lines = []
        self.dicts = []
        self.__KEYWORD_INDEPENDENT = " *** Independent Variable"
        self.__KEYWORD_DEPENDENT = " *** Dependent Variable"
        self.__KEYWORD_OPTIMIZED = " *** Optimized Variable"
        self.__ENCODING = "UTF-8"
        self.__set_lines()
        self.__set_dicts()

    def __set_lines(self):
        with open(self.path, mode="r", encoding=self.__ENCODING) as file:
            self.lines = file.readlines()

    def __set_dicts(self):
        # lines を捜索、# keyword～改行行までを一区切りとし、keywordごとにdictに登録
        # independ, depend, optの順に取得できるはず、取得できない場合は、無視し、N回目の読み込みに失敗した旨を報告
        # satisfiedしたか否かを判断し、dictsの項目の一つとして True or Falseで格納しておくと良いと思われる。
        # 行数も登録しておくと便利かも
        is_independent_line = False
        is_dependent_line = False
        is_optimized_line = False
        judgement_record_of_section = [is_independent_line, is_dependent_line, is_optimized_line]
        SKIP_NUM_OF_ROW = 3

        section_dict = {"independent": [], "dependent": [], "optimized": [], "satisfied": False, "count": 1}
        section_count = 0

        for line in self.lines:
            # 対象のセクションの開始判定
            if self.__KEYWORD_INDEPENDENT in line:
                is_independent_line = True
                judgement_record_of_section[0] = is_independent_line
            if self.__KEYWORD_DEPENDENT in line:
                is_dependent_line = True
                judgement_record_of_section[1] = is_dependent_line
            if self.__KEYWORD_OPTIMIZED in line:
                is_optimized_line = True
                judgement_record_of_section[2] = is_optimized_line

            # 対象のセクションの行でない場合、次の行へスキップ
            if not any(judgement_record_of_section):
                continue

            # 対象のセクションの終了判定
            if line.startswith("\n"):
                is_independent_line = False
                is_dependent_line = False
                is_optimized_line = False

            # セクション用の辞書へ、行の追加処理
            if is_independent_line:
                section_dict["independent"].append(line)
            if is_dependent_line:
                section_dict["dependent"].append(line)
            if is_optimized_line:
                section_dict["optimized"].append(line)

            # 対象のセクションの終了処理
            if all(judgement_record_of_section) and line.startswith("\n"):
                # セクション判定の初期化
                judgement_record_of_section = [False, False, False]
                # セクションのカウント
                section_count += 1
                section_dict["count"] = section_count
                # 制約を満足したか確認
                for i, l in enumerate(section_dict["dependent"]):
                    if i <= SKIP_NUM_OF_ROW:
                        continue
                self.__analysis_text(section_dict["dependent"][1:])

                # セクションをリストに登録
                self.dicts.append(section_dict)
                section_dict = {"independent": [], "dependent": [], "optimized": [], "satisfied": False, "count": 1}

    def __analysis_text(self, lines):
        blank_indexes = []
        for line in lines:
            # ワンセクションであること（リストに間に改行がないこと前提）
            if "\n" == line:
                print("改行だけの行が存在します。正常に動作しない可能性があります。")
            # ハイフンと空白だけの行を探す(個数は適当に大きい数に設定)
            if re.match("^[ -]{20,21}", line):
                print(line)
                # 空白文字の場所を保存
                for i, c in enumerate(line):
                    if c == " ":
                        blank_indexes.append(i)
                blank_indexes.append(len(line) + 1)

        for line in lines:
            var = self.__extract_string(line, blank_indexes)
            print(var)

    def __extract_string(self, line, blank_indexes):
        var = []
        for i in range(len(blank_indexes) - 1):
            s = blank_indexes[i] + 1
            e = blank_indexes[i+1] - 1
            var.append(line[s:e].strip())
        return var








    def printall(self):
        # 登録した情報をすべて表示, __str__とかで表現してもいいかも
        print("")

    def printsatisfied(self):
        # 制約を満たして物だけすべて表示, true, falseで、(only satisfied)の判断
        print("")

    def get_max(self):
        # 最大Optimizeを取り出し、文字列を返却
        # →最大Optimizeが何番目のdictに入っているか取得する関数必要
        print("")

# 以下はこのクラスで実現しなくてもよい
#  define Qxxx 1.30530495e+04の形でprintできるようにする。
#  alma input のdefine差し替え
#  何をしたのかコメントを残せる機能を追加してもよいかも？

main()