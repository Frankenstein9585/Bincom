import os
import re

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Baby(Base):
    __tablename__ = 'baby_names'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def extract_names():
    # Extraction of baby names from html file
    pattern = r"<td>([a-zA-Z]+)</td>"

    with open('../baby2008.html', 'r') as baby_file:
        file_content = baby_file.read()

    baby_names = re.findall(pattern, file_content)

    for name in baby_names:
        baby = Baby(name=name)
        session.add(baby)
    session.commit()


extract_names()
