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
| **Day 37** | **Portfolio Showcase: Enterprise AI Inventory Assistant** | 🚀 |

---

# 🌟 PORTFOLIO PROJECT: Enterprise AI Inventory Assistant

### 📺 Live Demo Video
> 🔗 **[Watch the Live System Walkthrough & Demo Here](PASTE_YOUR_GOOGLE_DRIVE_OR_YOUTUBE_LINK_HERE)** *(Replace this with your video link once recorded)*

---

### 📝 Problem Statement
Retail and E-commerce businesses lose significant revenue due to delayed customer service responses and slow manual inventory checks. Providing instant, 24/7 product availability updates traditionally requires expensive standalone software setups or high-maintenance customer support teams operating round the clock.

### 💡 The Solution
A production-ready, event-driven **AI Inventory Assistant** connected directly to Telegram. The system functions as a fully automated customer support agent that queries a live spreadsheet database in real-time, interprets user intent via natural language, and responds instantly. 

### ⚙️ Core System Architecture
The data pipeline runs seamlessly across distributed environments without heavy codebase dependencies:
```text
[Customer on Telegram] 
       │ (Inbound Query via Webhook)
       ▼
[n8n Automation Engine] ──(Fetch Live Stock)──► [Google Sheets Database]
       │                                                 │
       ├────────────────◄──(Inject Context Payload)──────┘
       ▼
[OpenRouter AI Gateway] (Llama 3.3 Infrastructure - $0 Cost Model)
       │
       ▼ (Grounded, Context-Aware Response in Roman Urdu)
[Customer on Telegram]