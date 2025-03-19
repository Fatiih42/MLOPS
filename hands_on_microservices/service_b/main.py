'''from fastapi import FastAPI, Depends
from db import engine, SessionLocal, Base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from models import TextData
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@db:5432/mydatabase")



engine = create_async_engine(DATABASE_URL, echo=True)


SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


Base = declarative_base()


app = FastAPI()


async def get_db():
    async with SessionLocal() as session:
        yield session


@app.get("/data")
async def get_data(db: AsyncSession = Depends(get_db)):
    return {"message": "Base de données connectée"}

@app.get("/texts")
async def get_texts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TextData))
    texts = result.scalars().all()
    return [{"id": t.id, "text": t.text, "language": t.language} for t in texts]'''

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db import SessionLocal, engine, Base
from models import TextData

# Initialisation de FastAPI
app = FastAPI()

# Création automatique des tables au démarrage
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup_event():
    await init_db()

# Dépendance pour récupérer la session DB
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.get("/home")
async def home():
    return {"message": "Bienvenue sur la page d'accueil"}

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'API Service B"}

# Endpoint pour tester la connexion DB
@app.get("/data")
async def get_data(db: AsyncSession = Depends(get_db)):
    return {"message": "Base de données connectée"}

# Endpoint pour récupérer les textes
@app.get("/texts")
async def get_texts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TextData))
    texts = result.scalars().all()
    return [{"id": t.id, "text": t.text, "language": t.language} for t in texts]