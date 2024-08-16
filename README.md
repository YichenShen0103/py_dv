# Python数据分析及可视化项目

## 关于本项目
本项目是基于Python数据分析及可视化的研究项目，主要研究焦虑症、抑郁症、压力焦虑等相关问题。

本项目为笔者2024春季学期Python基础与应用及数据可视化课程结课作业。

## 目录结构
- data：用于存放数据处理及可视化项目的原数据文件
    - 本目录下共四个子路径，分别存放四组不同的数据集。
    - 数据来源：
        - 焦虑症患病率数据集：https://www.kaggle.com/datasets/jaffidantonio/prevalence-of-anxiety-disorders-1990-to-2019?resource=download
        - 学生焦虑抑郁聊天记录数据集：https://www.kaggle.com/datasets/sahasourav17/students-anxiety-and-depression-dataset
        - 影响精神健康的因素数据集：https://www.kaggle.com/datasets/mdismielhossenabir/psychosocial-mental-health-analysis
        - 关于心理健康问题防治措施和解决方案的数据集：https://www.kaggle.com/datasets/twinkle0705/mental-health-and-suicide-rates
- py：用于存放数据处理及可视化所用的代码文件
    - 本目录下共两个子目录，分别用于存放python源文件和jupyter notebook文件。
    - ⚠注意：本项目使用的pyecharts的版本为1.8.1，请确保安装正确版本。
- main：用于存放可视化结果文档及数据分析报告文件。
- front_end：用于存放前端页面文件，包括前端页面所用的各种静态资源文件。
    - 本目录下有若干子目录，分别存放前端页面所需的html、css、js、图片、字体等静态资源文件。

## 运行和使用说明
确保安装git和其他必要运行环境的情况下，使用命令：

    git clone https://github.com/YichenShen0103/py_dv.git

并运行py目录下的所有python源文件或jupyter notebook文件（任选其一）即可。

运行结果位于自动生成的/result路径中，不会覆盖/main中的示例文件。

运行前端页面的方式可以有两种：
- 确保front_end目录完整的情况下使用vscode编辑器的live server插件运行index.html；
- 直接访问：https://yichenshen0103.github.io/py_dv/front_end/#
  
⚠警告：

- 本项目建议运行在windows系统下的anaconda环境中，并确保安装了pandas、numpy、matplotlib、pyecharts、jupyter notebook、wordcloud、nltk、textblob等运行环境。
- 经过测试，前端页面在macOS Sonoma，Windows 10/11下的chrome、firefox、edge、safari等主流浏览器中均可正常运行。其他系统和浏-览器可能存在兼容性问题。
- 请勿直接打开index.html，避免加载和显示问题。
- 前端页面部署在github pages上，建议使用VPN，否则可能存在延迟或访问不稳定问题。
- 本项目仅供学习交流使用，请勿用于商业用途。

## 声明
本项目自2024年8月20日起停止更新。