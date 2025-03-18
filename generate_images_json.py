import os
import json

# 目标文件夹
IMAGE_FOLDER = "images"
THEMES_FILE = "themes.json"
OUTPUT_FILE = "images.json"


def load_selected_themes():
    """读取 themes.json，获取选定的主题"""
    if not os.path.exists(THEMES_FILE):
        print(f"⚠️ 文件 {THEMES_FILE} 不存在，默认包含所有主题")
        return None  # 默认包含所有主题

    with open(THEMES_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data.get("selected_themes", None)  # 获取 `selected_themes` 字段


def get_images_by_themes(selected_themes):
    """根据所选主题获取图片列表"""
    images = []

    # 遍历 images/ 目录下的所有主题文件夹
    for theme_folder in os.listdir(IMAGE_FOLDER):
        theme_path = os.path.join(IMAGE_FOLDER, theme_folder)

        if not os.path.isdir(theme_path):
            continue  # 过滤非文件夹内容

        # 如果 themes.json 选择了某些主题，就过滤未选中的主题
        if selected_themes and theme_folder not in selected_themes:
            continue

        # 获取当前主题文件夹下的所有图片
        for file in os.listdir(theme_path):
            if file.lower().endswith(
                (".png", ".jpg", ".jpeg", ".webp", ".gif")):
                images.append(f"{theme_folder}/{file}")  # 记录相对路径

    return images


def generate_images_json():
    """生成 images.json 文件"""
    selected_themes = load_selected_themes()
    image_files = get_images_by_themes(selected_themes)

    # 生成 JSON 数据
    image_data = {"images": image_files}

    # 写入 images.json
    with open(OUTPUT_FILE, "w", encoding="utf-8") as json_file:
        json.dump(image_data, json_file, indent=4, ensure_ascii=False)

    print(f"✅ 成功生成 {OUTPUT_FILE}，包含 {len(image_files)} 张图片！!")


if __name__ == "__main__":
    generate_images_json()
