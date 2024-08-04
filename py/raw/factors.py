import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from pyecharts.charts import *
from pyecharts.options import global_options
import pyecharts.options as opts
root=os.path.abspath("../..")

df=pd.read_csv(root+'\\data\\factors\\Psychosocial_Health_Analysis.csv')
df.dropna(inplace=True)
df['problem_category'] = df['problem_category'].str.strip()
df['problem_category'] = df['problem_category'].str.lower()

pblm=dict()
for i in df.index:
    pbl=df.at[i,'problem_category']
    if pbl not in pblm:
        pblm[pbl]=1
    else:
        pblm[pbl]+=1     
new_pblm = sorted(pblm.items(),  key=lambda d: d[1], reverse=True)
 
pie = (
    Pie(init_opts=opts.InitOpts(width='1280px', height='720px'))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="焦虑抑郁患者因素分析"),
        legend_opts=opts.LegendOpts(pos_left="15%"),
    )
    .add(series_name='', data_pair=[pair for pair in new_pblm])
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
)

try:
    pie.render(root+"\\result\\factors.html")
except:
    os.mkdir(root+"\\result")
    pie.render(root+"\\result\\factors.html")