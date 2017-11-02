#!/usr/bin/python
#-*-coding:utf-8 -*-
import Levenshtein
import pandas as pd
import jieba
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def cos(vector1,vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a,b in zip(vector1,vector2):
        dot_product += a*b
        normA += a**2
        normB += b**2
    if normA == 0.0 or normB==0.0:
        return None
    else:
        return dot_product / ((normA*normB)**0.5)

path="../tecent/test_data"
tname=['Id','comment']
data=pd.read_table(path,sep="	",header=None,names=tname)
commentline=[]
for i in data.comment:
    commentline.append(i)
corpus=[]
#print data
# print data.comment
print len(commentline)
for i in range(len(commentline)):
     seg_line=jieba.cut(commentline[i],cut_all=True)
     corpus.append(" ".join(seg_line))
# for i in corpus:
#     print i
# print data.comment[0]
# print len(data.comment[0])
# print type(corpus[1])
# print corpus[0]
vectorizer=CountVectorizer()
#X=vectorizer.fit_transform(corpus)
#print X.toarray()

transformer=TfidfTransformer()
tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))
featurelist=vectorizer.get_feature_names()
print type(featurelist)
weightarray=tfidf.toarray()
print weightarray.shape
print weightarray
#print featurelist
# # for i in range(len(featurelist)):
#     print featurelist[i]

# for i in range(len(weightarray)):
#     print("第%s段文本的词语ti-idf权重"%i)
#     for j in range(len(featurelist)):
#         print (featurelist[j],weightarray[i][j])

dic={}
for i in range(len(commentline)):
    for j in range(i+1,len(commentline)):
        key=str(i)+":"+str(j)
        d_levenshtein=Levenshtein.distance(commentline[i],commentline[j])
        d_cos=cos(weightarray[i],weightarray[j])
        if d_cos!=None and d_cos!=0:
            dic[key]=d_levenshtein/d_cos
sorted_dic=sorted(dic.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
index=sorted_dic[0][0].split(":")
print "这两段话可以作为一个句子改写的平行语料:"
for i in index:
    print "%s    %s"%(data.Id[int(i)],commentline[int(i)])