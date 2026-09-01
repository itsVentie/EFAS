
# EFAS - Enterprise Fraud & Audit Scanner

A high-performance security auditing and behavioral anomaly detection system designed to monitor user activities, detect internal fraud risks, and analyze system event logs at scale.

Built with a focus on Clean Architecture (DDD), complex SQL analytical queries, and efficient large-dataset rendering on the frontend.

---

## Key Features

* **Behavioral Anomaly Engine:** Utilizes advanced PostgreSQL window functions (`ROW_NUMBER()`, `LAG()`, `LEAD()`) and specialized indexing to detect suspicious activity patterns.
* **High-Volume Log Explorer:** Virtualized client-side table built with `TanStack Table` capable of smoothly rendering tens of thousands of log entries without UI lag.
* **Full-Text & Analytical Search:** Integrated search engine using **Elasticsearch** for rapid log lookup across structured and unstructured payload data.
* **Rule Builder Interface:** Configurable rule management system allowing security admins to define real-time alert thresholds (e.g., unauthorized off-hours data extraction).
* **Inter-Service Communication:** Lightweight **gRPC** interfaces for high-efficiency internal service communications.

---

## Tech Stack

### Backend
* **Language & Framework:** Python 3.12+, Litestar / FastAPI
* **Architecture:** Domain-Driven Design (DDD) / Layered Architecture
* **Database & Search:** 
  * **PostgreSQL 16** (asyncpg, Alembic)
  * **Elasticsearch** (Audit log search)
  * **Redis** (Caching & session state)
* **RPC & Async Messaging:** gRPC (`grpclib`, `betterproto2`), Celery / Taskiq
* **Quality & Tooling:** `uv`, `ruff`, `pytest-asyncio`

### Frontend
* **Core:** React 19, TypeScript, Vite, Bun
* **Architecture:** Feature-Sliced Design (FSD)
* **Routing & State:** TanStack Router, TanStack Query, Zustand
* **Table & Forms:** TanStack Table (Virtualized), `react-hook-form`, `zod`
* **UI Components:** Mantine 8 / Tailwind CSS 4

---

## Architecture & Database Strategy


```

+------------------------+      +-------------------------+
|   PostgreSQL 16        |      |   Elasticsearch         |
|   - Relational Audits  |      |   - Full-text Log       |
|   - Window Functions   |      |     Payload Search      |
+-----------+------------+      +------------+------------+
^                                ^
|                                |
+---------------+----------------+
|
v
+----------------------------+
| Litestar / FastAPI Service |
| (Clean Architecture / DDD) |
+--------------+-------------+
|
| gRPC / REST
v
+----------------------------+
| React 19 Frontend (FSD)    |
| - TanStack Table Engine    |
| - Rule Builder Dashboard   |
+----------------------------+

```

---

## Key Performance Highlights

1. **Optimized Database Queries:** Includes custom migration scripts with B-Tree and GIN indexes specifically tuned for timestamp ranges and JSONB log payloads.
2. **Virtualization:** Frontend uses row virtualization to maintain 60 FPS performance while scrolling through 50,000+ audit entries.

---

## Quick Start (Docker)

```bash
# 1. Clone repository
git clone https://github.com/itsventie/efas.git
cd efas

# 2. Environment Setup
cp .env.example .env

# 3. Spin up infrastructure
docker compose up -d --build

```

### Endpoints

* **Web Application:** `http://localhost:3000`
* **OpenAPI Docs:** `http://localhost:8000/docs`

---

## Testing & Code Quality

```bash
# Run backend linters & tests
uv run ruff check .
uv run pytest

# Run frontend validation
bun run biome check .
bun run vitest

```
