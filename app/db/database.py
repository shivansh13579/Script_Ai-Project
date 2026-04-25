from sqlmodel import SQLModel, create_engine,Session
from app.db.models import Script
from app.core.config import settings
from app.core.logger import logger
from sqlalchemy.exc import OperationalError
import time

from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
    connect_args={"charset": "utf8mb4"},
)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    print("creating tables if not exist...")
    SQLModel.metadata.create_all(engine)
    print("Tables created successfully ✅")

def init_db_with_retry():
    retries = 10
    delay = 3

    while retries > 0:
        try:
            logger.info("⏳ Attempting DB connection...")
            init_db()
            logger.info("🎉 DB connected and ready")
            return 
        except OperationalError as e:
            logger.error(f"❌ DB not ready. Retries left: {retries}")
            logger.error(str(e))
            time.sleep(delay)
            retries -= 1

    raise Exception("🚫 Failed to connect to DB after multiple retries")
