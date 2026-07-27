import pandas as pd


def json_to_dataframe(board_json):
    """
    Convert Monday.com GraphQL JSON into a Pandas DataFrame.
    """

    try:
        items = board_json["data"]["boards"][0]["items_page"]["items"]
    except Exception:
        return pd.DataFrame()

    rows = []

    for item in items:

        row = {}

        row["Item Name"] = item["name"]

        for column in item["column_values"]:
            column_name = column["column"]["title"]
            row[column_name] = column["text"]

        rows.append(row)

    return pd.DataFrame(rows)

def clean_missing_values(df):

    df = df.copy()

    for col in df.columns:

        if pd.api.types.is_string_dtype(df[col]):
            df[col] = df[col].fillna("Unknown")

        else:
            df[col] = df[col].fillna(0)

    return df
def clean_text(df):
    """
    Remove extra spaces and standardize text.
    """

    df = df.copy()

    for col in df.columns:

        if pd.api.types.is_string_dtype(df[col]):

            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .str.replace(r"\s+", " ", regex=True)
            )

    return df


def convert_dates(df):
    """
    Automatically convert date columns.
    """

    df = df.copy()

    for col in df.columns:

        name = col.lower()

        if (
            "date" in name
            or "month" in name
            or "close" in name
            or "delivery" in name
            or "invoice" in name
            or "payment" in name
        ):

            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

    return df


def convert_numeric_columns(df):
    """
    Automatically convert money/number columns.
    """

    df = df.copy()

    keywords = [
        "amount",
        "value",
        "price",
        "cost",
        "quantity",
        "probability",
        "revenue"
    ]

    for col in df.columns:

        if any(word in col.lower() for word in keywords):

            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", "")
                .str.replace("₹", "", regex=False)
                .str.strip()
            )

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    return df


def prepare_dataframe(board_json):
    """
    Complete preprocessing pipeline.
    """

    df = json_to_dataframe(board_json)

    if df.empty:
        return df

    df = clean_missing_values(df)
    df = clean_text(df)
    df = convert_dates(df)
    df = convert_numeric_columns(df)

    df = normalize_status_values(df)

    return df
def normalize_status_values(df):

    df = df.copy()


    for col in df.columns:

        if "status" in col.lower():

            df[col] = (
                df[col]
                .replace(
                    {
                        "":
                        "Unknown",

                        "Deal Status":
                        "Unknown"
                    }
                )
            )


    return df