from pathlib import Path

# Hitta projektets rotmapp
BASE_DIR = Path(__file__).resolve().parent.parent

# Sökväg till mappen där data ligger
DATA_DIR = BASE_DIR / "data"

# Sökväg till loggfiler
LOG_DIR = BASE_DIR / "logs"

# Skapa loggmappen om den inte finns
LOG_DIR.mkdir(exist_ok=True)
