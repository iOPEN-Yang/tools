# tools

## News
+ [2021/09/12] add test1.py. 将result文件夹中的txt文件名称读取到 txt_name 文件夹下的 name.txt.
+ [2021/09/17] add test2.py. 实现最小二乘法
+ [2021/09/17] add test3.py. 读取source_folder文件夹下所有suffix后缀的文件名称，
  将名称以及路径读取到dis_floder文件夹下的txt_name文件中。
+ [2021/09/18] add test3.py. 从命令行获取参数，调用test3.py
  
## Introduction
There are some tools in this project.

## Quick start 
### Installation
1. install pytorch >= v1.4.0 following [official instruction](https://pytorch.org/).
    >- **tested with pytorch v1.9.0**

2. install dependencies:
    >```
    >pip install -r requirements.txt
    >```

3. Testing  

    > For test1.py:  
    >```
    >python test1.py
    >```
    >For test2.py:
    >```
    >python test2.py
    >```
    >For test3.py:
    >```
    >python test3.py
    >```
    >For test4.py
    >```commandline
    >python test4.py 
    >```
    >For test4.py, if you want to specify your own path, use
    >```commandline
    >python test4.py \
    >--source_folder result \
    >--dis_folder  txt_name \
    >--txt_name name.txt \
    >--suffix txt
    >```
创建脚注格式 [test].  
[test]: http://www.baidu.com