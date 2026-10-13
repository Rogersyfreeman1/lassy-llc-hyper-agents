# Orchestrator - Coordinates all 7 Hyper Agents

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from agents.scout import Scout
from agents.scribe import Scribe
from agents.ledger import Ledger
from agents.beacon import Beacon
from agents.video import Video
from agents.social import Social
from agents.support import Support

class Orchestrator:
    """Coordinates all 7 Lassy Hyper Agents in a pipeline."""
    
    def __init__(self):
        self.scout = Scout()
        self.scribe = Scribe()
        self.ledger = Ledger()
        self.beacon = Beacon()
        self.video = Video()
        self.social = Social()
        self.support = Support()
    
    def pipeline(self, topic: str = "", category: str = "") -> dict:
        """Run full pipeline: Scout → Scribe → Beacon → Video → Social → Ledger."""
        print(f"\n{'='*60}")
        print(f"🚀 LASSY HYPER AGENTS — Full Pipeline")
        print(f"   Topic: {topic or 'All'} | Category: {category or 'All'}")
        print(f"{'='*60}\n")
        
        results = {}
        
        # Step 1: Scout finds products
        print("📍 Step 1: Scout — Product Research")
        scout_result = self.scout.run(topic, category)
        results["scout"] = scout_result
        candidates = scout_result["candidates"]
        
        if not candidates:
            print("  No candidates found. Try a different topic.")
            return results
        
        # Step 2-5: For each candidate, run Scribe, Beacon, Video, Social
        listings = []
        for i, prod in enumerate(candidates[:3]):  # Top 3 for demo
            print(f"\n📍 Step 2-5: Processing '{prod['name']}'")
            
            scribe_result = self.scribe.run(prod)
            listings.append(scribe_result)
            
            beacon_result = self.beacon.run(scribe_result["listing"], prod)
            video_result = self.video.run(prod)
            social_result = self.social.run(prod)
            
            results[f"product_{i+1}"] = {
                "product": prod,
                "listing": scribe_result["listing"],
                "seo": beacon_result,
                "video": video_result,
                "social": social_result,
            }
        
        # Step 6: Ledger audit
        print(f"\n📍 Step 6: Ledger — Inventory Audit")
        ledger_result = self.ledger.run()
        results["ledger"] = ledger_result
        
        print(f"\n{'='*60}")
        print(f"✅ Pipeline complete! {len(candidates)} candidates, {len(listings)} listings.")
        print(f"{'='*60}\n")
        
        return results

def main():
    orch = Orchestrator()
    import argparse
    p = argparse.ArgumentParser(description="Lassy Hyper Agents Orchestrator")
    p.add_argument("--topic", default="", help="Product topic")
    p.add_argument("--category", default="", help="Product category")
    args = p.parse_args()
    orch.pipeline(args.topic, args.category)

if __name__ == "__main__":
    main()
