# Customer Engagement Scoring API

This project is a lightweight, production-ready API built with FastAPI. It accepts structured customer data and returns an engagement score and tier based on purchasing behavior, engagement metrics, and subscription status.

## Features

- Built with FastAPI
- Typed request validation using Pydantic
- Real-time scoring and tier classification
- Easily deployable via Uvicorn

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the API:
   ```bash
   uvicorn app:app --reload
   ```

3. Visit the interactive docs at:
   ```
   http://127.0.0.1:8000/docs
   ```

## Example Request

### Endpoint
POST `/score/`

### Body
```json
{
  "age": 35,
  "avg_purchase_value": 250.0,
  "engagement_rate": 0.65,
  "is_subscribed": true
}
```

### Response
```json
{
  "score": 81.5,
  "tier": "High"
}
```

This project demonstrates skills in Python API design, data modeling, scoring algorithms, and developer experience.
