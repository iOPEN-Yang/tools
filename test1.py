# 将result文件夹中的文件名称写到./txt_name/name.txt中
import os

def getFilePathList(path, filetype):
    pathList = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(filetype):
                pathList.append(os.path.join(root, file))
    return pathList  # 输出以filetype为后缀的列表

# 获取当前路径
basedir = os.path.abspath(os.path.dirname(__file__))

# 设置txt的名字
txt_name = 'name.txt'

# 设置要保存的路径
# in windows
txt_path = basedir + '\\txt_name'
if not os.path.exists(txt_path):
    os.makedirs(txt_path)
# # in Linux
# txt_path = basedir + '/txt_name'
# if not os.path.exists(txt_path):
#     os.makedirs(txt_path)

# 提取result文件夹中以txt为后缀的文件名称
resdir = basedir + '\\result'
print(resdir)
temps = getFilePathList(resdir, 'txt')
txt_file = []
for temp in temps:
    txt_file.append(temp.split('\\')[-1])
print(txt_file)

# 保存到name.txt中
# in windows
txt_abspath = txt_path + '\\' + txt_name
# # in Linux
# txt_abspath = txt_path + '/' + txt_name
fp = open(txt_abspath, 'w')
for i in range(len(txt_file)):
    print(txt_file[i] + "\n")
    fp.write(txt_file[i] + "\n")
fp.close()


