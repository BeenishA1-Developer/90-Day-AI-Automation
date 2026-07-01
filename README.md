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

---

## 📊 Week 3 Summary & Reflections
This week focused heavily on real-world HTTP networking and AI orchestration. I mastered handling standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) and successfully automated workflows using the `requests` library. A critical industry lesson learned was handling API deprecation, as experienced with the retired `restcountries.com` endpoint, which taught me the value of fallback logic and adaptive data structural parsing. Finally, I successfully bridged third-party data pipelines with the OpenAI standard client using OpenRouter, learning how to pass live external inputs directly to an LLM securely using environment variables (`.env`).