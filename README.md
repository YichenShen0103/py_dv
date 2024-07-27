# py_assignment

## 关于本项目
本项目是基于Python数据分析及可视化的研究项目，主要研究焦虑症、抑郁症、压力焦虑等相关问题。

本项目为笔者2024春季学期Python基础与应用课程结课作业。

## 目录结构
- data：用于存放数据处理及可视化项目的原数据文件
    - 本目录下共三个子路径，分别存放焦虑症患病率、学生焦虑抑郁群体的聊天记录、焦虑患者压力量表数据。
    - 数据来源：
        - 焦虑症患病率数据集：https://www.kaggle.com/datasets/jaffidantonio/prevalence-of-anxiety-disorders-1990-to-2019?resource=download
        - 学生焦虑抑郁聊天记录数据集：https://www.kaggle.com/datasets/sahasourav17/students-anxiety-and-depression-dataset
        - 焦虑患者压力量表数据集：https://www.kaggle.com/datasets/josephwillard/anxiety-stress-test-data
- py：用于存放数据处理及可视化所用的代码文件
    - 本目录下共两个子目录，分别用于存放python源文件和jupyter notebook文件。
    - 运行环境要求：
        - python 3.x
        - pandas 
        - numpy 
        - matplotlib 
        - pyecharts 
        - jupyter notebook 
        - wordcloud
- main：用于存放可视化结果文档及数据分析报告文件

## 运行和使用说明
确保安装git和其他必要运行环境的情况下，使用命令：

``git clone https://github.com/YichenShen0103/py_assignment.git``

并运行py目录下的所有python源文件和jupyter notebook文件即可。

运行结果位于自动生成的/result路径中，不会覆盖/main中的示例文件。

注意：本项目建议运行在windows系统下的anaconda环境中，并确保安装了pandas、numpy、matplotlib、pyecharts、jupyter notebook、wordcloud等运行环境。

## 声明
本项目自2024年8月20日起停止更新。