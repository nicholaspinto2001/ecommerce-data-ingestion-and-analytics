from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os

load_dotenv()

port = int(os.getenv("DB_PORT", 5432))
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{port}/{os.getenv('DB_NAME')}"
)


with engine.connect() as connection:
    try:
        result = connection.execute(text("SELECT 1"))
        print(result.scalar())
        print(f'Successfully connected to the database: {os.getenv("DB_NAME")}')
    except Exception as e:
        raise ValueError(f"Database connection failed: {e}")
    
    