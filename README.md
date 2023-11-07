# 【Bilibili每周必看】数据分析

## 项目介绍

本项目可以自动抓取Bilibili每周必看的视频相关数据，以json格式保存在本地，并提取其中的感兴趣的信息，存储为csv格式。  
对抓取到的数据，通过使用Tableau对其中的一些字段进行数据可视化分析。（暂未完成）  

### Update
| 日期              | 版本   | 更新说明            |
|-----------------|------|-----------------|
| 2023-11-07 Tue. | V1.0 | 完成数据抓取阶段和数据处理阶段 |

### Todo
数据分析阶段，使用Tableau绘制数据分析图表。  

## 开发环境

- Python 3.9.18 (Anaconda 3)
- PyCharm 2023.2.3 (Profession Edition)
- Tableau Desktop Public Edition 2023.3.0

## 如何运行该项目

### 项目结构

```text
BilibiliPopular
├── README.md
├── __pycache__
├── crawler
│   ├── __pycache__
│   │   └── config.cpython-39.pyc
│   ├── config.py
│   └── crawl.py
├── data_processing
│   ├── __pycache__
│   │   └── config.cpython-39.pyc
│   ├── config.py
│   └── data_process.py
├── processed_data
│   └── bilibili_popular_data.csv
├── raw_data
│   ├── week_1.json
│   ├── week_2.json
│   ├── week_3.json
│   └── ...
└── requirements.txt
```

### 运行前准备

首先，请确保您已在您的计算机上安装[Anaconda 3](https://www.anaconda.com/download)。  
您可以通过以下命令来创建一个Conda虚拟环境并进入该环境。其中`crawl`是您所创建的虚拟环境的名称，您也可以根据自己的喜好更改它。 

```commandline
conda create -n crawl python=3.9
conda activate crawl
```

接下来，您可以通过以下命令来安装本项目依赖的模块。  

```commandline
pip install -r requirements.txt
```

| 模块名称           | 版本     | 用途                        |
|----------------|--------|---------------------------|
| fake_useragent | 1.3.0  | 发送请求时随机使用一个User-Agent     |
| requests       | 2.31.0 | 向待抓取数据发送请求并返回响应           |
| retrying       | 1.3.4  | 确保每一次数据抓取只有成功运行后才能进行下一步操作 |
| pandas         | 2.1.2  | 对json和csv进行操作             |

依赖模块安装完毕，进入项目所在的目录。请将以下命令中的`/path/to/project`更改为您的项目路径。  

```commandline
cd /path/to/project
```

### 数据抓取阶段

进入`crawler`目录，运行`crawl.py`。抓取到的数据为json格式，将会保存在项目根目录下的`raw_data`目录下，以`week_<num>.json`命名，其中`num`为【每周必看】的期数。  
您可以根据自己的需求更改`config.py`的`NUM`值，以抓取您所需要的数据。  

```commandline
cd crawler
python crawl.py
```

### 数据处理阶段

进入`data_processing`目录，运行`data_process.py`。处理后的数据为csv格式，将会保存在项目根目录下的`processed_data`目录下，以`bilibili_popular_data.csv`命名。  

```commandline
cd ../data_processing
python data_process.py
```

### 数据分析阶段

使用Tableau进行数据分析。  
Todo...  

## 写在最后

本项目较为简单，仅为个人学习Tableau过程中获取数据使用。  
如果您对本项目有任何意见或建议，欢迎联系我！  
Email: <1398635912@qq.com> or <cch_personal@163.com>  