import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

def response_search():
    response = requests.get(search_url, params=search_params)
    if response.status_code == 200:
        data = response.json()  # отримання даних у форматі JSON
        print('Отримано дані:', data)
        items = data.get("collection", {}).get("items", [])
        print("Знайдено елементів:", len(items))

        nasa_ids = []
        for item in items:
            data_block = item.get("data", [])
            if not data_block:
                continue

            for block in data_block:
                nasa_id = block.get("nasa_id")
                if nasa_id:
                    nasa_ids.append(nasa_id)

        return nasa_ids
    else:
        print('Помилка. Статус-код:', response.status_code)
        return []

def asset_response(nasa_id):
    asset_url = asset_url_template.format(nasa_id=nasa_id)
    response = requests.get(asset_url)
    if response.status_code == 200:
        asset_data = response.json()  # отримання даних у форматі JSON
        # print('Отримано дані:', asset_data)
        asset_items = asset_data.get("collection", {}).get("items", [])

        image_urls = []
        for item in asset_items:
            href = item.get("href")
            if href and href.lower().endswith((".jpg", ".jpeg", ".png")):
                image_urls.append(href)
        print(f"{nasa_id}: знайдено {len(image_urls)} зображень")
        return image_urls
    else:
        print('Помилка. Статус-код:', response.status_code)
        return []

def choose_img(image_urls):
    for url in image_urls:
        if url.lower().endswith(("~orig.jpg", "~orig.jpeg", "~orig.png")):
            return url
        elif not url.lower().endswith(("~orig.jpg", "~orig.jpeg", "~orig.png")):
            return image_urls[0]
        else:
            continue


def download_two_img(image_urls):
    print("Починаємо завантаження зображень")

    for i in range(2):
        url = image_urls[i]
        filename = f"mars_photo{i + 1}.jpg"

        response = requests.get(url)

        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Файл {filename} збережено")
        else:
            print(f"Помилка при завантаженні {url}")

nasa_ids = response_search()

for nasa_id in nasa_ids:
    urls = asset_response(nasa_id)
    best = choose_img(urls)
    print(f"Image for {nasa_id}: {best}")

download_two_img(urls)

