from sqlmodel import SQLModel, Session, create_engine

db_url = 'postgresql://postgres:Aliya2103@localhost/todo'
engine = create_engine(db_url, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session