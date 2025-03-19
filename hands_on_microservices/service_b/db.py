import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Récupération de l'URL de la base de données
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@db:5432/mydatabase")

# Création du moteur SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)

# Création de la session
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base pour les modèles SQLAlchemy
Base = declarative_base()