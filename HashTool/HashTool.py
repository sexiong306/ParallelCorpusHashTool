#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午4:00
# @Author  : pudgeli@tecncent.com

import argparse
import xlrd
import sys
from Utiles.Utiles import Trie
import Utiles.Utiles as Utiles


def main():
    """计算文本hash
    
    :return: 
    """
    argparser = argparse.ArgumentParser(description='calculate hash for text')
    argparser.add_argument('inputfile', help='intput file')
    argparser.add_argument('outputfile', help='outtput file')

    args = argparser.parse_args()  # Getting path from command line
    inputfile = args.inputfile
    outputfile = args.outputfile

    outputcontent = []
    for line in Utiles.readfile(inputfile):
        splitline = line.replace('\n', '').replace('\r', '').replace('\b', '').split('|||')
        if len(splitline) != 3:
            continue
        uid = splitline[0].strip()
        text_cn = splitline[1].strip().encode('utf8')
        text_other = splitline[2].strip().encode('utf8')
        text_cn = Utiles.convert2lowercase(Utiles.tradition2simple(text_cn))
        text_other = Utiles.convert2lowercase(Utiles.filterinvalidechar(text_other))
        print 'text_cn:%s,text_other:%s' % (text_cn, text_other)
        hash_cn = hash(text_cn)
        hash_other = hash(text_other)

        outputcontent.append(u'%s|||%s|||%s\n'.encode('utf8') % (uid, hash_cn, hash_other))

    Utiles.write2file(outputfile, outputcontent)


# def tempmain():
#     t1 = Utiles.currenttime()
#     orgfile = u'/Users/pudgeli/Documents/数据厨房/翻译君/zh.ko.all.zh'
#     cmpfile = u'/Users/pudgeli/Documents/数据厨房/翻译君/中韩65万.xlsx'
#     # cmpfile = u'/Users/pudgeli/Documents/数据厨房/翻译君/数-中日样例.xlsx'
#     # outputfile = u'/Users/pudgeli/Documents/数据厨房/翻译君/filter.txt'
#     result = []
#     hashtrie = Trie()
#     for line in Utiles.readfile(orgfile):
#         line = line.replace('\n', '').replace('\r', '').replace('\b', '')
#         filterline = Utiles.convert2lowercase(Utiles.filterinvalidechar(Utiles.tradition2simple(line.encode('utf8'))))
#         if not hashtrie.find(str(hash(filterline))):
#             hashtrie.add(str(hash(filterline)))
#
#     # for line in readfile(cmpfile):
#     #     line = line.replace('\n', '').replace('\r', '').replace('\b', '')
#     #     filterline = convert2lowercase(tradition2simple(line.encode('utf8')))
#     #     if not hashtrie.find(str(hash(filterline))):
#     #         hashtrie.add(str(hash(filterline)))
#     #         print line
#     #         result.append(line)
#
#     data = xlrd.open_workbook(cmpfile)
#     table = data.sheets()[0]
#     PY2 = sys.version_info.major == 2
#     for i in range(table.nrows):
#         if not isinstance(table.row_values(i)[0], str if not PY2 else basestring):
#             continue
#         before_text = table.row_values(i)[0].replace('\n', '').replace('\r', '').replace('\b', '')
#         after_text = Utiles.convert2lowercase(Utiles.filterinvalidechar(Utiles.tradition2simple(before_text.encode('utf8'))))
#         if not hashtrie.find(str(hash(after_text))):
#             print before_text
#
#     # write2file(outputfile, result)
#     print 'start time:%s,end time:%s' % (t1, Utiles.currenttime())


if __name__ == '__main__':
    main()
    # tempmain()
