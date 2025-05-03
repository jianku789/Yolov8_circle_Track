# 导入必要的库
import os
import argparse

# 定义make_dataset函数，用于处理数据集
def make_dataset(opt):
    data_path = opt.data_path  # 从命令行参数获取数据路径
    valid_extensions = ['.jpg', '.png', '.bmp']  # 定义支持的图像文件格式

    # 定义一个函数，用于判断文件是否为图像文件
    def is_image_file(filename):
        return any(filename.lower().endswith(ext) for ext in valid_extensions)

    # 定义一个函数，用于处理指定目录中的文件
    def process_directory(directory, file):
        for filename in os.listdir(directory):  # 遍历目录中的所有文件
            if is_image_file(filename):  # 判断文件是否为图像文件
                file_path = os.path.join(directory, filename)  # 获取文件的完整路径
                file.write(file_path + '\n')  # 将文件路径写入到文本文件中

    # 构造训练集和验证集图像的路径
    train_images_path = os.path.join(data_path, 'images/train')
    val_images_path = os.path.join(data_path, 'images/val')

    # 创建并写入train.txt文件
    with open(os.path.join(data_path, 'train.txt'), 'w') as f:
        process_directory(train_images_path, f)  # 处理训练集目录

    # 创建并写入val.txt文件
    with open(os.path.join(data_path, 'val.txt'), 'w') as f:
        process_directory(val_images_path, f)  # 处理验证集目录

# 定义parse_opt函数，用于解析命令行参数
def parse_opt(known=False):
    parser = argparse.ArgumentParser()  # 创建ArgumentParser对象
    parser.add_argument('--data_path', type=str, default='your data_path')  # 添加data_path参数

    # 根据known标志决定是解析已知参数还是全部参数
    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    return opt

# 当脚本直接运行时执行以下代码
if __name__ == "__main__":
    opt = parse_opt()  # 解析命令行参数
    make_dataset(opt)  # 使用解析得到的参数调用make_dataset函数
