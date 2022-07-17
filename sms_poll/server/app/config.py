import pathlib

from pydantic import BaseSettings, Field

ROOT_DIR = pathlib.Path(__file__).resolve().parent

class Config(BaseSettings):
    port: int = Field(5000, gt=0, le=65536)
    db_path: pathlib.Path = ROOT_DIR / 'app.db'
    debug: bool = False

config = Config()
