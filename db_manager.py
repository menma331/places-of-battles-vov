from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from database import Place
from schema import PlaceSchema

engine = create_engine(f'sqlite:///database.db')

Session = sessionmaker(bind=engine)
session = Session()


def add_new_place(title, description, latitude: float, longitude: float, img_url, date_start, date_end):
    new_place = Place(title=title, description=description, latitude=latitude, longitude=longitude, img_url=img_url, date_start=date_start, date_end=date_end)
    session.add(new_place)
    session.commit()

    print(f"|Добавлено|'{title}'.")


def get_list_of_places():
    query = select(Place)
    query_result = session.execute(query).scalars().all()

    res = []
    for place in query_result:
        title = place.title
        description = place.description
        latitude = place.latitude
        longitude = place.longitude
        img_url = place.img_url
        date_start = place.date_start
        date_end = place.date_end

        res.append(
            PlaceSchema(
                title=title,
                description=description,
                latitude=latitude,
                longitude=longitude,
                img_url=img_url,
                date_start=date_start,
                date_end=date_end
            )
        )

    return res
