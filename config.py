# Lassy LLC Hyper Agents - Configuration

import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed, use env vars directly

# API Keys (all optional - demo mode works without them)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
CJ_API_KEY = os.getenv("CJ_API_KEY", "")
CJ_API_BASE = "https://developers.cjdropshipping.com/api2.0/v1/"
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN", "")
SHOPIFY_STORE = os.getenv("SHOPIFY_STORE", "lassygeneralstore.shop")

# Business Rules (Roger's rules)
MIN_PROFIT = 5.00  # Minimum $5/unit profit floor
BANNED_KEYWORDS = [
    "lithium", "lithium-ion", "li-ion", "rechargeable battery",
    "liquid", "beverage", "drink", "juice",
    "supplement", "vitamin", "medicine", "drug",
    "hazmat", "hazardous", "flammable", "explosive",
    "fragile", "glass", "ceramic", "porcelain",
]
BANNED_CATEGORIES = ["weapons", "adult", "tobacco", "alcohol"]

# Store Info
STORE_NAME = "Lassy General Store"
STORE_URL = "https://lassygeneralstore.shop"
STORE_EMAIL = "rogersy@lassygeneralstore.com"
STORE_PHONE = "+1 571 569 6829"

# Output
OUTPUT_DIR = "output"

# Demo mode - True if no API keys set
DEMO_MODE = not bool(OPENAI_API_KEY)
