import requests
import pandas as pd
from PIL import Image, ImageFilter
print("\n", "requests: ", "\n")
response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
print("\n", "pandas: ", "\n")
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)
df.describe()
print("\n", "Pillow: ", "\n")
img = Image.open('img.jpg')
img = img.resize((100, 100))
img = img.filter(ImageFilter.BLUR)
img.save('modified_image.jpg')