# -*- coding: utf-8 -*-
import os
import sys
import shutil
import json
from pprint import pprint
from PIL import Image

import Config


def _work_dir():
    return os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))


def copy_image_files():
    """将工程中的图片拷贝到 customization 目录下"""
    for x in Config.image_paths:
        src_path_dir = os.path.join(_work_dir(), x)
        dis_path_dir = os.path.join(_work_dir(), "customization", x)
        assert(os.path.isdir(src_path_dir))
        shutil.copytree(src_path_dir, dis_path_dir, symlinks=False)


def creat_image_json():
    """创建图片描述文件"""
    for x in Config.image_paths:
        src_path_dir = os.path.join(_work_dir(), x)
        dis_path_dir = os.path.join(_work_dir(), "customization", x)
        json_path = os.path.join(src_path_dir, 'Contents.json')
        assert(os.path.isfile(json_path))
        new_images = []
        with open(json_path, 'r') as f:
            data = json.load(f)
            images = data["images"]
            for image in images:
                if not image.has_key("filename"):
                    continue
                filename = image["filename"]
                size = ''
                if not image.has_key("size"):
                    img = Image.open(os.path.join(dis_path_dir, filename))
                    w, h = img.size
                    size = str(w) + 'x' + str(h)
                else:
                    size = image["size"]
                scale = image["scale"]
                new_data = {
                    'filename': filename,
                    'size': size,
                    'scale': scale
                }
                new_images.append(new_data)
        new_images.sort()
        newjson_path = os.path.join(dis_path_dir, 'Contents.json')
        with open(newjson_path, 'w') as f:
            json.dump(new_images, f, indent=3)


if __name__ == '__main__':
    # copy_image_files()
    creat_image_json()
