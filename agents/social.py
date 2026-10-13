# Social - Social Media Poster Agent
# Drafts Facebook, Instagram posts

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents import BaseAgent
import config

class Social(BaseAgent):
    def __init__(self):
        super().__init__("Social")
    
    def facebook_post(self, product: dict) -> str:
        """Draft Facebook post for product."""
        name = product.get("name", "Product")
        price = product.get("retail_price", 0)
        category = product.get("category", "")
        
        post = f"""🎉 NEW ARRIVAL at Lassy General Store! 🎉

✨ {name} — Only ${price}!

Perfect for {category.lower()} and everyday use. Quality you can afford!

🛒 Shop now: {config.STORE_URL}
📱 Link in bio for more deals!

#LassyGeneralStore #AffordableQuality #{category.replace(' ', '')} #ShopSmall #ForEveryone
"""
        return post
    
    def instagram_caption(self, product: dict) -> str:
        """Draft Instagram caption."""
        name = product.get("name", "Product")
        price = product.get("retail_price", 0)
        category = product.get("category", "")
        
        caption = f"""✨ {name} ✨

Only ${price} — Quality for everyone! 💯

Perfect for {category.lower()} 🎁

👉 Link in bio to shop!
❤️ Like if you love it
💬 Comment your thoughts
📤 Share with a friend who needs this!

#lassygeneralstore #affordable #quality #{category.lower().replace(' ', '')} #shoplocal #forpoorpeople #by poorpeople
"""
        return caption
    
    def post_schedule(self) -> list[str]:
        """Suggest best posting times."""
        return [
            "Best times: 9 AM, 12 PM, 6 PM, 8 PM (your timezone)",
            "Post 1-2x per day for best engagement",
            "Weekends: 10 AM and 7 PM work best",
            "Stories: Post in morning and evening",
        ]
    
    def run(self, product: dict) -> dict:
        """Run Social agent on a product."""
        self.log(f"Drafting social posts for: {product.get('name')}")
        return {
            "agent": "Social",
            "product": product.get("name"),
            "facebook_post": self.facebook_post(product),
            "instagram_caption": self.instagram_caption(product),
            "schedule_tips": self.post_schedule(),
        }
