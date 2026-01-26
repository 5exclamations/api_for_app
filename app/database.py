from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Временно SQLite для быстрой работы
DATABASE_URL = "sqlite:///./products.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Только для SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Создать таблицы
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
