# 读 ARJ压力参数统计 文件夹下所有xls的文件名称
# 提取source文件夹下所有后缀为suffix的文件路径
import os


def getFilePathList(path, filetype):
    pathList = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(filetype):
                pathList.append(os.path.join(root, file))
    return pathList  # 输出以filetype为后缀的列表



def test3(source_folder, dis_folder, txt_name, suffix):
    # 源文件夹名称，目标文件夹名称，目标文件名，后缀
    # souece_folder 源文件夹名称，要从这个文件夹中提取所有后缀为suffix的文件名称以及路径
    # dis_folder    目标文件夹名称，设置要保存的文件所在的文件夹
    # txt_name      设置保存文件的文件名
    # suffix        设置要提取文件的后缀

    # 获取当前路径
    basedir = os.path.abspath(os.path.dirname(__file__))

    # 设置要保存的路径
    # in windows
    txt_path = basedir + '\\' + dis_folder
    if not os.path.exists(txt_path):
        os.makedirs(txt_path)
    # # in Linux
    # txt_path = basedir + '/txt_name'
    # if not os.path.exists(txt_path):
    #     os.makedirs(txt_path)

    # 提取result文件夹中以suffix为后缀的文件名称
    resdir = basedir + '\\' + source_folder
    print(resdir)
    temps = getFilePathList(resdir, suffix)
    txt_file = []
    for temp in temps:
        temp_name = temp.split('\\')[-2] + '\\' + temp.split('\\')[-1]
        txt_file.append(temp_name)
    print(txt_file)

    # 保存到 txt_name 中
    # in windows
    txt_abspath = txt_path + '\\' + txt_name
    # # in Linux
    # txt_abspath = txt_path + '/' + txt_name
    fp = open(txt_abspath, 'w')
    for i in range(len(txt_file)):
        print(txt_file[i] + "\n")
        fp.write(txt_file[i] + "\n")
    fp.close()


def main():
    source_folder = 'result'
    dis_folder = 'txt_name'
    txt_name = 'name.txt'
    suffix = 'txt'
    test3(source_folder, dis_folder, txt_name, suffix)


if __name__ == '__main__':
    main()


