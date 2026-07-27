# 🚁 Skylark Drones Business Intelligence Agent

An AI-powered Business Intelligence Agent that connects with monday.com boards and provides founder-level business insights through natural language queries.

The agent integrates live monday.com business data, handles messy real-world data, performs analytics, and uses Gemini AI to generate executive-level reports.

---

# 📌 Problem Statement

Business leaders often need quick answers from multiple data sources, but extracting insights manually requires:

- Pulling data from multiple boards
- Cleaning inconsistent records
- Analysing sales and operational data
- Creating reports manually

This project automates this process by creating an AI Business Intelligence Agent that answers business questions conversationally.

---

# 🚀 Features

## 1. monday.com Integration

- Connected to monday.com using GraphQL API
- Dynamically fetches data from:

  - Deals Board
  - Work Orders Board

- No hardcoded CSV data is used.

---

## 2. Data Resilience

The system handles real-world messy business data by:

- Handling missing values
- Replacing empty records with meaningful placeholders
- Cleaning inconsistent text formats
- Removing unnecessary spaces
- Converting numeric fields
- Normalizing date formats

The agent also highlights data quality issues during responses.

---

## 3. Business Intelligence Capabilities

The agent can answer questions related to:

### Sales & Revenue
- Revenue summary
- Deal values
- Average deal size
- Largest and smallest deals

### Pipeline Analysis
- Open opportunities
- Won/Lost deals
- Pipeline health
- Deal funnel analysis

### Sector Analysis
- Sector-wise performance
- Industry pipeline analysis

### Operations
- Work order status
- Project execution insights

### Data Quality
- Missing values
- Incomplete records
- Data hygiene issues

### Leadership Updates
Generates executive summaries containing:

- Business overview
- Key metrics
- Risks
- Recommendations

---

# 🏗️ System Architecture

```
Founder Business Question

          ↓

Streamlit Conversational Interface

          ↓

AI Agent (Gemini)

          ↓

Intent Detection

          ↓

Analytics Engine
(Pandas)

          ↓

Data Cleaning Layer

          ↓

monday.com GraphQL API

          ↓

Deals Board + Work Orders Board
```

---

# 🛠️ Tech Stack

## Programming Language

- Python

## AI Model

- Google Gemini API

## Data Processing

- Pandas

## Frontend

- Streamlit

## Database Integration

- monday.com GraphQL API

## Environment Management

- python-dotenv

---

# 📂 Project Structure

```
Skylark_Monday_BI_Agent/

│
├── streamlit_app.py        # Streamlit user interface
│
├── agent.py                # AI agent and query handling
│
├── analytics.py            # Business analytics functions
│
├── data_cleaner.py         # Data preprocessing pipeline
│
├── monday_client.py        # monday.com API integration
│
├── config.py               # Configuration management
│
├── requirements.txt        # Python dependencies
│
├── Decision_Log.md         # Project decisions and assumptions
│
└── README.md
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```
git clone <repository-url>
```

Navigate into the project:

```
cd Skylark_Monday_BI_Agent
```

---

## 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## 3. Environment Variables

Create a `.env` file in the project directory.

Add:

```
MONDAY_API_TOKEN=your_monday_api_token

DEALS_BOARD_ID=your_deals_board_id

WORK_ORDERS_BOARD_ID=your_work_orders_board_id

GEMINI_API_KEY=your_gemini_api_key
```

---

# ▶️ Running the Application

Start the Streamlit application:

```
streamlit run streamlit_app.py
```

The application will open in the browser.

---

# 💬 Example Queries

Users can ask:

```
How is our pipeline looking?
```

```
How's our pipeline looking for energy sector this quarter?
```

```
Prepare leadership update
```

```
What are the data quality issues?
```

```
Give me revenue insights
```

---

# 🧠 AI Agent Workflow

1. User enters a business question.

2. The agent identifies the intent:
   - Revenue
   - Pipeline
   - Sector
   - Operations
   - Leadership Update

3. Relevant analytics functions process monday.com data.

4. Gemini converts analytical results into executive-level insights.

5. Final response is displayed in a conversational format.

---

# 🔒 Data Security

- API keys are stored using environment variables.
- monday.com access is read-only.
- Sensitive credentials are excluded from GitHub using `.gitignore`.

---

# 🔮 Future Improvements

Possible improvements:

- Automated weekly leadership reports
- Revenue forecasting models
- Interactive dashboards
- Advanced query understanding using LLM agents
- Authentication and role-based access
- Historical trend analysis
- Automated alerts for pipeline risks

---

# 👩‍💻 Author
-Vaishnavi Karanam

Developed as part of the Skylark Drones Technical Assignment.