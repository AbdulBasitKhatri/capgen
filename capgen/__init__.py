from PIL import Image, ImageDraw, ImageFont
import random
import string

def generate(length):
  text = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
  width, height = 200, 100
  image = Image.new('RGB', (width, height), (255, 255, 255))
  draw = ImageDraw.Draw(image)
  font = ImageFont.load_default(size=15)
  for i, v in enumerate(text):
    x = random.randint(i * width // length, i * width // length + random.randint(0, 30))
    y = random.randint(0, height - 20)
    draw.text((x, y), v, fill=(0, 0, 0), font=font)
    for _ in range(3):
      start = (x - 30, random.randint(y - 30, y + 20))
      end = (x + 30, random.randint(y - 30, y + 20))
      draw.line([start, end], fill=(random.randint(0, 125), random.randint(0, 155), random.randint(0, 150)), width=1)
  for _ in range(3000):
    x = random.randint(0, width)
    y = random.randint(0, height)
    draw.point((x, y, x + 2, y + 2), fill=(random.randint(0, 125), random.randint(0, 155), random.randint(0, 150)))
  return image, text
