import os
import requests
from bs4 import BeautifulSoup

def save_images(keyword, num_images):
    # 이미지를 저장할 폴더 생성하기
    save_directory = "images/" + keyword.replace(" ", "_")
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # 이미지 검색 및 다운로드
    url = f"https://www.google.com/search?q={keyword}&tbm=isch"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.select("img[src^='https://encrypted-tbn0.gstatic.com/']")

    count = 1
    for image in images[:num_images]:
        image_url = image["src"]
        image_data = requests.get(image_url).content

        with open(f"{save_directory}/{keyword}_{count}.jpg", "wb") as file:
            file.write(image_data)

        count += 1

if __name__ == '__main__':
    keyword = input("검색 키워드: ")
    num_images = int(input("이미지 개수: "))

    save_images(keyword, num_images)