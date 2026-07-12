## 🚀 90-Day AI Automation Journey — Progress Tracker

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

---

### 📝 Day 15: Public API Integration[cite: 1]
* **Concept:** Learnt how to fetch live data from a public API using the `requests` library.[cite: 1]
* **Error Handling:** Implemented network-level validation using `try-except` blocks to handle connection dropouts.[cite: 1]
* **Data Parsing:** Handled JSON string conversion to Python dictionaries to access nested keys safely.[cite: 1]

### 📝 Day 16: Advanced JSON Filtering & Data Validation[cite: 1]
* **Concept:** Filtered and parsed complex local JSON structures (`students.json`) to find students scoring below specific thresholds.[cite: 1]
* **File Handling:** Read student profiles dynamically and extracted data using strict functional constraints.[cite: 1]

### 📝 Day 17: PUT, DELETE Requests & Nested JSON Parsing[cite: 1]
* **Concept:** Successfully implemented HTTP PUT and DELETE requests using jsonplaceholder API via `requests.put()` and `requests.delete()`.[cite: 1]
* **Data Parsing:** Practiced nested JSON parsing using clean static dictionary structures inside `nested_json_practice()` to safely extract multi-level data without crashing the program.[cite: 1]

### 📝 Day 18: OpenAI API Integration[cite: 1]
* **Concept:** Integrated OpenRouter API using the standard OpenAI Python client library.[cite: 1]
* **Security:** Managed API keys securely using a `.env` file and handled environment variables with `python-dotenv`.[cite: 1]
* **Git Safety:** Configured `.gitignore` to prevent sensitive API credentials from being tracked.[cite: 1]

### 📝 Day 19: Combining Multiple APIs (Daily Digest)[cite: 1]
* **Concept:** Developed a workflow that combines data from two independent public API endpoints (`adviceslip` and `official-joke-api`).[cite: 1]
* **Data Flow:** Handled JSON data extraction and streamlined multiple asynchronous network responses into a unified console interface.[cite: 1]

### 📝 Day 20: OpenAI + Public API Combined[cite: 1]
* **Concept:** Connected a third-party data endpoint directly to an LLM provider to process live inputs dynamically.[cite: 1]
* **Data Pipeline:** Extracted text from a public endpoint and passed it contextually into a secure AI client to generate optimized developer insights.[cite: 1]

### 📝 Day 21: Nested JSON Deep Parsing Practice[cite: 1]
* **Concept:** Mastered multi-level nested dictionary handling and object schema extraction.[cite: 1]
* **Safe Navigation:** Implemented `.get()` nesting chains with custom defaults to guarantee crash-free fallback management in data tracking.[cite: 1]

### 📝 Day 22: FastAPI Basics[cite: 1]
* **Concept:** Created the first live web backend environment using FastAPI and production Uvicorn runners.[cite: 1]
* **Routing:** Successfully deployed a clean root handler (`/`) alongside dynamic URL path parameters (`/greet/{name}`) verified via Swagger UI (`/docs`).[cite: 1]

### 📝 Day 23: FastAPI: Query Parameters & Request Body[cite: 1]
* **Concept:** Explored advanced routing mechanics by handling dynamic query strings and schema-structured JSON payloads.[cite: 1]
* **Data Validation:** Utilized Pydantic's `BaseModel` to strictly validate incoming request body objects (`/products`), alongside managing custom default states inside dynamic queries (`/search`).[cite: 1]

### 📝 Day 24: FastAPI Error Handling & Virtual Environment[cite: 1]
* **Concept:** Configured an isolated python framework scope using `venv` to prevent interpreter path confusion permanently.[cite: 1]
* **Error Handling:** Mastered industrial API standard error dispatching by raising proper `HTTPException(status_code=404)` handlers to securely catch missing records during route lookups.[cite: 1]

### 📝 Day 25: FastAPI Path Operations Order & Multi-Route Resolution[cite: 1]
* **Concept:** Explored FastAPI's top-down matching mechanism for URL path layouts.[cite: 1]
* **Path Ordering:** Discovered that placing dynamic routes (`/products/{product_id}`) above static routes (`/products/featured`) captures static keywords incorrectly as variables, creating a tracking mismatch. Resolved this routing bug successfully by prioritizing exact static endpoints at the top of the execution block.[cite: 1]

### 📝 Day 26: FastAPI: Path Parameter Type Validation[cite: 1]
* **Concept:** Explored FastAPI's automatic data validation using standard Python type hinting (`item_id: int`).[cite: 1]
* **Type Validation:** Verified that sending a valid integer (`/items/5`) executes correctly, while sending an invalid type like text (`/items/abc`) triggers an automatic `422 Unprocessable Entity` response.[cite: 1]
* **Mechanism:** Learnt that FastAPI leverages Pydantic internally to parse and validate incoming data before it even hits the core path function, removing the need for manual validation checks.[cite: 1]

### 📝 Week 4 Summary & Core Framework Wrap-Up[cite: 1]
This week, I transitioned into backend development using FastAPI. I learned the basics of routing, handling parameters, and managing incoming request data securely. I practiced structural rules like endpoint ordering to avoid bugs, implemented data validation using Pydantic, and created proper custom error handling using status codes. Everything was brought together into a fully functional Mini Inventory system.[cite: 1]

