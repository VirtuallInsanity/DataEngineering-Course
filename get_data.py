import io
import os
import time
from pathlib import Path
import hashlib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver


def get_content_from_url(url):
    driver = webdriver.Chrome()  # Add "executable_path=" if the driver is in a custom directory.
    driver.get(url)

    # driver.execute_script("window.scrollTo(1501, document.body.scrollHeight);")  # scroll down instantly
    # time.sleep(2)
    y = 1000
    for timer in range(0, 20):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")  # scroll down iteratively
        y += 1000
        time.sleep(1)

    page_content = driver.page_source
    driver.quit()  # You don't need the browser instance for further steps.
    return page_content


def parse_image_urls(content, classes, location):
    soup = BeautifulSoup(content)
    img_url = "https://hdpic.club/"
    results = []
    for a in soup.findAll(attrs={"class": classes}):
        name = a.get(location)
        if name not in results:
            results.append(img_url + name)
    return results


def save_urls_to_csv(image_urls):
    df = pd.DataFrame({"links": image_urls})
    df.to_csv("links.csv", index=False, encoding="utf-8")


def get_and_save_image_to_file(image_url, output_dir):
    response = requests.get(image_url, headers={"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"})
    image_content = response.content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert("RGB")
    filename = hashlib.sha1(image_content).hexdigest()[:10] + ".png"
    file_path = output_dir / filename
    image.save(file_path, "PNG", quality=80)


if __name__ == "__main__":
    url = "https://hdpic.club/28286-iduschego-poezda-36-foto.html"
    out_dir = Path("data/pics")
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    content = get_content_from_url(url)
    image_urls = parse_image_urls(content=content, classes="lazy-loaded", location="src")
    save_urls_to_csv(image_urls)
    for image_url in image_urls:
        get_and_save_image_to_file(
            image_url, output_dir=out_dir,
        )