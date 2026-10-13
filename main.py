#!/usr/bin/env python3
"""
Lassy LLC Hyper Agents - Main CLI
7 Hyper AI Agents for an Empire | Built by Roger

Usage:
  python main.py --agent scout --topic "Halloween"
  python main.py --agent scribe --product "Pumpkin Lantern"
  python main.py --pipeline --topic "Christmas"
  python main.py --agent support --question "When will my order arrive?"
"""

import argparse
import json
import sys
import os

from orchestrator import Orchestrator
from agents.scout import Scout
from agents.scribe import Scribe
from agents.ledger import Ledger
from agents.beacon import Beacon
from agents.video import Video
from agents.social import Social
from agents.support import Support

def main():
    parser = argparse.ArgumentParser(description="Lassy LLC Hyper Agents - 7 AI Agents for an Empire")
    parser.add_argument("--agent", choices=["scout", "scribe", "ledger", "beacon", "video", "social", "support", "all"],
                        help="Which agent to run")
    parser.add_argument("--topic", default="", help="Product topic to research")
    parser.add_argument("--category", default="", help="Product category")
    parser.add_argument("--product", default="", help="Product name (for scribe/beacon/video/social)")
    parser.add_argument("--question", default="", help="Customer question (for support)")
    parser.add_argument("--pipeline", action="store_true", help="Run full pipeline")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    orch = Orchestrator()
    
    # Full pipeline
    if args.pipeline or args.agent == "all":
        result = orch.pipeline(args.topic, args.category)
        if args.json:
            print(json.dumps(result, indent=2, default=str))
        return
    
    # Single agent
    result = None
    
    if args.agent == "scout":
        result = orch.scout.run(args.topic, args.category)
    
    elif args.agent == "scribe":
        product = {"name": args.product or "Sample Product", "category": args.category, "retail_price": 19.99}
        result = orch.scribe.run(product)
    
    elif args.agent == "ledger":
        result = orch.ledger.run()
    
    elif args.agent == "beacon":
        product = {"name": args.product or "Sample Product", "category": args.category}
        listing = orch.scribe.run(product)["listing"]
        result = orch.beacon.run(listing, product)
    
    elif args.agent == "video":
        product = {"name": args.product or "Sample Product", "category": args.category, "retail_price": 19.99}
        result = orch.video.run(product)
    
    elif args.agent == "social":
        product = {"name": args.product or "Sample Product", "category": args.category, "retail_price": 19.99}
        result = orch.social.run(product)
    
    elif args.agent == "support":
        question = args.question or "When will my order arrive?"
        result = orch.support.run(question)
    
    else:
        parser.print_help()
        print("\nExample:")
        print('  python main.py --agent scout --topic "Halloween"')
        print('  python main.py --pipeline --topic "Christmas"')
        return
    
    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        # Pretty print
        print(f"\n--- {result.get('agent', 'Result')} ---")
        for key, val in result.items():
            if key == "agent":
                continue
            if isinstance(val, (dict, list)):
                print(f"{key}:")
                print(json.dumps(val, indent=2, default=str)[:2000])
            else:
                print(f"{key}: {val}")

if __name__ == "__main__":
    main()
