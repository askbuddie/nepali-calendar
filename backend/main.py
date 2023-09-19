from sqlalchemy import Column, Date, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine("sqlite:///storage.db", echo=True)
Base = declarative_base()


class Date(Base):
    __tablename__ = "date"

    date = Column(String, primary_key=True)
    NepDate = Column(String)
    EngDate = Column(String)
    Day = Column(String)
    tithi = Column(String)


class Event(Base):
    __tablename__ = "event"

    event_id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(ForeignKey("date.date"))
    title = Column(String)
    color = Column(String)

    date_rel = relationship("Date", backref="events")


Base.metadata.create_all(engine)
from sqlalchemy.orm import Session


def search_data_by_year_and_month(year, month):
    with Session(engine) as session:
        # Form the search string for the year and month (e.g., "2078-10%")
        search_string = f"{year}-{month}-%"

        # Query the Date objects with the search string session.query(Date).filter(Date.date.like(pattern)).all()
        queried_dates = session.query(Date).filter(Date.date.like(search_string)).all()
        print(queried_dates)

        if queried_dates:
            results = []

            for queried_date in queried_dates:
                events = queried_date.events
                result = {
                    "date": queried_date.date,
                    "nepaliDate": queried_date.NepDate,
                    "englishDate": queried_date.EngDate,
                    "day": queried_date.Day,
                    "tithi": queried_date.tithi,
                    "events": [],
                }

                for event in events:
                    result["events"].append(
                        {"eventTitle": event.title, "eventColor": event.color}
                    )

                results.append(result)

            return results

    return None


nepali_month_dict = {
    "Baishakh": 1,
    "Jestha": 2,
    "Ashadh": 3,
    "Shrawan": 4,
    "Bhadra": 5,
    "Ashwin": 6,
    "Kartik": 7,
    "Mangsir": 8,
    "Poush": 9,
    "Magh": 10,
    "Falgun": 11,
    "Chaitra": 12,
}


from flask import Flask, request
from bleach import clean

app = Flask(__name__)


years = [2080]


@app.route("/calender", methods=["GET"])
def main():
    # Example usage
    args = request.args
    year_to_search = clean(args.get("year"))  # Replace with the year you want to search
    month_index = nepali_month_dict.get(clean(args.get("month")))
    if int(year_to_search) in years:
        if month_index is not None:
            queried_data = search_data_by_year_and_month(year_to_search, month_index)
            return queried_data

        else:
            return "You have eneterd wrong month name!"

    else:
        return "Data does not exist", 400


if __name__ == "__main__":
    app.run()
