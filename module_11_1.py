from PIL import Image, ImageFilter

file_name = 'photorealistic-rainbow-with-countryside-nature-landscape_23-2151597638.jpg'
with Image.open(file_name) as f:
    f.load()

resize_f = f.resize((1920, 1080))
rotate_f = resize_f.rotate(45, expand=True)
filter_f = rotate_f.filter(ImageFilter.BoxBlur(1))
filter_f.show()
filter_f.save("new_image.png")