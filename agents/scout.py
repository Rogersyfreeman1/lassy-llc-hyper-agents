# Scout - Product Research Agent
# Finds trending products, checks CJ, calculates profit

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents import BaseAgent
import config

# Demo product database (used when no CJ API key)
DEMO_PRODUCTS = [
    {"name": "Halloween Pumpkin LED Lantern", "cj_price": 8.50, "shipping": 5.05, "stock": 150630, "category": "Halloween", "warehouse": "China"},
    {"name": "LED Willow Vine String Lights", "cj_price": 12.00, "shipping": 10.15, "stock": 38038, "category": "Halloween", "warehouse": "China"},
    {"name": "Christmas Stockings 4-Pack", "cj_price": 6.20, "shipping": 4.50, "stock": 85000, "category": "Christmas", "warehouse": "China"},
    {"name": "Thermal Underwear Set", "cj_price": 9.80, "shipping": 5.00, "stock": 120000, "category": "Winter", "warehouse": "China"},
    {"name": "Bamboo Charcuterie Board", "cj_price": 11.50, "shipping": 6.00, "stock": 45000, "category": "Kitchen", "warehouse": "China"},
    {"name": "Fleece-Lined Leggings", "cj_price": 7.30, "shipping": 4.80, "stock": 95000, "category": "Winter", "warehouse": "China"},
    {"name": "Window Insulation Film Kit", "cj_price": 5.60, "shipping": 3.90, "stock": 67000, "category": "Home", "warehouse": "China"},
    {"name": "Silicone Baking Molds Set", "cj_price": 4.20, "shipping": 3.50, "stock": 78000, "category": "Kitchen", "warehouse": "China"},
]

class Scout(BaseAgent):
    def __init__(self):
        super().__init__("Scout")
    
    def check_hard_rules(self, product: dict) -> tuple[bool, str]:
        """Check if product passes Roger's hard rules. Returns (pass, reason)."""
        name_lower = product.get("name", "").lower()
        for banned in config.BANNED_KEYWORDS:
            if banned in name_lower:
                return False, f"Contains banned keyword: {banned}"
        for banned in config.BANNED_CATEGORIES:
            if banned in name_lower:
                return False, f"Banned category: {banned}"
        if product.get("stock", 0) < 1000:
            return False, f"Low stock: {product.get('stock')}"
        return True, "Pass"
    
    def calculate_profit(self, cj_price: float, shipping: float, retail_price: float) -> float:
        """Calculate profit: retail - (CJ price + shipping)."""
        landed = cj_price + shipping
        return round(retail_price - landed, 2)
    
    def suggest_retail_price(self, cj_price: float, shipping: float) -> float:
        """Suggest retail price for at least $5 profit, rounded to .99."""
        landed = cj_price + shipping
        target = landed + config.MIN_PROFIT + 2.00  # $5 floor + $2 buffer
        # Round up to nearest .99
        import math
        price = math.ceil(target) - 0.01
        return round(price, 2)
    
    def research(self, topic: str = "", category: str = "", limit: int = 10) -> list[dict]:
        """Research products. Returns list of vetted candidates."""
        self.log(f"Researching products: topic='{topic}' category='{category}'")
        
        candidates = []
        for prod in DEMO_PRODUCTS:
            # Filter by topic/category
            if topic and topic.lower() not in prod["name"].lower() and topic.lower() not in prod["category"].lower():
                continue
            if category and category.lower() not in prod["category"].lower():
                continue
            
            # Hard rules check
            passes, reason = self.check_hard_rules(prod)
            if not passes:
                self.log(f"  REJECTED: {prod['name']} - {reason}")
                continue
            
            # Price and profit
            retail = self.suggest_retail_price(prod["cj_price"], prod["shipping"])
            profit = self.calculate_profit(prod["cj_price"], prod["shipping"], retail)
            
            if profit < config.MIN_PROFIT:
                self.log(f"  REJECTED: {prod['name']} - Profit ${profit} < ${config.MIN_PROFIT}")
                continue
            
            candidates.append({
                "name": prod["name"],
                "category": prod["category"],
                "cj_price": prod["cj_price"],
                "shipping": prod["shipping"],
                "landed_cost": round(prod["cj_price"] + prod["shipping"], 2),
                "retail_price": retail,
                "profit": profit,
                "stock": prod["stock"],
                "warehouse": prod["warehouse"],
            })
            self.log(f"  FOUND: {prod['name']} - Retail ${retail}, Profit ${profit}, Stock {prod['stock']}")
        
        return candidates[:limit]
    
    def run(self, topic: str = "", category: str = "") -> dict:
        """Run Scout agent. Returns results dict."""
        candidates = self.research(topic, category)
        return {
            "agent": "Scout",
            "topic": topic,
            "candidates_found": len(candidates),
            "candidates": candidates,
        }
