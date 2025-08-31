import os

# Use env var if provided, otherwise default like your Spring props
# Example: export DATABASE_URL="mysql+pymysql://user:user@localhost:3306/products_db"
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://user:user@localhost:3306/products_db"
)
