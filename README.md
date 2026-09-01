
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

## Roadmap & Implementation Progress

<details>
<summary><b>Phase 1: Architecture & Local Dev Environment Setup</b></summary>

- [x] Initialize monorepo project structure
- [x] Setup Python 3.12+ backend workspace with `uv` package manager and `ruff` linter/formatter
- [x] Setup React 19 frontend workspace with `bun` package manager and `biome` linter
- [x] Create `docker-compose.yml` for local infrastructure:
  - [x] PostgreSQL 16 (Relational state & window analytics)
  - [x] Elasticsearch 8 (Full-text log index & payload search)
  - [x] Redis (Caching, session state, & task rate limiting)
  - [ ] gRPC dependencies & local protocol buffers generation environment
- [ ] Verify connectivity and health checks across all containerized services

</details>

<details>
<summary><b>Phase 2: Database Schemas, Indexing Strategy & Domain Modeling (DDD)</b></summary>

- [ ] **PostgreSQL Setup:**
  - [ ] Configure async database drivers (`asyncpg`) and `Alembic` migrations
  - [ ] Design DDD domain entities: `User`, `AuditLog`, `SecurityRule`, `IncidentCase`, `Session`
  - [ ] Implement optimized B-Tree and GIN indexes for timestamp ranges and JSONB payload searching
- [ ] **Elasticsearch Mapping:**
  - [ ] Define index mappings and analyzers for unstructured system log payloads
  - [ ] Set up index lifecycle management (ILM) for log retention and rotation

</details>

<details>
<summary><b>Phase 3: High-Volume Log Engine & Anomaly Seed Strategy</b></summary>

- [ ] Create synthetic system log generator engine using Python
- [ ] Implement realistic user activity simulation (IP addresses, auth attempts, data exports)
- [ ] Seed PostgreSQL & Elasticsearch with 100,000+ realistic system audit logs
- [ ] Inject pre-seeded insider threat and fraud patterns:
  - [ ] *Privilege escalation and unauthorized admin calls*
  - [ ] *Mass sensitive data extraction outside business hours*
  - [ ] *Impossible travel / Anomaly session hijack patterns*
  - [ ] *Rapid consecutive failed login bursts*
- [ ] Configure gRPC log-ingestion stream service for high-throughput entry intake

</details>

<details>
<summary><b>Phase 4: Backend Core Development (Python 3.12 / Litestar / gRPC)</b></summary>

- [ ] Implement Domain-Driven Design (DDD) layers:
  - [ ] `domain/` (Entities, value objects, repository interfaces)
  - [ ] `infrastructure/` (Postgres, Elasticsearch, Redis, gRPC clients)
  - [ ] `application/` (Behavioral anomaly algorithms, window function aggregators)
  - [ ] `presentation/` (Litestar REST API & gRPC endpoints)
- [ ] Write complex SQL window functions (`ROW_NUMBER()`, `LAG()`, `LEAD()`) for time-series anomaly detection
- [ ] Build key REST endpoints:
  - [ ] `GET /api/v1/audit-logs` (Paginated, indexed relational log lookup)
  - [ ] `POST /api/v1/search/logs` (Elasticsearch full-text log payload search)
  - [ ] `GET /api/v1/analytics/anomalies` (Aggregated behavioral metrics)
- [ ] Setup background task execution (Celery / Taskiq) for real-time alert triggers
- [ ] Add unit and integration tests using `pytest-asyncio`

</details>

<details>
<summary><b>Phase 5: Frontend Core Development (React 19 / FSD Architecture)</b></summary>

- [ ] Setup Feature-Sliced Design folder structure (`app`, `pages`, `widgets`, `features`, `entities`, `shared`)
- [ ] Setup global state (`Zustand`) and server cache layer (`TanStack Query`)
- [ ] **Module 1: Virtualized Log Explorer**
  - [ ] Implement high-performance client-side virtualized table using `TanStack Table`
  - [ ] Ensure 60 FPS scrolling capabilities for 50,000+ log entries
  - [ ] Add dynamic column filtering, sorting, and JSON payload inspector drawer
- [ ] **Module 2: Rule Builder Interface**
  - [ ] Build dynamic threshold rule generator using `react-hook-form` and `zod`
  - [ ] Create visual alert condition configurator for security admins
- [ ] **Module 3: Security Analytics & Anomaly Dashboard**
  - [ ] Build behavioral trend visualizers and risk score indicators
  - [ ] Connect real-time alert notifications for flagged insider threats

</details>

<details>
<summary><b>Phase 6: CI/CD, DevOps & Final Polish</b></summary>

- [ ] Setup `.github/workflows/ci.yml` (`ruff`, `pytest`, `biome check`, and type checks)
- [ ] Write optimized multi-stage `Dockerfile` for frontend and backend services
- [ ] **Documentation & Benchmarks:**
  - [ ] Document gRPC protobuf definitions and API specifications
  - [ ] Benchmark virtualized frontend rendering and PostgreSQL window query execution times
  - [ ] Record demo showcasing real-time log ingestion, search filtering, and anomaly detection

</details>

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
