# Decision Log

## Skylark Drones Business Intelligence Agent


# 1. Key Assumptions

The following assumptions were made while building the solution:

- monday.com boards are considered the primary source of business information.
- Business data may contain missing values, inconsistent formats, and incomplete records.
- The AI agent has read-only access to monday.com data.
- Founder queries may not always contain exact technical terms, therefore natural language intent detection is used.
- The objective is to provide actionable business insights instead of only displaying raw data.


---

# 2. Technology Decisions


## monday.com GraphQL API

### Decision:
Used monday.com GraphQL API for data access.

### Reason:
- Provides dynamic access to live business data.
- Avoids hardcoding CSV files.
- Allows the agent to work with updated board information.
- Supports integration with multiple boards.


---

## Pandas Analytics Layer

### Decision:
Used Pandas for data processing and analysis.

### Reason:
- Efficient handling of structured business data.
- Provides data cleaning and aggregation capabilities.
- Suitable for calculating revenue, pipeline, and operational metrics.


---

## Google Gemini API

### Decision:
Used Gemini as the reasoning and response generation layer.

### Reason:
- Provides natural language understanding.
- Converts analytical outputs into executive-level explanations.
- Enables conversational interaction with business users.


---

## Streamlit

### Decision:
Used Streamlit for the user interface.

### Reason:
- Enables rapid prototype development.
- Provides an interactive conversational experience.
- Allows founders to query the system without technical knowledge.


---

# 3. Data Handling Decisions


The system was designed to handle real-world messy business data.

Implemented approaches:

## Missing Data Handling

- Empty values are replaced with meaningful placeholders.
- Missing information is reported to the user.


## Text Normalization

- Extra spaces are removed.
- Text fields are standardized.


## Numeric Processing

- Currency symbols and commas are removed.
- Values are converted into numerical formats.


## Date Processing

- Different date formats are normalized automatically.


---

# 4. Interpretation of Leadership Updates


The phrase "leadership updates" was interpreted as an executive-level business report.

The generated update includes:

- Overall business summary
- Revenue performance
- Pipeline health
- Operational insights
- Data quality concerns
- Business risks
- Recommended actions


The goal is to help founders make decisions quickly without manually analysing multiple boards.


---

# 5. Trade-offs


## Rule-Based Intent Detection vs Fully LLM-Based Agent


### Decision:
Used a lightweight rule-based intent detection system.

### Reason:
- The number of business categories was limited.
- Provides predictable behaviour.
- Reduces unnecessary API calls.
- Suitable for the given 6-hour development timeline.


A fully autonomous LLM agent could be implemented in the future.


---

## Prototype Speed vs Production Architecture


### Decision:
Built a lightweight architecture using Streamlit, Pandas, and APIs.

### Reason:
- Faster implementation.
- Easy testing.
- Suitable for demonstrating the core business intelligence workflow.


A production system could include a data warehouse, authentication, monitoring, and advanced analytics pipelines.


---

# 6. Challenges Handled


## Messy Business Data

Challenge:
Business records contained missing and inconsistent values.

Solution:
Implemented automated cleaning and quality reporting.


## Ambiguous Queries

Challenge:
Founder questions may have multiple interpretations.

Solution:
Implemented intent detection and conversational analysis.


## Multiple Data Sources

Challenge:
Insights may require combining sales and operational information.

Solution:
Integrated both Deals and Work Orders monday.com boards.


---

# 7. Future Improvements


With additional development time, the system could include:

- Machine learning based query classification
- Predictive revenue forecasting
- Automated weekly leadership emails
- Interactive dashboards
- Better entity extraction for sectors and regions
- User authentication
- Advanced multi-agent architecture


---

# Conclusion

The Skylark Drones Business Intelligence Agent provides a conversational interface for founders to query business data, understand performance, identify risks, and receive actionable recommendations from live monday.com data.