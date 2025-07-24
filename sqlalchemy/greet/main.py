"""Greetings from sqlalchemy"""

from sqlalchemy import Text
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import Session
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    """Base"""

class Greeting(Base):
    """Greeting"""

    __tablename__ = "greetings"

    id: Mapped[int] = mapped_column(primary_key=True)
    greeting: Mapped[str] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"Greeting(id={self.id!r}, greeting={self.greeting!r})"


def insert_greeting(session: Session, greeting: str):
    """Insert greeting"""

    print(f"Inserting greeting \"{greeting}\"...")
    g = Greeting(greeting=greeting)
    session.add(g)
    session.commit()


def list_greetings(session: Session):
    """List greetings"""

    print("Listing greetings...")
    stmt = select(Greeting)
    for greeting in session.scalars(stmt):
        print(greeting)


def get_id(session: Session, greeting_id: int):
    """Get greeting by ID"""

    print(f"Getting greeting by ID {greeting_id}...")
    stmt = select(Greeting).where(Greeting.id == greeting_id)
    g = session.scalars(stmt).one()
    print(g)


def get_text(session: Session, text: str):
    """Get greeting by text"""

    print(f"Getting greeting by text \"{text}\"...")
    stmt = select(Greeting).where(Greeting.greeting == text)
    g = session.scalars(stmt).one()
    print(g)


def delete_id(session: Session, greeting_id: int):
    """Delete greeting by ID"""

    print(f"Deleting greeting by ID {greeting_id}...")
    stmt = select(Greeting).where(Greeting.id == greeting_id)
    g = session.scalars(stmt).one()
    session.delete(g)
    session.commit()


def main():
    """Main entry point"""

    # create db and table
    from sqlalchemy import create_engine
    engine = create_engine("sqlite://", echo=True)
    Base.metadata.create_all(engine)


    # fill table
    session = Session(engine)
    for greeting in ("hello", "hi", "good day", "greetings"):
        insert_greeting(session, greeting)

    #with Session(engine) as session:
    #    hello = Greeting(greeting="hello")
    #    hi = Greeting(greeting="hi")
    #    good_day = Greeting(greeting="good day")
    #    greetings = Greeting(greeting="greetings")
    #    session.add_all([hello, hi, good_day, greetings])
    #    session.commit()

    # list greetings
    list_greetings(session)

    # get greeting by ID
    get_id(session, 1)

    # get greeting by text
    get_text(session, "good day")

    # delete greeting by ID
    delete_id(session, 2)
    list_greetings(session)


if __name__ == "__main__":
    main()
