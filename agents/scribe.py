# Scribe - Listing Writer Agent
# Writes product titles, descriptions, bullet points

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents import BaseAgent

class Scribe(BaseAgent):
    def __init__(self):
        super().__init__("Scribe")
    
    def write_title(self, product_name: str, category: str = "") -> str:
        """Write SEO-friendly product title (under 70 chars)."""
        # Clean and optimize title
        title = product_name.strip()
        if len(title) > 70:
            title = title[:67] + "..."
        return title
    
    def write_description(self, product: dict) -> str:
        """Write product description (benefits-first, honest delivery)."""
        name = product.get("name", "Product")
        category = product.get("category", "")
        warehouse = product.get("warehouse", "China")
        
        if warehouse.lower() == "china":
            delivery = "Ships from our supplier warehouse. Delivery in 5-11 business days. Order early for holidays!"
        else:
            delivery = "Ships from US warehouse. Fast delivery in 3-5 business days."
        
        desc = f"""{name}

Perfect for {category.lower()} and everyday use. Quality you can trust at a price that works for regular people.

✨ Key Features:
• High-quality materials built to last
• Great value — premium feel without the premium price
• Perfect gift for family and friends

📦 What's Included:
• 1x {name}

🚚 Shipping:
{delivery}

💯 Satisfaction Guarantee:
If you're not happy, we'll make it right. Your satisfaction is our priority.

Shop with confidence at Lassy General Store — where everyone can afford quality.
"""
        return desc
    
    def write_bullets(self, product: dict) -> list[str]:
        """Write bullet points for listing."""
        name = product.get("name", "Product")
        return [
            f"Premium {name} — quality at an affordable price",
            "Durable materials built to last",
            "Perfect for gifts, home, and everyday use",
            "Ships with tracking — know where your order is",
            "Satisfaction guaranteed or your money back",
        ]
    
    def write_listing(self, product: dict) -> dict:
        """Write full listing for a product."""
        self.log(f"Writing listing for: {product.get('name')}")
        
        title = self.write_title(product.get("name", ""), product.get("category", ""))
        description = self.write_description(product)
        bullets = self.write_bullets(product)
        
        return {
            "title": title,
            "description": description,
            "bullets": bullets,
            "price": product.get("retail_price", 0),
            "category": product.get("category", ""),
        }
    
    def run(self, product: dict) -> dict:
        """Run Scribe on a product."""
        listing = self.write_listing(product)
        return {
            "agent": "Scribe",
            "product": product.get("name"),
            "listing": listing,
        }
