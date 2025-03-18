from PIL import Image, ImageDraw
import os

# 创建 images/test 目录
output_dir = "images/test"
os.makedirs(output_dir, exist_ok=True)

# 生成 20 张小图片
for i in range(1, 21):
    img = Image.new("RGB", (200, 100), color=(255, 255, 255))  # 白色背景
    draw = ImageDraw.Draw(img)
    text = f"this is a test {i}"

    # 在图片中心绘制文字
    draw.text((20, 40), text, fill=(0, 0, 0))

    # 保存图片
    img_path = os.path.join(output_dir, f"test_{i}.png")
    img.save(img_path)

# 确保生成的文件可供用户下载
output_dir
