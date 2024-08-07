from PIL import Image

# 이미지 파일 열기
img = Image.open('your_image_file.jpg')

# 이미지 가로, 세로 크기 출력
print(img.size)

# 이미지 출력
img.show()