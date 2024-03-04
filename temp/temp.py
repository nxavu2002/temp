import urllib.request
import os
import requests
import undetected_chromedriver as uc
import time
from selenium import webdriver
from selenium_stealth import stealth
# Adding user_agent information
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

# # # Image URL and Filename
# # filename = "pic1.jpg"
image_url = "https://file4.batdongsan.com.vn/resize/200x200/2023/04/17/20230417230210-69b7_wm.jpg"

# # # # Get resource
# # # urllib.request.urlretrieve(image_url, filename)

# # print(os.listdir())
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}
driver = uc.Chrome()

driver.get(image_url)
driver.save_screenshot("new" + '.png')
# response = requests.get(image_url, headers=headers)
# time.sleep(8)
# driver.get("https://file4.batdongsan.com.vn/resize/200x200/2023/10/17/20231017141845-284e_wm.jpg")
# s = requests.session()
# s.headers.update(headers)
# for cookie in driver.get_cookies():
#     c = {cookie['name']: cookie['value']}
#     s.cookies.update(c)

# r = s.get(image_url, allow_redirects=True)
# open("pig" + '.jpg', 'wb').write(r.content)

# # urllib.request.urlretrieve(image_url, "pic.jpg")
# # headers = {
# # "User-Agent":
# #     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
# # }
# # s = requests.session()
# # s.headers.update(headers)
# # for cookie in driver.get_cookies():
# #     c = {cookie['name']: cookie['value']}
# #     s.cookies.update(c)
# # for index, image_div in enumerate(image_element):
# #     image_src = image_div.get_attribute("data-src")
# #     image_name = f"{name_element.text}_{index}.jpg"
# #     image_path = os.path.join("media", image_name)
# #     response = requests.get(image_src)
# #     if response.status_code == 200:
# #         with open(image_path, 'wb') as f:
# #             f.write(response.content)
# #             print("successfully.")
# #     else:
# #         print("Failed")

# driver.close()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

driver = uc.Chrome()
wait = WebDriverWait(driver, 30)

url = "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-pho-ton-duc-thang-phuong-ben-nghe-prj-vinhomes-golden-river-ba-son/chuyen-c-vinmes-bason-1-2-3-4-pn-gia-tot-nhat-tt-lh-xem-nha-0902762707-pr32384211"
driver.get(url)
iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 're__section-body.js__section-body iframe')))
temp = iframe.get_attribute("data-src")
driver.switch_to.frame(iframe)

try:
    # Find the place name element within the iframe
    place_name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'place-name')))

    # Get the text of the place name element
    place_name = place_name_element.text
    print("Place Name:", place_name)

except Exception as e:
    print("Error:", e)

# import requests

# url = 'https://file4.batdongsan.com.vn/resize/200x200/2023/04/17/20230417230210-69b7_wm.jpg'
# # pip install zenrows
# from zenrows import ZenRowsClient

# client = ZenRowsClient("651070fa5d2475988f14ac1e96eddea0b02c3b8b")
# response = client.get(url)
# with open("new.jpg", 'wb') as f:
#     f.write(response.content)
driver.close()
