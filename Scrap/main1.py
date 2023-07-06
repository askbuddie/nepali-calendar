from bs4 import BeautifulSoup


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
# Made the structure of how will the scraping be done
for td in ManyTd:
    x = td.find("div", {"class": "event_one"})
    # print(x.isspace())
    if x is not None:
        print(x.get("style"))
        print(x.get("style") == "color:#FF4D00")
        data = x.get_text(strip=True)
        if not data:
            print("No Event")
        else:
            # Print the div content
            print(data)

        # data = data.strip()
        # if data == "&nbsp;":
        #     print(True)
        # print(data.isspace())
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
