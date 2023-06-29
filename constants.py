import os

from chromadb.config import Settings
from dotenv import load_dotenv

load_dotenv()

# Define the folder for storing database on disk and load
PERSIST_DIRECTORY = os.environ.get("PERSIST_DIRECTORY")

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
    chroma_db_impl="duckdb+parquet",
    # Optional, defaults to .chromadb/ in the current directory
    persist_directory=PERSIST_DIRECTORY,
    anonymized_telemetry=False,
)
