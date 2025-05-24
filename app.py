from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
import math

app = FastAPI(title="Customer Engagement Scoring API")

class CustomerProfile(BaseModel):
    age: int
    avg_purchase_value: float
    engagement_rate: float  # e.g., open/click rates
    is_subscribed: bool

@app.get("/")
def read_root():
    return {"message": "Welcome to the Customer Scoring API"}

@app.post("/score/")
def score_customer(profile: CustomerProfile):
    base_score = (
        profile.engagement_rate * 0.5 +
        profile.avg_purchase_value / 100 * 0.3 +
        (1 if profile.is_subscribed else 0) * 0.2
    )
    age_penalty = max(0, (60 - profile.age) / 60)
    score = round(base_score * age_penalty * 100, 2)
    return {"score": score, "tier": "High" if score > 75 else "Medium" if score > 50 else "Low"}
