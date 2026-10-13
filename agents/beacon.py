# Beacon - SEO Optimizer Agent
# Optimizes listings for search, keywords

import sys
import os
import re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents import BaseAgent

class Beacon(BaseAgent):
    def __init__(self):
        super().__init__("Beacon")
    
    def extract_keywords(self, product_name: str, category: str = "") -> list[str]:
        """Extract keywords from product name and category."""
        text = f"{product_name} {category}".lower()
        # Remove common stop words
        stop_words = {"the", "and", "for", "with", "a", "an", "of", "to", "in"}
        words = re.findall(r'\b[a-z]+\b', text)
        keywords = [w for w in words if w not in stop_words and len(w) > 2]
        # Deduplicate, preserve order
        seen = set()
        result = []
        for kw in keywords:
            if kw not in seen:
                seen.add(kw)
                result.append(kw)
        return result[:10]
    
    def generate_tags(self, product: dict) -> list[str]:
        """Generate SEO tags for product."""
        keywords = self.extract_keywords(product.get("name", ""), product.get("category", ""))
        category = product.get("category", "").lower()
        tags = keywords.copy()
        # Add category-specific tags
        if category:
            tags.append(category)
        tags.extend(["affordable", "quality", "gift", "home"])
        return tags[:15]
    
    def optimize_title(self, title: str, keywords: list[str]) -> str:
        """Optimize title for SEO (keyword-first)."""
        # Title already has keywords from name, just ensure length
        if len(title) > 70:
            title = title[:67] + "..."
        return title
    
    def seo_score(self, listing: dict) -> int:
        """Score listing SEO 0-100."""
        score = 0
        title = listing.get("title", "")
        desc = listing.get("description", "")
        bullets = listing.get("bullets", [])
        
        if 30 <= len(title) <= 70:
            score += 30
        elif len(title) > 0:
            score += 15
        if len(desc) > 200:
            score += 30
        elif len(desc) > 50:
            score += 15
        if len(bullets) >= 3:
            score += 20
        elif len(bullets) > 0:
            score += 10
        if listing.get("price", 0) > 0:
            score += 10
        if listing.get("category"):
            score += 10
        
        return min(score, 100)
    
    def optimize(self, listing: dict, product: dict) -> dict:
        """Optimize a listing for SEO."""
        self.log(f"Optimizing SEO for: {listing.get('title', '')}")
        
        keywords = self.extract_keywords(product.get("name", ""), product.get("category", ""))
        tags = self.generate_tags(product)
        opt_title = self.optimize_title(listing.get("title", ""), keywords)
        score = self.seo_score(listing)
        
        return {
            "optimized_title": opt_title,
            "keywords": keywords,
            "tags": tags,
            "seo_score": score,
            "suggestions": self._suggestions(listing, score),
        }
    
    def _suggestions(self, listing: dict, score: int) -> list[str]:
        """Generate improvement suggestions."""
        suggestions = []
        if score < 80:
            if len(listing.get("title", "")) < 30:
                suggestions.append("Title is short — add descriptive keywords")
            if len(listing.get("description", "")) < 200:
                suggestions.append("Description is short — add more benefits and details")
            if len(listing.get("bullets", [])) < 3:
                suggestions.append("Add more bullet points (aim for 5)")
        if score >= 80:
            suggestions.append("SEO looks good! Ready to publish.")
        return suggestions
    
    def run(self, listing: dict, product: dict) -> dict:
        """Run Beacon on a listing."""
        result = self.optimize(listing, product)
        result["agent"] = "Beacon"
        return result
