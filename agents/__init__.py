# Lassy LLC Hyper Agents
# Agent base class

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

class BaseAgent:
    """Base class for all Lassy Hyper Agents."""
    
    def __init__(self, name: str):
        self.name = name
        self.demo_mode = config.DEMO_MODE
    
    def log(self, msg: str):
        print(f"[{self.name}] {msg}")
    
    def save_output(self, filename: str, content: str) -> str:
        """Save output to output/ folder. Returns path."""
        os.makedirs(config.OUTPUT_DIR, exist_ok=True)
        path = os.path.join(config.OUTPUT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path
