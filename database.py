import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor de la base de datos
# Neon requiere sslmode=require, que ya está incluido en la DATABASE_URL
engine = create_engine(DATABASE_URL)

# Crear una sesión local para interactuar con la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para nuestros modelos
class Base(DeclarativeBase):
    pass

# Dependencia para obtener la sesión de DB en los endpoints de FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
