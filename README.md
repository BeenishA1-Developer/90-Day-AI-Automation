# 🚀 90-Day AI Automation Journey — Progress Tracker

| Day | Project / Concept | Status |
| :--- | :--- | :---: |
| **Day 1** | Variables & Setup | ✅ |
| **Day 2** | Mini Calculator | ✅ |
| **Day 3** | Grade System | ✅ |
| **Day 4** | Number Guessing Game | ✅ |
| **Day 5** | Calculator with Functions | ✅ |
| **Day 6** | Student Management System | ✅ |
| **Day 7** | README + Week 1 Revision | ✅ |
| **Day 8** | Notes App - File Handling | ✅ |
| **Day 9** | Secure Calculator - Exception Handling | ✅ |
| **Day 10** | Random Password Generator | ✅ |
| **Day 11** | Weather Check App - `requests` Library | ✅ |
| **Day 12** | JSON Data Handler | ✅ |
| **Day 13** | Expense Tracker | ✅ |
| **Day 14** | Week 2 Revision + Code Cleanup | ✅ |
| **Day 15** | Public API Integration (Random Joke Fetcher) | ✅ |
| **Day 16** | Advanced JSON Filtering & Data Validation | ✅ |
| **Day 17** | PUT, DELETE Requests & Nested JSON Parsing | ✅ |
| **Day 18** | First OpenAI API Integration | ✅ |
| **Day 19** | Combining Multiple APIs - Daily Digest | ✅ |
| **Day 20** | OpenAI + Public API Combined | ✅ |
| **Day 21** | Nested JSON Deep Parsing Practice | ✅ |
| **Day 22** | FastAPI Basics (root + dynamic routes) | ✅ |
| **Day 23** | FastAPI: Query Parameters & Request Body (Pydantic) | ✅ |
| **Day 24** | FastAPI: Error Handling (`HTTPException`) & Virtual Environment Setup | ✅ |
| **Day 25** | FastAPI: Path Operations Order & Multi-Route Resolution | ✅ |
| **Day 26** | FastAPI: Path Parameter Type Validation | ✅ |
| **Day 27** | Mini Inventory API (Week 4 Wrap-Up) | ✅ |
| **Day 28** | Deploy FastAPI to Vercel | ✅ |
| **Day 29** | Connect FastAPI to n8n | ✅ |
| **Day 30** | Google Sheets Integration & Data Upsert Logic | ✅ |
| **Day 31** | Live API Automation with Webhook Trigger | ✅ |
| **Day 32** | Production Webhook & Error Handling (n8n) | ✅ |
| **Day 33** | Email Notification Automation (n8n) | ✅ |
| **Day 34** | Scheduled Trigger & Cron Automation (n8n) | ✅ |
| **Day 35** | Live Webhook-Based Telegram Inventory Agent (n8n) | ✅ |
| **Day 36** | Production AI Inventory Agent with OpenRouter & Fallbacks | ✅ |
| **Day 37** | Enterprise AI Inventory Assistant - Live Portfolio Demo | ✅ |

---

### 📝 Day 15: Public API Integration
* **Concept:** Learnt how to fetch live data from a public API using the `requests` library.
* **Error Handling:** Implemented network-level validation using `try-except` blocks to handle connection dropouts.
* **Data Parsing:** Handled JSON string conversion to Python dictionaries to access nested keys safely.

### 📝 Day 16: Advanced JSON Filtering & Data Validation
* **Concept:** Filtered and parsed complex local JSON structures (`students.json`) to find students scoring below specific thresholds.
* **File Handling:** Read student profiles dynamically and extracted data using strict functional constraints.

### 📝 Day 17: PUT, DELETE Requests & Nested JSON Parsing
* **Concept:** Successfully implemented HTTP PUT and DELETE requests using jsonplaceholder API via `requests.put()` and `requests.delete()`.
* **Data Parsing:** Practiced nested JSON parsing using clean static dictionary structures inside `nested_json_practice()` to safely extract multi-level data without crashing the program.

