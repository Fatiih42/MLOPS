import pandas as pd
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from main import engine, SessionLocal
from models import TextData

# Charger les données du CSV
df = pd.read_csv("/mnt/data/dataset.csv")
#D:\m2\mlops\TD_API\TD2\build_api_ml\data

async def insert_data():
    async with SessionLocal() as session:
        for _, row in df.iterrows():
            new_entry = TextData(text=row["Text"], language=row["language"])
            session.add(new_entry)
        await session.commit()
        print(" Données insérées avec succès !")

asyncio.run(insert_data())