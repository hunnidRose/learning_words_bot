from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core import get_dsn

engine = create_engine(
    url=get_dsn(),
    echo=True
)


SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)
