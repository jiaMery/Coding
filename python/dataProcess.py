#!/usr/bin/python
#-*-coding:utf-8 -*-
import socket
import struct
import pandas as pd
path="access.log"
name=["IP","URL","unix_timestamps"]
df=pd.read_table(path,sep="\t",header=None,names=name)
url_index=list(set(df["URL"]))
print "all URL in access.log:"
print url_index
hot=pd.DataFrame(columns=["Hot_IP"],index=url_index)
print df
hot["Hot_IP"]=0
for i in df["URL"]:
    if i in hot.index:
        hot.loc[i,"Hot_IP"]+=1
hot=hot.sort_values("Hot_IP",ascending=False)
print "统计该日志中所有URL的热度，并按热度降序输出TOP 5:"
print hot.ix[:5]
time_hot=df[df["unix_timestamps"]>1508439600]
time_hot=time_hot[time_hot["unix_timestamps"]<1508448600]
print time_hot
time_hot_df=pd.DataFrame(columns=["time_hot_total"],index=url_index)
time_hot_df["time_hot_total"]=0
for i in time_hot["URL"]:
    if i in time_hot_df.index:
        time_hot_df.loc[i,"time_hot_total"]+=1
time_hot_df=time_hot_df.sort_values("time_hot_total",ascending=False)
print "今天凌晨3点至凌晨5点30分期间内，用户访问最频繁的5个URL:"
print time_hot_df[:5]

for i in range(len(df)):
    df.ix[i,"IP"]=struct.unpack("!L",socket.inet_aton(df.ix[i,"IP"]))[0]
print "把点分格式字符串表示的IP地址转换成其整数表示:"
print df