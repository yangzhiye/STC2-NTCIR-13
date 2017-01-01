# -*- coding: utf-8 -*-
#import jieba
import thulac
import re


def get_new_filename(filepath):
    if filepath.split('-')[-1] == "post":
        return "./data/repository/data_clean_post.txt"
    else:
        return "./data/repository/data_clean_cmnt.txt"


def cut_word(filepath):

    def _remove_special_char(m):
        s = m.group(0)
        if s in u'，。！？“”《》':
            return s
        return ''

    thu_cut = thulac.thulac("-seg_only")
    f_old = open(filepath)
    f_new = open(get_new_filename(filepath),"w+")
    for i,line in enumerate(f_old.readlines()):
        id = line.split("\t")[0]
        content = line.split("\t")[-1].decode('utf-8')
        content = re.sub(u'[\(\[（#「【《].*[\)\]）#」】》]', '', content)
        content = re.sub(u'[^\u4e00-\u9fa50-9a-zA-Z]', _remove_special_char, content).encode('utf-8')
        if(len(content) > 0):
            content = " ".join(thu_cut.cut(content)).strip()
            # result = jieba.cut(result)
            # print ' '.join(result)
        f_new.write(id+"\t"+content+"\n")
        if(i%10000==0):
            print " %d content write to file ok ! " % i
    f_new.close()


def get_clean_data():
    filepath_list = ["./data/repository/stc2-repos-id-post",
                     "./data/repository/stc2-repos-id-cmnt"]
    for filepath in filepath_list:
        cut_word(filepath)


if __name__ == "__main__":
   get_clean_data()