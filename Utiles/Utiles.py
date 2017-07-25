#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 下午2:42
# @Author  : pudgeli@tecncent.com

import mmh3
import io
from langconv import *
import re
import time

TIMEFORMATE = '%Y-%m-%d %X'
invalidpattern = '[\s+\.\!\/_,$%^*()+\"\']+|[+——！，。？、~@#￥%……&*（） ].*?'

def currenttime():
    return time.strftime(TIMEFORMATE, time.localtime())


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
        f.writelines([u''.join(line).encode('utf8') for line in content])


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


class Trie:
    root = {}
    END = '/'

    def add(self, word):
        # 从根节点遍历单词,char by char,如果不存在则新增,最后加上一个单词结束标志
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.END] = None

    def find(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.END in node