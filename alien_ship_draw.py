from PIL import Image, ImageDraw

# 创建一个空白图像，大小为200x200像素，背景为黑色
width, height = 200, 200
image = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(image)

# 绘制外星飞船的主体
draw.ellipse((50, 50, 150, 150), fill="green", outline="white")

# 绘制外星飞船的顶部
draw.polygon([(100, 30), (70, 70), (130, 70)], fill="blue", outline="white")

# 绘制外星飞船的底部
draw.polygon([(100, 170), (70, 130), (130, 130)], fill="red", outline="white")

# 保存图像为BMP格式
image.save("alien_spaceship.bmp")

# 显示图像
image.show()