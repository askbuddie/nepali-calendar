from sqlalchemy import Column, Date, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=True)
Base = declarative_base()


class Date(Base):
    __tablename__ = "date"

    date = Column(Date, primary_key=True)
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


def add(date,Events, Color_code, day, tithi, EngDate, NepDate):
    with Session(engine) as session:
        
        date1 = Date(date=date, Day=day, tithi=tithi, EngDate=EngDate, NepDate=NepDate)
        session.add(date1)
        for item1, item2 in zip(Events, Color_code):
            event = Event(date=date, title=item1, color=item2)
            session.add(event)

        session.commit()
