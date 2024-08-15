import pandas as pd
import os
from scipy import stats
from pyecharts.charts import *
from pyecharts.options import global_options
from pyecharts import options as opts
import numpy as np
import pyecharts
print(pyecharts.__version__)

root=os.path.abspath("")

#以下模块用于处理焦虑症发病率随年龄的变化趋势
df_age = pd.read_csv(root+'\\data\\prevalence\\anxiety-disorders-prevalence-by-age.csv')
count=0
for i in df_age.columns[3:16]:
    count+=1
    df_age.rename(columns={i:'p'+str(count)},
                  inplace=True)
df_g=df_age.drop('Code',axis=1).groupby('Entity',as_index=False).mean()
dfAge=df_g[(df_g['Entity']=='China') | (df_g['Entity']=='United States')]
dfAge.set_index('Entity',inplace=True)
dfAge.drop(columns=['Year','Anxiety disorders (share of population) - Sex: Both - Age: All ages',
                    'Anxiety disorders (share of population) - Sex: Both - Age: Age-standardized'],
           axis=1,
           inplace=True)
formater="{0:.02f}".format

dfAge = dfAge.applymap(formater)

x=['5-14','15-19','19-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70+']
y1=dfAge.values[0].tolist()
y2=dfAge.values[1].tolist()

bar = Bar()
 
bar.set_global_opts(title_opts=global_options.TitleOpts(title="各年龄段焦虑发病率"))
bar.add_xaxis(x)
bar.add_yaxis("China", y1, stack="stack1")
bar.add_yaxis("United States", y2, stack="stack2")
 
try:
    bar.render(root+"\\result\\age.html")
except:
    os.mkdir(root+"\\result")
    bar.render(root+"\\result\\age.html")
    
#以下模块用于分析性别因素

df_gender=pd.read_csv(root+'\\data\\prevalence\\anxiety-disorders-prevalence-males-vs-females.csv')
df_gender.rename(columns={'Anxiety disorders (share of population) - Sex: Male - Age: All ages':'Male', 
                          'Anxiety disorders (share of population) - Sex: Female - Age: Age-standardized':'Female'},
                 inplace=True)
df_gender.head()

df_gender=df_gender.drop(columns=['Year','Population (historical estimates)','Continent','Code'],
                         axis=1)
df_gender=df_gender.groupby('Entity',
                            as_index=False).mean()
dfGen=df_gender[(df_gender['Entity']=='China') | (df_gender['Entity']=='United States')]
dfGen.set_index('Entity',
                inplace=True)

dfGen = dfGen.applymap(formater)#formater 的定义在上方

y1=dfGen['Male'].tolist()
y2=dfGen["Female"].tolist()
c = (
    Scatter()
    .add_xaxis(['China',"America"])
    .add_yaxis("Female", y2)
    .add_yaxis("Male", y1)
    
    .set_global_opts(
        title_opts=opts.TitleOpts(title="焦虑症患病率与性别的关系"),
        xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        visualmap_opts=opts.VisualMapOpts(
            type_="size",  #映射大小
            max_=8,
            min_=2,
            pos_bottom = 50,pos_right = 0)
    )
    .render(root+"\\result\\gender.html")
)

#以下模块用于处理焦虑患病率和国家gdp关系
df_gdp=pd.read_csv(root+'\\data\\prevalence\\anxiety-disorders-prevalence-vs-gdp.csv')
df_gdp.rename(columns={'Anxiety disorders (share of population) - Sex: Both - Age: Age-standardized':'Anxiety',
                       'GDP per capita, PPP (constant 2017 international $)':'GDP',
                       },inplace=True)
df_gdp.drop(columns=['Code','Population (historical estimates)','Continent'],inplace=True)
df_gdp.dropna(inplace=True)
df_gdp=df_gdp[df_gdp["Year"]==2019].drop(columns=["Year"])

#地图制作
x=df_gdp['Entity']
y=df_gdp['Anxiety']
value = list(y)
attr = list(x)
 
data = []
for index in range(len(attr)):
    city_ionfo=[attr[index],value[index]]
    data.append(city_ionfo)
 
map = (
    Map()
    .add("焦虑指数",data, "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="世界热力地图"),
        visualmap_opts=opts.VisualMapOpts(max_=df_gdp['Anxiety'].max(), 
                                          min_=df_gdp['Anxiety'].min()
                                          ),
    )
    .render(root+'\\result\\map.html')
)

#数学检验
stats.ttest_ind(df_gdp['GDP'],df_gdp['Anxiety'],equal_var=False)

# 数据准备
x = df_gdp['GDP'].tolist()
y = df_gdp['Anxiety'].tolist()

# 创建散点图
scatter = (
    Scatter()
    .add_xaxis(x)
    .add_yaxis(
        series_name="焦虑指数",
        y_axis=y,
        symbol_size=20,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="焦虑指数与GDP的关系"),
    )
    .render(root+"\\result\\gdp.html")
)