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
        search_string = f"{year}-{month:02}%"

        # Query the Date objects with the search string
        queried_dates = session.query(Date).filter(Date.date.like(search_string)).all()
        print(queried_dates)

        if queried_dates:
            results = []

            for queried_date in queried_dates:
                events = queried_date.events
                result = {
                    "date": queried_date.date,
                    "Nepali Date": queried_date.NepDate,
                    "English Date": queried_date.EngDate,
                    "Day": queried_date.Day,
                    "Tithi": queried_date.tithi,
                    "events": [],
                }

                for event in events:
                    result["events"].append(
                        {"Event Title": event.title, "Event Color": event.color}
                    )

                results.append(result)

            return results

    return None


# Example usage
year_to_search = "2080"  # Replace with the year you want to search
month_to_search = "11"  # Replace with the month you want to search

queried_data = search_data_by_year_and_month(year_to_search, month_to_search)
i = 1
if queried_data:
    for data in queried_data:
        print("Date:", data["date"])
        print("Nepali Date:", data["Nepali Date"])
        print("English Date:", data["English Date"])
        print("Day:", data["Day"])
        print("Tithi:", data["Tithi"])
        i += 1

        events = data["events"]
        if events:
            print("Events:")
            for event in events:
                print("Event Title:", event["Event Title"])
                print("Event Color:", event["Event Color"])
        else:
            print("No events found for the date.")
else:
    print("No data found for the specified year and month.")
print(i)
