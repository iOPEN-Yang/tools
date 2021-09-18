# 获取参数
import argparse
import test3


def main(args):
    test3.test3(args.source_folder, args.dis_folder, args.txt_name, args.suffix)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_folder', type=str, default='result')
    parser.add_argument('--dis_folder', type=str, default='txt_name')
    parser.add_argument('--txt_name', type=str, default='name.txt')
    parser.add_argument('--suffix', type=str, default='txt')
    opt = parser.parse_args()
    main(opt)
