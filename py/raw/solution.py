import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import *
import os
root=os.path.abspath("")

df_fclty=pd.read_csv(root+'\\data\\solutions\\Facilities.csv')
df_human=pd.read_csv(root+'\\data\\solutions\\Human Resources.csv')

fclty_s=df_fclty.sort_values('Mental _hospitals', ascending=False)
fclty_s=fclty_s.head(10)
fclty_s2=df_fclty.sort_values('health_units', ascending=False)
fclty_s2=fclty_s2.head(10)
human_s=df_human.sort_values('Psychiatrists',ascending=False)
human_s=human_s.head(10)
human_s2=df_human.sort_values('Nurses',ascending=False)
human_s2=human_s2.head(10)

l1=fclty_s['Country'].to_list()
l2=fclty_s['Mental _hospitals'].to_list()

bar = (
    Bar()
    .add_xaxis(l1)
    .add_yaxis("精神科医院", l2, color="#ffc000")
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(title_opts=opts.TitleOpts(title="2016年各国精神科医院数量对比"))
)

l1=fclty_s2['Country'].to_list()
l2=fclty_s2['health_units'].to_list()

bar2 = (
    Bar()
    .add_xaxis(l1)
    .add_yaxis("精神医学中心", l2,color='#70ad47')
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(title_opts=opts.TitleOpts(title="2016年各国综合医院精神医学中心数量对比"))
)

l1=human_s['Country'].to_list()
l2=human_s['Psychiatrists'].to_list()

bar3 = (
    Bar()
    .add_xaxis(l1)
    .add_yaxis("精神科医生", l2,color='#ed7d31')
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(title_opts=opts.TitleOpts(title="2016年各国精神科医生数量对比"))
)

l1=human_s2['Country'].to_list()
l2=human_s2['Nurses'].to_list()

bar4 = (
    Bar()
    .add_xaxis(l1)
    .add_yaxis("精神科护士", l2,color='#5b9bd5')
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(title_opts=opts.TitleOpts(title="2016年各国精神科护士数量对比"))
)

tab = Tab()
tab.add(bar, "精神医院")
tab.add(bar2, "精神医学中心")
tab.add(bar3, "精神科医生")
tab.add(bar4, "护士")
try:
    tab.render(root+"\\result\\solution.html")
except:
    os.mkdir(root+"\\result")
    tab.render(root+"\\result\\solution.html")