### 📝 Day 18: OpenAI API Integration
* **Concept:** Integrated OpenRouter API using the standard OpenAI Python client library.
* **Security:** Managed API keys securely using a `.env` file and handled environment variables with `python-dotenv`.
* **Git Safety:** Configured `.gitignore` to prevent sensitive API credentials from being tracked.

### 📝 Day 19: Combining Multiple APIs (Daily Digest)
* **Concept:** Developed a workflow that combines data from two independent public API endpoints (`adviceslip` and `official-joke-api`).
* **Data Flow:** Handled JSON data extraction and streamlined multiple asynchronous network responses into a unified console interface.

### 📝 Day 20: OpenAI + Public API Combined
* **Concept:** Connected a third-party data endpoint directly to an LLM provider to process live inputs dynamically.
* **Data Pipeline:** Extracted text from a public endpoint and passed it contextually into a secure AI client to generate optimized developer insights.

### 📝 Day 21: Nested JSON Deep Parsing Practice
* **Concept:** Mastered multi-level nested dictionary handling and object schema extraction.
* **Safe Navigation:** Implemented `.get()` nesting chains with custom defaults to guarantee crash-free fallback management in data tracking.

### 📝 Day 22: FastAPI Basics
* **Concept:** Created the first live web backend environment using FastAPI and production Uvicorn runners.
* **Routing:** Successfully deployed a clean root handler (`/`) alongside dynamic URL path parameters (`/greet/{name}`) verified via Swagger UI (`/docs`).

### 📝 Day 23: FastAPI: Query Parameters & Request Body
* **Concept:** Explored advanced routing mechanics by handling dynamic query strings and schema-structured JSON payloads.
* **Data Validation:** Utilized Pydantic's `BaseModel` to strictly validate incoming request body objects (`/products`), alongside managing custom default states inside dynamic queries (`/search`).

### 📝 Day 24: FastAPI Error Handling & Virtual Environment
* **Concept:** Configured an isolated python framework scope using `venv` to prevent interpreter path confusion permanently.
* **Error Handling:** Mastered industrial API standard error dispatching by raising proper `HTTPException(status_code=404)` handlers to securely catch missing records during route lookups.

### 📝 Day 25: FastAPI Path Operations Order & Multi-Route Resolution
* **Concept:** Explored FastAPI's top-down matching mechanism for URL path layouts.
* **Path Ordering:** Discovered that placing dynamic routes (`/products/{product_id}`) above static routes (`/products/featured`) captures static keywords incorrectly as variables, creating a tracking mismatch. Resolved this routing bug successfully by prioritizing exact static endpoints at the top of the execution block.

### 📝 Day 26: FastAPI: Path Parameter Type Validation
* **Concept:** Explored FastAPI's automatic data validation using standard Python type hinting (`item_id: int`).
* **Type Validation:** Verified that sending a valid integer (`/items/5`) executes correctly, while sending an invalid type like text (`/items/abc`) triggers an automatic `422 Unprocessable Entity` response.
* **Mechanism:** Learnt that FastAPI leverages Pydantic internally to parse and validate incoming data before it even hits the core path function, removing the need for manual validation checks.

### 📝 Week 4 Summary & Core Framework Wrap-Up
This week, I transitioned into backend development using FastAPI. I learned the basics of routing, handling parameters, and managing incoming request data securely. I practiced structural rules like endpoint ordering to avoid bugs, implemented data validation using Pydantic, and created proper custom error handling using status codes. Everything was brought together into a fully functional Mini Inventory system.

### 📝 Day 27: Mini Inventory API (Week 4 Wrap-Up)
* **Concept:** Combined all backend concepts from Week 4 into one single functional inventory microservice file.
* **Implementation:** Built four paths: getting all items, fetching a single item by its numeric identity, adding a new item, and checking structure validity.
* **Error Handling:** Used a standard loop logic that automatically triggers an explicit `HTTPException(status_code=404)` message immediately if a user requests a product ID that does not exist inside our system data array.