### 📝 Day 27: Mini Inventory API (Week 4 Wrap-Up)[cite: 1]
* **Concept:** Combined all backend concepts from Week 4 into one single functional inventory microservice file.[cite: 1]
* **Implementation:** Built four paths: getting all items, fetching a single item by its numeric identity, adding a new item, and checking structure validity.[cite: 1]
* **Error Handling:** Used a standard loop logic that automatically triggers an explicit `HTTPException(status_code=404)` message immediately if a user requests a product ID that does not exist inside our system data array.[cite: 1]

## 📝 Day 28: Deploy FastAPI to Vercel[cite: 1]
* **Concept:** Learned how to deploy a local FastAPI project to the live internet for a portfolio.[cite: 1]
* **Implementation:** Created a simple `vercel.json` configuration file, connected the GitHub repository to Vercel, and successfully deployed the backend for free.[cite: 1]
* **Live API Link:** [https://90-day-ai-automation.vercel.app/docs](https://90-day-ai-automation.vercel.app/docs)[cite: 1]

### 📝 Day 29: Connect FastAPI to n8n Workflow[cite: 1]
* **Concept:** Transitioned to Month 2 automation concepts by linking custom backend infrastructure directly to an enterprise automation platform.[cite: 1]
* **Implementation:** Configured a manual execution sequence inside n8n, mapped an HTTP Request node using the `GET` method to point directly to the live Vercel inventory endpoint, and verified data parsing.[cite: 1]
* **Result:** Successfully fetched the live inventory dictionary structure (`Laptop`, `Mouse`, `Keyboard`) directly into the n8n node canvas output panel.[cite: 1]

### 📝 Day 30: Google Sheets Integration & Data Upsert Logic[cite: 1]
* **Concept:** Modeled database synchronization workflows by streaming external API responses into spreadsheets.[cite: 1]
* **Implementation:** Connected Google Sheets OAuth2 credentials into n8n and utilized the **Append or Update Row** operation.[cite: 1]
* **Data Structuring:** Configured exact data key mapping (`id`, `name`, `price`, `stock`) and set `Id` as the unique matching key constraint. This structural logic creates an industrial upsert mechanism, preventing row duplication by cleanly updating existing stocks if the items run again.[cite: 1]

### 📝 Day 31: Live API Automation with Webhook Trigger[cite: 1]
* **Concept:** Converted the manual testing layout into a completely hands-free, event-driven production pipeline.[cite: 1]
* **Implementation:** Swapped manual node executors with a native **Webhook Trigger** (GET method) capable of running background jobs autonomously via incoming network hits.[cite: 1]
* **Data Processing:** Implemented a **Split Out** node autonomously between the HTTP caller and the database writer. Because incoming API payloads stream down inside a packed singular array, splitting out the main data key breaks down the object structure into clean individual items. This optimization handles iterative workflows flawlessly, sending unique item payloads directly to Google Sheets rows automatically.[cite: 1]

### 📝 Day 32: Production Webhook & Error Handling (n8n)[cite: 1]
* **Concept:** Transitioned from development mode to fully operational production infrastructure by understanding the critical difference between Test URLs and Production URLs. Learnt that production webhooks run 24/7 as a background daemon without needing the n8n editor active.[cite: 1]
* **Production Deployment:** Successfully flipped the workflow execution state to **Active/Published**. Captured the dynamic production web gateway routing (`/webhook/` injection format) and verified remote triggering with the editor panel closed.[cite: 1]
* **Error Infrastructure (Fail-Safe):** Architected a dedicated downstream global **Error Trigger Workflow** named `Error_Workflow`. Configured the core workflow properties to automatically reroute network timeouts, API drops, or execution faults into this error handler to log diagnostic data safely inside Google Sheets, eliminating silent crashes.[cite: 1]

### 📝 Day 33: Email Notification Automation & Conditional Logic (n8n)[cite: 1]
* **Concept:** Transitioned the automation system from a static data pipe to an intelligent, decision-making production layout by exploring n8n's conditional branching (`IF` Node).[cite: 1]
* **Logical Branching:** Implemented a data evaluation gate immediately following the `Split Out` array extraction layer. Configured a dynamic numerical comparison check to trap item inventory state where `stock` is **Less Than 15**.[cite: 1]
* **Alert Infrastructure:** Integrated a live **Gmail API / SMTP Node** downstream on the `true` logical outcome path. Designed an autonomous multi-variable email notification payload that dynamically fires custom real-time alert vectors directly to the ops team when stock thresholds drop, leaving the `false` data to process cleanly without triggering notifications.[cite: 1]

### 📝 Day 34: Scheduled Trigger & Cron-Based Automation (n8n)
* **Concept:** Advanced from event-driven (reactive) webhooks to time-based (proactive) scheduled background automation handlers.
* **Proactive Scheduling:** Replaced the external network gateway dependency with a native **Schedule Trigger** core module. Configured an iterative minute-based heartbeat interval to drive background execution sweeps entirely hands-free.
* **Architecture Integration:** Linked the system directly into the decoupled multi-node inventory processing block (`HTTP Request` ➡️ `Split Out` ➡️ `IF` Gate ➡️ `Gmail Alert`). Verified stable logical evaluation routines and dynamic payload delivery without relying on inbound external network calls.