# -*- coding: utf-8 -*-
# !/usr/bin/env python3

__author__ = "Vicentini Tommaso"
__version__ = "01.01"


import csv
import os


def main():
    """
    main
    :return: none
    """
    with open(".\\shazamlibrary.csv", "r", encoding="utf-8") as f_in:
        line = 0
        for i in f_in:
            line += 1
        f_in.close()

    with open(".\\shazamlibrary.csv", "r", encoding="utf-8") as f_in:
        skip_line = 2
        reader = csv.reader(f_in)
        for f in range(skip_line):
            next(f_in)      #salta 2 righe
        my_list = list(reader)
        lines_seen = []
        lines_duplicates = []
        with open(".\\songlist.txt", "w", encoding="utf-8") as f_out:
            for i in range(line - skip_line):
                string = my_list[i][3] + " - " + my_list[i][2]
                if string not in lines_seen:
                    f_out.write(string + "\n")
                    lines_seen.append(string)
                else:
                    pass
                    lines_duplicates.append(string)
            f_out.close()
        f_in.close()
        
        if lines_duplicates != "":
            with open(".\\songduplicates.txt", "w", encoding="utf-8") as f_duplicates:
                for i in lines_duplicates:
                    f_duplicates.write(i + "\n")
                f_duplicates.close()
    
    exit()


if __name__ == "__main__":
    main()
