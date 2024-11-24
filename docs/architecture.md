# System Architecture

## Overview
The system is designed for scalability and resilience, integrating real-time data collection, strategy evaluation, and trading execution.

---

## Components

1. **Data Pipeline**
   - Collects market data using yFinance and Alpha Vantage.
   - Stores data in PostgreSQL for analysis.
   
2. **Strategy Engine**
   - Executes trading strategies and calculates signals.
   
3. **Trading Executor**
   - Sends buy/sell orders to Interactive Brokers.

---

## Diagram
```plantuml
@startuml
actor User
participant "Dashboard (Web)" as Dashboard
participant "API Gateway" as API
participant "Data Pipeline" as Pipeline
participant "Database (PostgreSQL)" as DB
participant "Broker (Interactive Brokers)" as Broker

User -> Dashboard: Manages strategies
Dashboard -> API: Sends requests
API -> Pipeline: Collects market data
Pipeline -> DB: Stores data
API -> DB: Fetches data
API -> Broker: Executes trades
@enduml


---

### **3. `setup_guide.md`**
Guida all’installazione e configurazione.

```markdown
# Setup Guide

## Prerequisites
1. **Python 3.8+**
2. **PostgreSQL**
3. **Docker and Docker Compose**
4. **API keys for Alpha Vantage and yFinance**
5. **Interactive Brokers account with API enabled**

---

## Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/algotrading.git
   cd algotrading
