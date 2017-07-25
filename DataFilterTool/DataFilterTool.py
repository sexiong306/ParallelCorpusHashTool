#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 下午2:42
# @Author  : pudgeli@tecncent.com

from Utiles.Utiles import Trie
import Utiles.Utiles as Utiles
import argparse


def main():
    """文本去重
    
    :return: 
    """
    argparser = argparse.ArgumentParser(description='filter duplicated text')
    argparser.add_argument('inputfile', help='intput file')
    argparser.add_argument('outputfile', help='outtput file')
    args = argparser.parse_args()  # Getting path from command line
    inputfile = args.inputfile
    outputfile = args.outputfile

    outputcontent = []

    hashTrie = Trie()
    for line in Utiles.readfile(inputfile):
        text_org = line.replace('\n', '').replace('\r', '').replace('\b', '').strip().encode('utf8')
        text_dest = Utiles.convert2lowercase(Utiles.tradition2simple(text_org))
        print 'text_dest:%s' % text_dest
        hash_org = hash(text_dest)
        if not hashTrie.find(str(hash_org)):
            hashTrie.add(str(hash_org))
            outputcontent.append(u'%s\n'.encode('utf8') % text_dest.decode('utf8'))

    Utiles.write2file(outputfile, outputcontent)

if __name__ == '__main__':
    print 'test'