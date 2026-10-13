# Support - Customer Support Agent
# Answers questions, handles orders

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents import BaseAgent
import config

# FAQ database
FAQ = {
    "shipping": "We ship from our supplier warehouse. Delivery takes 5-11 business days for most items. You'll get tracking once your order ships!",
    "returns": "Not happy? Contact us within 30 days and we'll make it right. Email us at rogersy@lassygeneralstore.com",
    "tracking": "Your tracking number is sent by email once your order ships. Check your inbox (and spam folder) for the tracking link.",
    "payment": "We accept all major credit cards, PayPal, and Shop Pay. Your payment is secure.",
    "discount": "We offer affordable prices every day. Follow us on Facebook and Instagram for special deals!",
    "contact": f"Reach us at {config.STORE_EMAIL} or call {config.STORE_PHONE}. We're here to help!",
}

class Support(BaseAgent):
    def __init__(self):
        super().__init__("Support")
    
    def answer_question(self, question: str) -> str:
        """Answer a customer question based on FAQ."""
        q_lower = question.lower()
        
        # Match keywords
        for key, answer in FAQ.items():
            if key in q_lower:
                return answer
        
        # Shipping-related
        if any(w in q_lower for w in ["ship", "deliver", "arrive", "when", "long"]):
            return FAQ["shipping"]
        if any(w in q_lower for w in ["return", "refund", "exchange"]):
            return FAQ["returns"]
        if any(w in q_lower for w in ["track", "where is", "status"]):
            return FAQ["tracking"]
        if any(w in q_lower for w in ["pay", "card", "payment"]):
            return FAQ["payment"]
        
        # Default
        return f"Thanks for your question! For help with '{question}', please email us at {config.STORE_EMAIL} and we'll get back to you within 24 hours."
    
    def draft_reply(self, customer_msg: str, tone: str = "friendly") -> str:
        """Draft a support reply."""
        answer = self.answer_question(customer_msg)
        reply = f"""Hi there! 👋

Thanks for reaching out to Lassy General Store!

{answer}

Is there anything else I can help you with? We're happy to assist!

Best,
Lassy General Store Team
"""
        return reply
    
    def run(self, question: str) -> dict:
        """Run Support agent on a question."""
        self.log(f"Answering: {question[:50]}...")
        reply = self.draft_reply(question)
        return {
            "agent": "Support",
            "question": question,
            "answer": reply,
        }
