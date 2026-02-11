import requests

BASE_URL = "http://127.0.0.1:8080"


file_path = "76f0311453148cc0540f95344ee5026f.jpg"

with open(file_path, "rb") as f:
    files = {"image": f}
    response = requests.post(f"{BASE_URL}/upload", files=files)

if response.status_code == 201:
    image_url = response.json().get("image_url")
    print("Завантажено успішно! URL:", image_url)
else:
    print("Помилка завантаження:", response.status_code, response.text)


filename = image_url.split("/")[-1]
response = requests.get(f"{BASE_URL}/image/{filename}", headers={"Content-Type": "text"})
if response.status_code == 200:
    print("Отриманий URL з сервера:", response.json().get("image_url"))
else:
    print("Помилка отримання URL:", response.status_code, response.text)

response = requests.delete(f"{BASE_URL}/delete/{filename}")
if response.status_code == 200:
    print("Зображення видалено. Повідомлення сервера:", response.json())
else:
    print("Помилка видалення:", response.status_code, response.text)
