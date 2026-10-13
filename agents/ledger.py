# Ledger - Inventory Auditor Agent
# Checks stock, flags zero-inventory, tracks sales

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents import BaseAgent

# Demo inventory (simulates Shopify store)
DEMO_INVENTORY = [
    {"name": "Fall Pumpkin Doormat", "status": "active", "inventory": 0, "price": 29.99},
    {"name": "Checkered Knit Throw Blanket", "status": "active", "inventory": 5, "price": 39.99},
    {"name": "Halloween Pumpkin LED Lantern", "status": "active", "inventory": 0, "price": 24.99},
    {"name": "Steampunk Plague Beak Mask", "status": "draft", "inventory": 9592, "price": 16.36},
    {"name": "Christmas Stockings 4-Pack", "status": "draft", "inventory": 0, "price": 19.99},
    {"name": "Label Printer", "status": "active", "inventory": 0, "price": 45.00},
    {"name": "CCTV Camera", "status": "active", "inventory": 0, "price": 89.99},
]

class Ledger(BaseAgent):
    def __init__(self):
        super().__init__("Ledger")
    
    def audit(self, inventory: list[dict] = None) -> dict:
        """Audit inventory. Returns flags and summary."""
        if inventory is None:
            inventory = DEMO_INVENTORY
        
        self.log("Auditing inventory...")
        
        active = [p for p in inventory if p["status"] == "active"]
        drafts = [p for p in inventory if p["status"] == "draft"]
        
        zero_inventory_live = [p for p in active if p["inventory"] == 0]
        drafts_with_inventory = [p for p in drafts if p["inventory"] > 0]
        drafts_zero_stock = [p for p in drafts if p["inventory"] == 0]
        
        self.log(f"  Active: {len(active)}, Drafts: {len(drafts)}")
        self.log(f"  Zero-inventory LIVE: {len(zero_inventory_live)} (restock or unpublish?)")
        self.log(f"  Drafts with inventory: {len(drafts_with_inventory)} (launch candidates!)")
        
        return {
            "total_products": len(inventory),
            "active_count": len(active),
            "draft_count": len(drafts),
            "zero_inventory_live": zero_inventory_live,
            "zero_inventory_live_count": len(zero_inventory_live),
            "drafts_with_inventory": drafts_with_inventory,
            "drafts_with_inventory_count": len(drafts_with_inventory),
            "drafts_zero_stock": len(drafts_zero_stock),
        }
    
    def run(self, inventory: list[dict] = None) -> dict:
        """Run Ledger audit."""
        result = self.audit(inventory)
        result["agent"] = "Ledger"
        return result
