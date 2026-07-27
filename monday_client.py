import requests
from config import (
    MONDAY_API_TOKEN,
    MONDAY_API_URL
)

headers = {
    "Authorization": MONDAY_API_TOKEN,
    "Content-Type": "application/json"
}


def execute_query(query):
    """
    Executes a GraphQL query on Monday.com.
    """

    try:

        response = requests.post(
            MONDAY_API_URL,
            json={"query": query},
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        result = response.json()

        if "errors" in result:
            raise Exception(result["errors"])

        return result

    except requests.exceptions.Timeout:
        print("Request timed out.")
        return None

    except requests.exceptions.ConnectionError:
        print("Could not connect to Monday.com")
        return None

    except Exception as e:
        print("API Error:", e)
        return None


def fetch_board(board_id):

    query = f"""
    {{
      boards(ids: {board_id}) {{
        id
        name

        items_page(limit: 500) {{
          items {{
            id
            name

            column_values {{
              id
              text
              column {{
                title
              }}
            }}
          }}
        }}
      }}
    }}
    """

    return execute_query(query)

def get_board_name(board_json):

    try:
        return board_json["data"]["boards"][0]["name"]
    except:
        return "Unknown Board"


def fetch_deals_board():

    from config import DEALS_BOARD_ID

    return fetch_board(DEALS_BOARD_ID)


def fetch_work_orders_board():

    from config import WORK_ORDERS_BOARD_ID

    return fetch_board(WORK_ORDERS_BOARD_ID)