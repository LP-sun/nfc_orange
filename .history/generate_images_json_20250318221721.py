import os
import json

# 目标文件夹
IMAGE_FOLDER = "images"

# 获取所有图片文件
image_files = [
    f for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))
]

# 生成 JSON 数据
image_data = {"images": image_files}

# 写入 images.json
with open("images.json", "w", encoding="utf-8") as json_file:
    json.dump(image_data, json_file, indent=4, ensure_ascii=False)

print(f"✅ 成功生成 images.json，包含 {len(image_files)} 张图片！")
