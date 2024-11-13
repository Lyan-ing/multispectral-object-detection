import json
import os

def coco2yolo(coco_json_path, output_dir):
    # 读取COCO格式的JSON文件
    with open(coco_json_path, 'r') as f:
        coco_data = json.load(f)

    # 创建一个类别ID到类别名称的映射
    categories = {cat['id']: cat['name'] for cat in coco_data['categories']}

    # 创建一个类别名称到类别ID的映射（YOLO格式需要从0开始）
    cat_id_to_yolo_id = {cat['id']: idx for idx, cat in enumerate(coco_data['categories'])}

    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历每个图像
    for image in coco_data['images']:
        image_id = image['id']
        image_width = image['width']
        image_height = image['height']
        image_name = image['file_name']

        # 创建一个空的YOLO格式的标注文件
        yolo_lines = []

        # 遍历每个标注
        for annotation in coco_data['annotations']:
            if annotation['image_id'] == image_id:
                bbox = annotation['bbox']
                category_id = annotation['category_id']

                # COCO的bbox格式是 [x_min, y_min, width, height]
                x_min, y_min, box_width, box_height = bbox

                # 计算YOLO格式的中心点坐标和宽高
                x_center = (x_min + box_width / 2) / image_width
                y_center = (y_min + box_height / 2) / image_height
                width = box_width / image_width
                height = box_height / image_height

                # 获取YOLO格式的类别ID
                yolo_category_id = cat_id_to_yolo_id[category_id]

                # 添加到YOLO格式的标注文件中
                yolo_lines.append(f"{yolo_category_id} {x_center} {y_center} {width} {height}")

        # 保存YOLO格式的标注文件
        yolo_file_path = os.path.join(output_dir, os.path.splitext(image_name)[0] + '.txt')
        with open(yolo_file_path, 'w') as f:
            f.write('\n'.join(yolo_lines))

# 示例用法
coco_json_path = 'path/to/coco.json'
output_dir = 'path/to/output_dir'
coco2yolo(coco_json_path, output_dir)