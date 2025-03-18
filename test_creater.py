from PIL import Image, ImageDraw
import os
import random

# 创建 images/test 目录
output_dir = "images/test"
os.makedirs(output_dir, exist_ok=True)

# 生成 20 张小图片，每张底色不同
for i in range(1, 21):
    # 生成随机背景颜色
    background_color = (random.randint(0, 255), random.randint(0, 255),
                        random.randint(0, 255))

    img = Image.new("RGB", (200, 100), color=background_color)  # 随机背景
    draw = ImageDraw.Draw(img)
    text = f"this is a test {i}"

    # 在图片中心绘制文字（使用黑色或白色，确保对比度）
    text_color = (255, 255, 255) if sum(background_color) < 382 else (
        0, 0, 0)  # 亮色背景用黑字，暗色背景用白字
    draw.text((20, 40), text, fill=text_color)

    # 保存图片
    img_path = os.path.join(output_dir, f"test_{i}.png")
    img.save(img_path)

# 确保生成的文件可供用户下载
output_dir
