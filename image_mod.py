from PIL import Image, ImageTk

def load_image(path, size=(100, 100)):
    img = Image.open(path)
    img = img.resize(size)
    return ImageTk.PhotoImage(img)
