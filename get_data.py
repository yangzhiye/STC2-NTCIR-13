# -*- coding: utf-8 -*-
__author__ = 'vino'

import jieba

def cut_word(filepath):
    f = open(filepath)
    for line in f.readlines():
        result = line.split("\t")[-1]
        result = jieba.cut(result)
        print ' '.join(result)


if __name__ == "__main__":

    filepath = "./data/repository/stc2-repos-id-post"
    cut_word(filepath)