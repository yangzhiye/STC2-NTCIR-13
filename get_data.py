# -*- coding: utf-8 -*-
#import jieba
import thulac
import re


def cut_word(filepath):

    def _remove_special_char(m):
        s = m.group(0)
        if s in u'，。！？“”《》':
            return s
        return ''

    thu_cut = thulac.thulac("-seg_only")
    f = open(filepath)
    for line in f.readlines():
        content = line.split("\t")[-1].decode('utf-8')
        content = re.sub(u'[\(\[（#「【《].*[\)\]）#」】》]', '', content)
        content = re.sub(u'[^\u4e00-\u9fa50-9a-zA-Z]', _remove_special_char, content).encode('utf-8')
        if(len(content) > 0):
            print " ".join(thu_cut.cut(content))
        # result = jieba.cut(result)
        # print ' '.join(result)


if __name__ == "__main__":

    filepath = "./data/repository/stc2-repos-id-post"
    #filepath = "./data/repository/stc2-repos-id-cmnt"
    cut_word(filepath)

