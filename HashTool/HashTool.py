#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午4:00
# @Author  : pudgeli@tecncent.com

import mmh3
import io
from langconv import *
import re
import argparse

invalidpattern = '[\s+\.\!\/_,$%^*()+\"\']+|[+——！，。？、~@#￥%……&*（）].*?'

def readfile(inputfile):
    """read file
    
    读取文件
    
    :param inputfile: 输入文件 
    :return: 读取内容
    """
    with io.open(inputfile, 'r', encoding='utf8') as f:
        for line in f:
            yield line


def write2file(outputfile, content):
    """wtire result to file.
    写入文件
    
    :param outputfile: 输出文件
    :param content: 输出内容
    :return: 返回
    """
    with open(outputfile, "w") as f:
        f.writelines([u''.join(line + '\n').encode('utf8') for line in content])


def filterinvalidechar(text):
    """filterinvalidechar
    
    过滤特殊字符
    
    :return: 
    """
    return re.sub(invalidpattern.decode('utf8'), '', text)


def convert2lowercase(text):
    return text.lower()


def hash(key):
    """calculate hash
    
    计算hash
    
    :param key: 文本 
    :return: 64位算法hash
    """
    hash_64, hash_128 = mmh3.hash64(key)
    return hash_64


def tradition2simple(line):
    """tradition2simple
    
    繁体转换为简体
    :param line: 繁体文本
    :return: 简体文本
    """
    # 将繁体转换成简体
    line = Converter('zh-hans').convert(line.decode('utf-8'))
    line = line.encode('utf-8')
    return line


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('inputfile', help='intput file')
    argparser.add_argument('outputfile', help='outtput file')

    args = argparser.parse_args()  # Getting path from command line
    inputfile = args.inputfile
    outputfile = args.outputfile

    outputcontent = []
    for line in readfile(inputfile):
        splitline = line.replace('\n', '').split('|||')
        if len(splitline) != 3:
            continue
        uid = splitline[0].strip()
        text_cn = splitline[1].strip().encode('utf8')
        text_other = splitline[2].strip().encode('utf8')
        text_cn = convert2lowercase(filterinvalidechar(tradition2simple(text_cn)))
        text_other = convert2lowercase(filterinvalidechar(text_other))
        print 'text_cn:%s,text_other:%s' % (text_cn, text_other)
        hash_cn = hash(text_cn)
        hash_other = hash(text_other)

        outputcontent.append(u'%s|||%s|||%s'.encode('utf8') % (uid, hash_cn, hash_other))

    write2file(outputfile, outputcontent)


if __name__ == '__main__':
    main()
    # print convert2lowercase('你好 QWE asdfsd')