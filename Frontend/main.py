from flask import Flask, render_template, jsonify
import json
import urllib

app = Flask(__name__)

# Replace this with the actual URL of your backend API
url = "https://caleneder.dipeshsharma5.repl.co/calender?month=Mangsir&year=2080"


#
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


@app.route("/")
def get_events():
    # Fetch data from your backend API
    # You can use libraries like requests or urllib to make HTTP requests
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = mod(json.loads(data))

    return render_template("index.html", events=dict)


if __name__ == "__main__":
    app.run(debug=True)
