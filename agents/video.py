# Video - Video Content Creator Agent
# Generates video scripts, ties into AI-Video system

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents import BaseAgent

class Video(BaseAgent):
    def __init__(self):
        super().__init__("Video")
    
    def generate_script(self, product: dict) -> str:
        """Generate video script for product."""
        name = product.get("name", "Product")
        price = product.get("retail_price", 0)
        category = product.get("category", "")
        
        script = f"""[INTRO - 0:00-0:15]
Hey everyone! Today I'm showing you the {name} — and you're going to love this one.

[FEATURES - 0:15-1:00]
This {name} is perfect for {category.lower()} and everyday use. 
It's high quality, affordable, and built to last.
At just ${price}, it's a steal for what you get.

[DEMO - 1:00-2:00]
Let me show you how it works...
[Show product in use, highlight key features]

[CTA - 2:00-2:30]
If you want one, link is in the description below.
Don't forget to like and subscribe for more great finds!
Check out Lassy General Store — where everyone can afford quality.
"""
        return script
    
    def generate_ideas(self, topic: str, count: int = 5) -> list[str]:
        """Generate video ideas for a topic."""
        ideas = [
            f"Top 5 {topic} Under $20 — Affordable Finds",
            f"{topic} Review — Is It Worth It?",
            f"Best {topic} for Gifts — Holiday Guide",
            f"{topic} Unboxing — First Impressions",
            f"How to Use {topic} — Complete Guide",
            f"{topic} vs Competitors — Honest Comparison",
            f"5 Reasons to Buy {topic} Today",
        ]
        return ideas[:count]
    
    def suggest_thumbnail(self, product: dict) -> str:
        """Suggest thumbnail text."""
        name = product.get("name", "Product")
        price = product.get("retail_price", 0)
        return f"{name} — Only ${price}! 🔥"
    
    def run(self, product: dict) -> dict:
        """Run Video agent on a product."""
        self.log(f"Generating video content for: {product.get('name')}")
        script = self.generate_script(product)
        thumbnail = self.suggest_thumbnail(product)
        return {
            "agent": "Video",
            "product": product.get("name"),
            "script": script,
            "thumbnail_text": thumbnail,
            "note": "Ties into AI-Video system: github.com/Rogersyfreeman1/AI-Video",
        }
