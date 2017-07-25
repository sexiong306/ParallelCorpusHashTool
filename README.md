# ParallelCorpusHashTool
ParallelCorpusHashTool用于对数据预处理，主要包括去重，计算hash等

##	安装
安装前先安装好python运行环境(python 2.7)

```
	git clone https://github.com/sexiong306/ParallelCorpusHashTool.git
	cd ParallelCorpusHashTool
	python setup.py install
```

##	使用
###	HashTool使用
用于计算双语文本的murmurhash。
文本必须为utf8编码，格式要求：

```
	uid|||中文文本|||翻译文本
```
例如：

```
	123|||那你说该怎么办啊|||どうしろってんだ
```
使用方法：

```
	python -m HashTool inputfile outfile
```
###	DataFilterTool使用
用于对文本去重。
文本必须为utf8编码，格式要求:

```
	中文
```
例如：

```
	你好啊，这是一个test
```
使用方法：

```
	python -m DataFilterTool inputfile outfile
```
