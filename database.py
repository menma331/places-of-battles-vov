from sqlalchemy import Integer, VARCHAR, Text, Float, String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Place(Base):
    __tablename__ = 'place'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    title: Mapped[str] = mapped_column(VARCHAR(70))
    description: Mapped[str] = mapped_column(Text)
    latitude: Mapped[float] = mapped_column(Float, comment='Широта')
    longitude: Mapped[float] = mapped_column(Float, comment='Долгота')
    img_url: Mapped[str] = mapped_column(String, nullable=True)
    date_start: Mapped[str] = mapped_column(String)
    date_end: Mapped[str] = mapped_column(String)
