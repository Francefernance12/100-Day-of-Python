from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


### SQLAlchemy Initialization ###
class Base(DeclarativeBase):
    pass


# extension
db = SQLAlchemy(model_class=Base)


class MovieDB(db.Model):
    __tablename__ = 'movie'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(10000), nullable=False)
    rating: Mapped[float] = mapped_column(Float, default=0.0)
    ranking: Mapped[int] = mapped_column(Integer, default=0)
    review: Mapped[str] = mapped_column(String(10000), default="")
    img_url: Mapped[str] = mapped_column(String(250), default="")

    # # this will allow each book object to be identified by its title when printed.
    # def __repr__(self):
    #     return f'{self.title} - {self.author} - {self.rating}'
