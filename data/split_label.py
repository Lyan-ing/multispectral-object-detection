import os
from tqdm import tqdm
import shutil

# 定义数据集的根目录
dataset_root = '/data/yl/data/LLVIP'

# 定义图像和标签的目录
image_dir = os.path.join(dataset_root, 'visible')
label_dir = os.path.join(dataset_root, 'label')

# 定义训练和测试的子目录
train_image_dir = os.path.join(image_dir, 'train')
test_image_dir = os.path.join(image_dir, 'test')

# 创建训练和测试标签的目录
train_label_dir = os.path.join(dataset_root, 'labels', 'train')
test_label_dir = os.path.join(dataset_root, 'labels', 'test')

os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(test_label_dir, exist_ok=True)

# 获取训练和测试图像的文件名
train_images = [f for f in os.listdir(train_image_dir)]  # 
test_images = [f for f in os.listdir(test_image_dir)]

# 将标签文件移动到相应的训练和测试目录
for image_file in tqdm(train_images):
    base_name, _ = os.path.splitext(image_file)
    label_file = base_name + '.txt'
    # label_file = image_file.replace('.jpg', '.txt')
    src_label_path = os.path.join(label_dir, label_file)
    dst_label_path = os.path.join(train_label_dir, label_file)
    shutil.copy(src_label_path, dst_label_path)

for image_file in tqdm(test_images):
    # label_file = image_file.replace('.jpg', '.txt')
    base_name, _ = os.path.splitext(image_file)
    label_file = base_name + '.txt'
    src_label_path = os.path.join(label_dir, label_file)
    dst_label_path = os.path.join(test_label_dir, label_file)
    shutil.copy(src_label_path, dst_label_path)

print("标签文件已成功移动到训练和测试目录下。")