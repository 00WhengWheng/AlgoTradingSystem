# API Documentation

## Overview
This document describes the RESTful APIs available in the algorithmic trading system for managing data, strategies, and trading operations.

---

## Authentication
All API endpoints require authentication using API tokens. Include the token in the `Authorization` header:


---

Authorization: Bearer

### Endpoints

#### 1. Market Data
- **GET `/api/market_data`**
  - **Parameters:**
    - `symbol`: Trading symbol (e.g., `AAPL`).
    - `from_date`: Start date for data (ISO 8601).
    - `to_date`: End date for data (ISO 8601).
  - **Response Example:**
    ```json
    {
      "symbol": "AAPL",
      "data": [
        {"date_time": "2024-11-01T10:00:00Z", "open": 150.0, "close": 155.0}
      ]
    }
    ```

#### 2. Strategy Management
- **POST `/api/strategies`**
  - **Request Example:**
    ```yaml
    name: Momentum Trading
    description: Tracks price momentum to generate signals.
    risk_limit: 5.0
    ```