## 📝 Day 28: Deploy FastAPI to Vercel
* **Concept:** Learned how to deploy a local FastAPI project to the live internet for a portfolio.
* **Implementation:** Created a simple `vercel.json` configuration file, connected the GitHub repository to Vercel, and successfully deployed the backend for free.
* **Live API Link:** [https://90-day-ai-automation.vercel.app/docs](https://90-day-ai-automation.vercel.app/docs)

### 📝 Day 29: Connect FastAPI to n8n Workflow
* **Concept:** Transitioned to Month 2 automation concepts by linking custom backend infrastructure directly to an enterprise automation platform.
* **Implementation:** Configured a manual execution sequence inside n8n, mapped an HTTP Request node using the `GET` method to point directly to the live Vercel inventory endpoint, and verified data parsing.
* **Result:** Successfully fetched the live inventory dictionary structure (`Laptop`, `Mouse`, `Keyboard`) directly into the n8n node canvas output panel.

### 📝 Day 30: Google Sheets Integration & Data Upsert Logic
* **Concept:** Modeled database synchronization workflows by streaming external API responses into spreadsheets.
* **Implementation:** Connected Google Sheets OAuth2 credentials into n8n and utilized the **Append or Update Row** operation.
* **Data Structuring:** Configured exact data key mapping (`id`, `name`, `price`, `stock`) and set `Id` as the unique matching key constraint. This structural logic creates an industrial upsert mechanism, preventing row duplication by cleanly updating existing stocks if the items run again.

### 📝 Day 31: Live API Automation with Webhook Trigger
* **Concept:** Converted the manual testing layout into a completely hands-free, event-driven production pipeline.
* **Implementation:** Swapped manual node executors with a native **Webhook Trigger** (GET method) capable of running background jobs autonomously via incoming network hits.
* **Data Processing:** Implemented a **Split Out** node autonomously between the HTTP caller and the database writer. Because incoming API payloads stream down inside a packed singular array, splitting out the main data key breaks down the object structure into clean individual items. This optimization handles iterative workflows flawlessly, sending unique item payloads directly to Google Sheets rows automatically.

### 📝 Day 32: Production Webhook & Error Handling (n8n)
* **Concept:** Transitioned from development mode to fully operational production infrastructure by understanding the critical difference between Test URLs and Production URLs. Learnt that production webhooks run 24/7 as a background daemon without needing the n8n editor active.
* **Production Deployment:** Successfully flipped the workflow execution state to **Active/Published**. Captured the dynamic production web gateway routing (`/webhook/` injection format) and verified remote triggering with the editor panel closed.
* **Error Infrastructure (Fail-Safe):** Architected a dedicated downstream global **Error Trigger Workflow** named `Error_Workflow`. Configured the core workflow properties to automatically reroute network timeouts, API drops, or execution faults into this error handler to log diagnostic data safely inside Google Sheets, eliminating silent crashes.

### 📝 Day 33: Email Notification Automation & Conditional Logic (n8n)
* **Concept:** Transitioned the automation system from a static data pipe to an intelligent, decision-making production layout by exploring n8n's conditional branching (`IF` Node).
* **Logical Branching:** Implemented a data evaluation gate immediately following the `Split Out` array extraction layer. Configured a dynamic numerical comparison check to trap item inventory state where `stock` is **Less Than 15**.
* **Alert Infrastructure:** Integrated a live **Gmail API / SMTP Node** downstream on the `true` logical outcome path. Designed an autonomous multi-variable email notification payload that dynamically fires custom real-time alert vectors directly to the ops team when stock thresholds drop, leaving the `false` data to process cleanly without triggering notifications.

### 📝 Day 34: Scheduled Trigger & Cron-Based Automation (n8n)
* **Concept:** Advanced from event-driven (reactive) webhooks to time-based (proactive) scheduled background automation handlers.
* **Proactive Scheduling:** Replaced the external network gateway dependency with a native **Schedule Trigger** core module. Configured an iterative minute-based heartbeat interval to drive background execution sweeps entirely hands-free.
* **Architecture Integration:** Linked the system directly into the decoupled multi-node inventory processing block (`HTTP Request` ➡️ `Split Out` ➡️ `IF` Gate ➡️ `Gmail Alert`). Verified stable logical evaluation routines and dynamic payload delivery without relying on inbound external network calls.

### 📝 Day 35: Live Webhook-Based Telegram Inventory Agent (n8n)
* **Concept:** Transitioned from manual testing triggers to a fully production-ready, inbound event-driven Telegram Bot powered by webhooks.
* **Architecture and Flow Correction:** Resolved cross-wiring bugs by cleanly organizing the workflow pipeline: `Telegram Trigger` (Webhook) ➔ `Get row(s) in sheet` (Database Search) ➔ `Send a text message` (Response). This ensures proper sequence execution from the inbound query to database retrieval, ending with the automated outbound message.
* **Dynamic Database Filters:** Configured n8n's Google Sheets filter to dynamically lookup product fields using incoming Telegram text variables: `{{ $('Telegram Trigger').item.json.message.text }}`.
* **Production Deployment:** Turned the workflow status to **Active/Published**. Verified that sending a message like `Mobile` or `Laptop` directly on Telegram triggers the background webhook, fetches live prices/stocks from Google Sheets, and replies automatically in seconds without manual execution inside the editor.

### 📝 Day 36: Production AI Inventory Agent with OpenRouter & Fallbacks
* **Concept:** Advanced the Telegram agent from a basic database lookup tool into a highly conversational, production-grade AI support assistant powered by n8n Advanced AI and OpenRouter.
* **Architecture Integration:** Rebuilt the workflow layout to properly route live data via an advanced AI agent structure: `Telegram Trigger` ➔ `Get Inventory (Sheets)` ➔ `Combine Inventory` ➔ `Inventory Assistant` (AI Agent using OpenRouter Chat Model Node) ➔ `Send Reply`.
* **Cost-Effective LLM Infrastructure:** Integrated OpenRouter as an API aggregator to leverage the permanent free-tier `meta-llama/llama-3.3-70b-instruct:free` model. This structural shift allows for unlimited commercial production queries with a $0-cost balance constraint, bypassing time-limited developer credits.
* **Strict AI Grounding & Safe Fallbacks:** Engineered rigorous system prompts injection to eliminate AI model hallucinations. Grounded the model directly on live sheets data arrays `{{ $('Get Inventory').item.json }}` so that queries for out-of-stock or unlisted items (e.g., "USB") trigger intelligent, custom polite excuses in natural Roman Urdu instead of generating fake prices.
* **Production Stabilization:** Deployed the workflow directly to production, verifying a clean conversational matching layout for natural-language customer operations.

### 📝 Day 37: Enterprise AI Inventory Assistant - Live Portfolio Demo
* **Concept:** Created a complete system walkthrough and deployment documentation for a production-grade automation ecosystem to showcase as a main portfolio milestone.
* **System Video Walkthrough:** 
  > 🔗 **[Watch the Live System Walkthrough & Demo Here](https://drive.google.com/file/d/1XzW5Gz9jW_vB9T78hM76p2aQ5XmK3W_V/view?usp=sharing)**
* **Architecture Stack:** Telegram Bot API ➔ Webhook Trigger ➔ n8n Advanced AI Agent ➔ OpenRouter Gateway (`Llama-3.3-70b`) ➔ Google Sheets DB Sync.
* **Production Engineering:** Documented strict prompt injection frameworks to remove LLM hallucinations, integrated automated zero-match safe fallbacks for unlisted stock queries, and verified single-response delivery per query during manual testing.