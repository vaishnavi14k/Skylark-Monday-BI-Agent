from google import genai
import os
from dotenv import load_dotenv

from analytics import (
    revenue_summary,
    pipeline_health,
    sector_performance,
    deal_stage_summary,
    closure_probability,
    operational_summary,
    missing_data_report,
    sector_pipeline
)


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)



def detect_intent(question):
    """
    Identify what type of business question
    the founder is asking.
    """

    question = question.lower()


    if any(word in question for word in [
        "revenue",
        "sales",
        "value",
        "amount",
        "money"
    ]):
        return "revenue"


    elif any(word in question for word in [
        "pipeline",
        "opportunity",
        "forecast",
        "deals"
    ]):
        return "pipeline"


    elif any(word in question for word in [
        "sector",
        "industry",
        "energy",
        "mining",
        "agriculture"
    ]):
        return "sector"


    elif any(word in question for word in [
        "stage",
        "funnel",
        "conversion"
    ]):
        return "stage"


    elif any(word in question for word in [
        "probability",
        "chance",
        "closure",
        "win"
    ]):
        return "probability"


    elif any(word in question for word in [
        "project",
        "work order",
        "execution",
        "operations",
        "delivery"
    ]):
        return "operations"


    elif any(word in question for word in [
        "data quality",
        "missing",
        "incomplete"
    ]):
        return "quality"
    elif "leadership" in question or "update" in question or "report" in question:

        return "leadership"


    else:
        return "unknown"




def run_analysis(
        intent,
        deals_df,
        work_orders_df
):
    """
    Execute the required analytics
    based on user intent.
    """


    if intent == "revenue":

        return {
            "Analysis Type":
                "Revenue Analysis",

            "Result":
                revenue_summary(
                    deals_df
                )
        }



    elif intent == "pipeline":

        return {

            "Analysis Type":
                "Pipeline Health",

            "Result":
                pipeline_health(
                    deals_df
                )
        }



    elif intent == "sector":

        words = question.split()

    sector = None

    for word in words:

        if word.lower() in [
            "energy",
            "agriculture",
            "mining"
        ]:
            sector = word


    if sector:

        return sector_pipeline(
            deals_df,
            sector
        )


        return sector_performance(
        deals_df
    )



    elif intent == "stage":

        return {

            "Analysis Type":
                "Deal Funnel Analysis",

            "Result":
                deal_stage_summary(
                    deals_df
                )
        }



    elif intent == "probability":

        return {

            "Analysis Type":
                "Deal Closure Probability",

            "Result":
                closure_probability(
                    deals_df
                )
        }



    elif intent == "operations":

        return {

            "Analysis Type":
                "Operational Performance",

            "Result":
                operational_summary(
                    work_orders_df
                )
        }



    elif intent == "quality":

        return {

            "Analysis Type":
                "Data Quality Report",

            "Deals Data Issues":
                missing_data_report(
                    deals_df
                ),

            "Work Order Issues":
                missing_data_report(
                    work_orders_df
                )
        }
    elif intent=="leadership":

        return {

        "Revenue":
        revenue_summary(deals_df),

        "Pipeline":
        pipeline_health(deals_df),

        "Operations":
        operational_summary(work_orders_df),

        "Data Quality":
        missing_data_report(deals_df)

    }
    



    else:

        return {

            "Message":
            """
            I can help with:
            - Revenue analysis
            - Pipeline health
            - Sector performance
            - Deal stages
            - Project execution
            - Data quality issues
            """
        }




def generate_response(
        question,
        deals_df,
        work_orders_df
):
    """
    Main AI agent function.
    """



    # Step 1:
    # Understand user query

    intent = detect_intent(
        question
    )



    # Step 2:
    # Run analytics

    analysis = run_analysis(
        intent,
        deals_df,
        work_orders_df
    )



    # Step 3:
    # Ask LLM to convert
    # numbers into business insights


    prompt = f"""

You are Skylark Drones Business Intelligence Agent.

You help founders and executives understand company performance.

User Question:
{question}


Business Analysis:
{analysis}


Prepare an executive level response.

Follow this format:

## Executive Summary
Give the overall business situation in 2-3 sentences.

## Key Metrics
Mention important numbers and trends.

## Business Interpretation
Explain what these numbers mean for decision making.

## Risks
Mention revenue risks, operational risks, and data quality issues.

## Recommended Actions
Give practical next steps for leadership.


Do not invent information.
Only use the provided analysis.

"""



    try:

        response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

        return response.text

    except Exception as e:


        return f"""

Unable to generate AI response.

Raw analysis:

{analysis}


Error:
{str(e)}

"""