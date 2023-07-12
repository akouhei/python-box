import os
import numpy as np


def main():
    print("create temporary covariance matrix.py")
    lines = []
    maxtime = 100
    maxline_in_section = 7
    covariance_file_name = "covariance_matrix.txt"

    with open("covariance_matrix.txt", mode="w") as f:
        for t in range(0, maxtime):
            f.write("  {:<1.10e}  {:<1.10e}  {:<1.10e}  {:<1.10e}\n".format(t, np.random.rand(), np.random.rand(),
                                                                            np.random.rand()))
            f.write("  {}  {:<1.10e}  {:<1.10e}  {:<1.10e}\n".format(" " * 16, np.random.rand(), np.random.rand(),
                                                                     np.random.rand()))
            randoms = [[np.random.rand() for m in range(0, 6)] for n in range(0, 6)]
            for l in range(0, maxline_in_section - 1):
                f.write("  {:<1.10e}  {:<1.10e}  {:<1.10e}  {:<1.10e}\n".format(l + 1, randoms[l][0], randoms[l][1],
                                                                                randoms[l][2]))
                f.write("  {}  {:<1.10e}  {:<1.10e}  {:<1.10e}\n".format(" " * 16, randoms[l][3], randoms[l][4],
                                                                         randoms[l][5]))


main()
