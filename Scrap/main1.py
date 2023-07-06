# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# import requests

# # driver = webdriver.Chrome()
# # driver.get("https://www.ashesh.com.np/nepali-calendar/")
# url = "https://www.ashesh.com.np/nepali-calendar/"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9",
# }
# import json

# data = requests.get(url, headers=headers)
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#     script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
#     print(script_tag)
#     if script_tag is not None:
#         json_blob = json.loads(script_tag.get_text())
#         product_data = json_blob["props"]["pageProps"]["initialData"]["data"]["product"]

# # r.raise_for_status()
# # data = r.json()
# # print(data["data"]["currentStatistics"])
# soup = BeautifulSoup(data.text, "html.parser")
# # print(soup)

# # soup = BeautifulSoup(html)

# # assert "Python" in driver.title
# # elem = driver.find_element(By.NAME, "q")
# # elem.clear()
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)
# # assert "No results found." not in driver.page_source
# # driver.close()

# from time import sleep
# from selenium import webdriver


# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome()

# driver.get("https://www.ashesh.com.np/nepali-calendar/")

# driver.execute_script(
#     "window.scrollTo(0, document.body.scrollHeight);"
# )  ## Scroll to bottom of page with using driver
# sleep(5)


# html = driver.page_source

# soup = BeautifulSoup(html, "html.parser")
# soup = soup.find_all("div", {"id": "container"})
# print(soup)
# # print(soup.prettify())
# from requests_html import HTMLSession

# # create the session
# session = HTMLSession()

# # define our URL
# url = "https://www.ashesh.com.np/nepali-calendar/"

# # use the session to get the data
# r = session.get(url)

# # Render the page, up the number on scrolldown to page down multiple times on a page
# r.html.render(sleep=1, keep_page=True, scrolldown=1)
# page_source = r.html.html

# # Print the page source code
# print(page_source)
# take the rendered html and find the element that we are interested in
# videos = r.html.find('#video-title')

# loop through those elements extracting the text and link
# for item in videos:
#     video = {
#         'title': item.text,
#         'link': item.absolute_links
#     }
#     print(video)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Selenium options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set path to chromedriver executable (Update with your own path)
chromedriver_path = "/chromedriver/chromedriver"

# Create a new Selenium web driver with the specified options
driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)

# Define the URL
url = "https://www.ashesh.com.np/nepali-calendar/"

# Navigate to the URL
driver.get(url)

# Wait for the page to load (You might need to adjust the sleep duration)
driver.implicitly_wait(5)  # Wait for 5 seconds

# Scroll down the page (You can adjust the scroll height based on your requirements)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Get the page source code
page_source = driver.page_source

# Print the page source code
soup = BeautifulSoup(page_source, "html.parser")
table = soup.find("table", {"id": "calendartable"})
ManyTd = soup.find_all("td")
for td in ManyTd:
    x = td.find("div", {"class": "event_one"})
    # print(x.isspace())
    if x is not None:
        data = x.get_text(strip=True)

        # data = data.strip()
        if data == "&nbsp;":
            print(True)
        print(data.isspace())
        # print(type(data))
        # if data.isspace():
        #     print("No event")
        # else:
        #     print(data)
    else:
        print("No event")
# print(table.prettify())
# Close the browser
driver.quit()
