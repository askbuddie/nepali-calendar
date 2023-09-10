from flask import Flask, render_template, jsonify, url_for
import json
import urllib

app = Flask(__name__)

# Replace this with the actual URL of your backend API


nep_month = [
    "Baishakh",
    "Jestha",
    "Ashadh",
    "Shrawan",
    "Bhadra",
    "Ashwin",
    "Kartik",
    "Mangsir",
    "Poush",
    "Magh",
    "Falgun",
    "Chaitra",
]


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def dist(a, b):
    return abs(days.index(b)) - (days.index(a))


def mod(data):
    empty = {
        "date": "",
        "day": "",
        "englishDate": "",
        "events": [
            {"eventColor": "None", "eventTitle": "None"},
            {"eventColor": "None", "eventTitle": "None"},
            {"eventColor": "None", "eventTitle": "None"},
        ],
        "nepaliDate": "",
        "tithi": "",
    }
    new_data = []
    i = 0
    app = 1
    for new in data:
        if new["day"] != days[i] and app == 1:
            app += 1
            print(new["day"], days[i])

            print(abs(dist(new["day"], days[i])))
            for p in range(0, abs(dist(new["day"], days[i]))):
                i += 1
                new_data.append(empty)
            new_data.append(new)

        else:
            new_data.append(new)
            i += 1
        if i == 7:
            i = 0
    return new_data


def next(month):
    index = nep_month.index(month) + 1
    print(index)
    print("--------------------")
    if index > 11:
        return None

    return nep_month[index]


def previous(month):
    index = nep_month.index(month) - 1
    if index < 0:
        return None
    return nep_month[index]


@app.route("/<month>")
def get_events(month):
    if month is None:
        month = "Baishakh"

    # Fetch data from your backend API
    # You can use libraries like requests or urllib to make HTTP requests
    print(month)
    url = f"https://caleneder.dipeshsharma5.repl.co/calender?month={month}&year=2080"
    print(url)
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = mod(json.loads(data))
    next_month = next(month=month)
    if next_month is None:
        next_month_url = "#"
    else:
        next_month_url = url_for("get_events", month=next_month)
    previous_month = previous(month=month)
    if previous_month is None:
        previous_month_url = "#"
    else:
        previous_month_url = url_for("get_events", month=previous_month)

    return render_template(
        "index.html",
        events=dict,
        next_month_url=next_month_url,
        previous_month_url=previous_month_url,
    )


# if __name__ == "__main__":
#     app.run(debug=True)


@app.route("/")
def events(month="Baishakh"):
    # Fetch data from your backend API
    # You can use libraries like requests or urllib to make HTTP requests

    url = f"https://caleneder.dipeshsharma5.repl.co/calender?month={month}&year=2080"
    print(url)
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = mod(json.loads(data))
    next_month = next(month=month)
    if next_month is None:
        next_month_url = "#"
    else:
        next_month_url = url_for("get_events", month=next_month)
    previous_month_url = "#"

    return render_template(
        "index.html",
        events=dict,
        next_month_url=next_month_url,
        previous_month_url=previous_month_url,
    )


if __name__ == "__main__":
    app.run(debug=True)
