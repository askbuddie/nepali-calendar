from bs4 import BeautifulSoup


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def scrap(data):
    data = data.get_text(strip=True)
    if not data:
        return "None"
    else:
        # Print the div content
        return data


def style(data):
    color = data.get("style")
    if color == "color:#FF4D00":
        return "Red"
    elif color == "color:#89BB0E":
        return "Green"
    else:
        return "None"


# It will find all the events on the page and then save it in the database
def events_collector(ManyTr):
    # Event

    day_of_week_dict = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    # <div class="rotate_right"></div>
    # <div class="event_one">गथाँमुग</div>
    # <div class="rotate_left"></div>
    # <div class="date_np">31</div>

    # <div class="tithi"> Chaturdashi </div>
    # <div class="date_en">16</div></td>

    for trs in ManyTr:
        # Week Day intializer
        a = 1
        tds = trs.find_all("td")

        for td in tds:
            Events = []
            Color_code = []
            event = td.find("div", {"class": "event_one"})
            left_event = td.find("div", {"class": "rotate_left"})
            right_event = td.find("div", {"class": "rotate_right"})
            tithi = td.find("div", {"class": "tithi"})
            NepDate = td.find("div", {"class": "date_np"})
            EngDate = td.find("div", {"class": "date_en"})
            # Checking if everything is Not None
            if (
                event is not None
                and left_event is not None
                and right_event is not None
                and tithi is not None
                and NepDate is not None
                and EngDate is not None
            ):
                Events.append(scrap(event))
                Color_code.append(style(event))
                Events.append(scrap(left_event))
                Color_code.append(style(left_event))
                Events.append(scrap(right_event))
                Color_code.append(style(right_event))
                tithi = scrap(tithi)
                NepDate = scrap(NepDate)
                EngDate = scrap(EngDate)
                day = day_of_week_dict.get(a)
                print((Events, Color_code, day, tithi, EngDate, NepDate))

            # ...

            # print(day_of_week_dict.get(a))
            # print(td)
            a += 1

        # x = td.find("div", {"class": "event_one"})
        # Checking the td of only calender
        # if x is not None:
        #     data = x.get_text(strip=True)
        #     print(a)
        #     a += 1
        #     if not data:
        #         print("No Event")
        #     else:
        #         # Print the div content
        #         print(data)


# Now using the page source code and parsing it to bs4
def get_content(page_source):
    soup = BeautifulSoup(page_source, "html.parser")
    table = soup.find("table", {"id": "calendartable"})
    ManyTr = soup.find_all("tr")
    events_collector(ManyTr=ManyTr)


# Set up Selenium options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set path to chromedriver executable (Update with your own path)
chromedriver_path = "/chromedriver/chromedriver"

# Create a new Selenium web driver with the specified options
driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)


def dynamic_page_scrape(url):
    # Define the URL

    # Navigate to the URL
    driver.get(url)

    # Wait for the page to load (You might need to adjust the sleep duration)
    driver.implicitly_wait(5)  # Wait for 5 seconds

    # Scroll down the page (You can adjust the scroll height based on your requirements)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Get the page source code
    page_source = driver.page_source
    get_content(page_source=page_source)
    driver.quit()


# print(table.prettify())
# Close the browser

dynamic_page_scrape(url="https://www.ashesh.com.np/nepali-calendar/")
