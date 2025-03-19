from sqlalchemy import Column, Integer, String
from db import Base

class TextData(Base):
    __tablename__ = "text_data"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    language = Column(String, nullable=False)