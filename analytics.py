import pandas as pd

def find_column(df, keywords):
    """
    Find the first column whose name contains any keyword.
    """

    for col in df.columns:
        name = col.lower()

        for key in keywords:
            if key in name:
                return col

    return None


# ------------------------------
# Revenue Summary
# ------------------------------

def revenue_summary(df):

    revenue_col=find_column(
        df,
        ["value","amount","revenue"]
    )


    if revenue_col is None:
        return "Revenue information unavailable"


    revenue=pd.to_numeric(
        df[revenue_col],
        errors="coerce"
    ).fillna(0)


    return {

        "Total Pipeline Value":
            float(revenue.sum()),

        "Average Deal Size":
            float(revenue.mean()),

        "Highest Opportunity":
            float(revenue.max()),

        "Number Of Opportunities":
            len(revenue)

    }

# ------------------------------
# Pipeline Health
# ------------------------------

def pipeline_health(df):

    status_col = find_column(
        df,
        ["status"]
    )

    if status_col is None:
        return {
            "error": "Status column not found"
        }

    return (
        df[status_col]
        .value_counts(dropna=False)
        .to_dict()
    )


# ------------------------------
# Deal Stage Summary
# ------------------------------

def deal_stage_summary(df):

    stage_col = find_column(
        df,
        ["stage"]
    )

    if stage_col is None:
        return {
            "error": "Deal Stage column not found"
        }

    return (
        df[stage_col]
        .value_counts(dropna=False)
        .to_dict()
    )


# ------------------------------
# Sector Performance
# ------------------------------

def sector_performance(df):

    sector_col = find_column(
        df,
        ["sector", "service"]
    )

    if sector_col is None:
        return {
            "error": "Sector column not found"
        }

    return (
        df[sector_col]
        .value_counts(dropna=False)
        .to_dict()
    )


# ------------------------------
# Closure Probability
# ------------------------------

def closure_probability(df):

    probability_col = find_column(
        df,
        ["probability"]
    )

    if probability_col is None:
        return {
            "error": "Probability column not found"
        }

    return (
        df[probability_col]
        .value_counts(dropna=False)
        .to_dict()
    )


# ------------------------------
# Missing Data Report
# ------------------------------

def missing_data_report(df):

    report = {}

    for col in df.columns:

        missing = (
            df[col].isna().sum()
            + (df[col] == "Unknown").sum()
        )

        report[col] = int(missing)

    return report

# ------------------------------
# Leadership Update
# ------------------------------

def leadership_update(df):

    return {

        "Revenue Summary":
            revenue_summary(df),

        "Pipeline Health":
            pipeline_health(df),

        "Sector Performance":
            sector_performance(df),

        "Deal Stages":
            deal_stage_summary(df),

        "Closure Probability":
            closure_probability(df),

        "Missing Data":
            missing_data_report(df)
    }
def operational_summary(
        work_df
):


    status_col=find_column(
        work_df,
        ["status"]
    )


    if status_col is None:

        return {
            "error":
            "Work order status unavailable"
        }



    return {

        "Project Status":
            work_df[status_col]
            .value_counts()
            .to_dict(),

        "Total Projects":
            len(work_df)

    }
def operational_summary(df):

    status_col = find_column(
        df,
        ["status"]
    )

    if status_col is None:
        return {
            "error": "Operational status column not found"
        }


    return {

        "Total Work Orders":
            int(len(df)),

        "Status Distribution":
            df[status_col]
            .value_counts(dropna=False)
            .to_dict()

    }
def sector_pipeline(df, sector):

    sector_col = find_column(
        df,
        [
            "sector",
            "industry",
            "service"
        ]
    )


    if sector_col is None:
        return {
            "error":
            "Sector column missing"
        }


    filtered = df[
        df[sector_col]
        .str.lower()
        .str.contains(
            sector.lower(),
            na=False
        )
    ]


    return {

        "Sector":
            sector,

        "Number of Deals":
            len(filtered),

        "Pipeline Value":
            revenue_summary(filtered)

    }
def sector_pipeline(df, sector):

    sector_col = find_column(
        df,
        [
            "sector",
            "industry",
            "service"
        ]
    )

    if sector_col is None:
        return {
            "error": "Sector column not found"
        }


    filtered_df = df[
        df[sector_col]
        .astype(str)
        .str.lower()
        .str.contains(
            sector.lower(),
            na=False
        )
    ]


    return {

        "Sector": sector,

        "Number of Deals":
            len(filtered_df),

        "Pipeline Health":
            pipeline_health(filtered_df),

        "Revenue":
            revenue_summary(filtered_df)

    }