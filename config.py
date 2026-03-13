import os
from dotenv import load_dotenv

# Carga el .env en desarrollo local; en Render las vars ya están en el entorno
load_dotenv()

class Config:
    # ── Flask ──────────────────────────────────
    SECRET_KEY  = os.environ.get("SECRET_KEY", "dev-secret-key-cambiar")
    FLASK_ENV   = os.environ.get("FLASK_ENV", "development")
    DEBUG       = FLASK_ENV == "development"

    # ── MySQL / Aiven ──────────────────────────
    MYSQL_HOST     = os.environ.get("DB_HOST", "localhost")
    MYSQL_PORT     = int(os.environ.get("DB_PORT", 3306))
    MYSQL_USER     = os.environ.get("DB_USER", "root")
    MYSQL_PASSWORD = os.environ.get("DB_PASSWORD", "")
    MYSQL_DB       = os.environ.get("DB_name", "eps_citas")

    # SSL: True en Aiven (producción), False en local
    MYSQL_SSL      = os.environ.get("MYSQL_SSL", "false").lower() == "true"
