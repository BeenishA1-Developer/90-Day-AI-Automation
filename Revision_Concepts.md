## Day 29 — Connect FastAPI to n8n
**Concept:** HTTP Request node integration
**Key Point:** Live external API (Vercel URL) ko n8n ke HTTP Request node ke saath link karke data fetch karna.
**Common mistake:** API endpoint URL mein typo karna ya method (GET/POST) galat select karna → 404/405 error aana.

## Day 30 — Google Sheets Upsert
**Concept:** Append or Update Row operation
**Key Point:** "Id" ko match key banate hain taake duplicate rows na banein.
**Common mistake:** Match key set na karna → har run pe naya row ban jata hai aur data duplicate hota hai.

## Day 31 — Live API Automation (Webhook + Split Out)
**Concept:** Event-driven Webhook + Data Splitting
**Key Point:** Packed array payload ko Split Out node ke zariye single rows mein break karke Sheets mein likhna.
**Common mistake:** Split Out node skip karna → poora array ek hi row mein dump ho kar workflow crash kar deta hai.

## Day 32 — Production Webhook + Error Handling
**Concept:** Test URL vs Production URL & Error Trigger
**Key Point:** Production webhook 24/7 active rehta hai aur Error Trigger workflow silent crashes ko rokta hai.
**Common mistake:** Error Trigger na lagana → bot background mein crash ho jata hai aur humein pata bhi nahi chalta.

## Day 33 — Email Automation & Conditional Logic
**Concept:** IF Node branching + Gmail Node alerts
**Key Point:** Stock state check karna (e.g., < 15) aur condition true hone par dynamic real-time email fire karna.
**Common mistake:** True aur False paths ko galat wire kar dena → normal stock par bhi wrong alerts chale jana.

## Day 34 — Scheduled Trigger & Cron Automation
**Concept:** Time-based automation sweeps
**Key Point:** External webhook dependency ke bina native schedule module se fixed intervals par scripts chalana.
**Common mistake:** Interval bohot short rakhna → server par faltu ka overhead barh jana.

## Day 35 — Telegram Inventory Bot
**Concept:** Telegram Webhook Trigger + Dynamic Filters
**Key Point:** Chat variables `{{ $('Telegram Trigger').item.json.message.text }}` ko direct Google Sheet filtering logic banana.
**Common mistake:** Inbound JSON schema aur search parameter ka exact match na hona → text search fail hona.

## Day 36 — AI Agent with OpenRouter & Grounding
**Concept:** Advanced AI Agent node + Hallucination Guardrails
**Key Point:** OpenRouter free tier models ko strict prompt injection ke zariye sirf Google Sheets data par bound (ground) rakhna.
**Common mistake:** Open-ended prompt chorna → AI ka out-of-stock items ke liye fake prices aur ghost stock invent karna.

## Day 37 — Enterprise AI Assistant Showcase
**Concept:** System documentation & Technical Walkthrough
**Key Point:** Production-grade system architecture ko end-to-end user ke liye visual video aur data sync diagrams ke sath explain karna portfolio impact ke liye.
**Common mistake:** Live edge cases aur verification metrics show na karna → client ko tool ki reliability ka proof na milna.

## Day 38 — Conversational Order Booking Bot
**Concept:** Transactional E-commerce Checkout Flow
**Key Point:** Conversational flow ke andar explicit fields (item, quantity, delivery data) ko capture karke parallel processing database columns ke liye stage karna.
**Common mistake:** (Note: Not directly tested as a bug, general best practice) Conversational slots loosely chorna jis se model data parameters ko misalign kar de.

## Day 39 — E-Commerce Order Flow (Phantom-Item Fix)
**Concept:** Decoupled Cognitive Loop + Tool Separation
**Key Point:** AI ki sochne ki logic aur order write karne ki logic (`book_order` node) ko alag karna taake phantom items produce na hon.
**Common mistake:** N8n node parameters aur Google Sheets ke headers ka naming syntax alag rakhna → database write logic crash ho jana.