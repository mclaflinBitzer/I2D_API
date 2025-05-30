
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import os
import json



# API Query with pagination control (ability to iterate through all pages/records)

# API base URL and static parameters
def api_call():
    api_url = "https://my.intelligence2day.com/components/api/search.cfc"
    params = {
        "method": "query",
        "APIid": "I2DE_4880557FFC6ABA165C916880849F9CAC",
        "authKey": "c51e7492-ab7f-46d8-9d10-edd4e434d2c1",
        "customerGUID": "b6150206-d9b1-4963-8907-22b7695c0477",
        "accessGroups": "8329",
        "returnFields": "*",
        # "queryString": "*:*",  # Query for all records
        "queryString": "dateline:[NOW-2MONTHS TO NOW] AND topicId:135576",  # Query for all records within time range
        "maxRows": 500,  # Limit to x results
        "sort": "dateline desc",  # Sort by UID in descending order
    }

    # Pagination control
    cursor = "*"  # Start with an empty cursor for the first request
    has_more = True
    total_articles = 0
    page = 1
    all_articles = []  # To store all article data

    while has_more:
        time.sleep(2)
        print(f"\n--- Fetching Page {page} ---")

        # Update the cursor in the request parameters for pagination
        params["cursorMark"] = cursor

        # Make the request
        response = requests.get(api_url, params=params, verify=False)

        # Print the status code
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            try:
                data = response.json()  # Parse the response as JSON
                print("Returned Data:")

                formatted_json = json.dumps(data, indent=4)
                print(formatted_json)    # Print the raw JSON response

                articles = data.get("docs", [])
                next_cursor = data.get("nextCursormark", None)

                if not articles:
                    print("No more articles returned.")
                    break

                print(f"Retrieved {len(articles)} articles on page {page}.")

                # Print the articles' title, summary, and URL
                for i, article in enumerate(articles, 1):
                    title = article.get("headline", "No title")
                    summary = article.get("summary", "No summary")
                    url = article.get("attachmenturl", "No URL")
                    date = article.get("dateline", "No date")

                    all_articles.append({"Title": title, "Summary": summary, "URL": url, "Date": date})

                    # print(f"\nArticle {total_articles + i}")
                    # print(f"Title   : {title}")
                    # print(f"Summary : {summary}")
                    # print(f"URL     : {url}")
                    # print(f"Date    : {date}")

                total_articles += len(articles)
                page += 1

                # Prepare for the next iteration with the nextCursormark
                if next_cursor:
                    cursor = next_cursor  # Update the cursor for the next request
                else:
                    has_more = False  # No more pages, end the loop

            except ValueError:
                print("Error: Response is not valid JSON.")
                break
        else:
            print(f"Request failed with status code {response.status_code}")
            break

    print(f"\n✅ Total articles fetched: {total_articles}")
    return all_articles

def article_call():
    api_url = "https://my.intelligence2day.com/components/api/search.cfc"
    params = {
        "method": "query",
        "APIid": "I2DE_4880557FFC6ABA165C916880849F9CAC",
        "authKey": "c51e7492-ab7f-46d8-9d10-edd4e434d2c1",
        "customerGUID": "b6150206-d9b1-4963-8907-22b7695c0477",
        "accessGroups": "8329",
        "returnFields": "*",
        # "queryString": "*:*",  # Query for all records
        "queryString": "dateline:[NOW-14DAYS TO NOW] AND topicId:135576",  # Query for all records within time range to update w/ topicId
        "maxRows": 500,  # Limit to x results
        "sort": "dateline desc",  # Sort by UID in descending order
    }

    # Pagination control
    cursor = "*"  # Start with an empty cursor for the first request
    has_more = True
    total_articles = 0
    page = 1
    all_articles = []  # To store all article data

    while has_more:
        time.sleep(2)
        print(f"\n--- Fetching Page {page} ---")

        # Update the cursor in the request parameters for pagination
        params["cursorMark"] = cursor

        # Make the request
        response = requests.get(api_url, params=params, verify=False)

        # Print the status code
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            try:
                data = response.json()  # Parse the response as JSON
                print("Returned Data:")

                formatted_json = json.dumps(data, indent=4)
                print(formatted_json)    # Print the raw JSON response

                articles = data.get("docs", [])
                next_cursor = data.get("nextCursormark", None)

                if not articles:
                    print("No more articles returned.")
                    break

                print(f"Retrieved {len(articles)} articles on page {page}.")

                # Print the articles' title, summary, and URL
                for i, article in enumerate(articles, 1):
                    title = article.get("headline", "No title")
                    summary = article.get("summary", "No summary")
                    url = article.get("attachmenturl", "No URL")
                    date = article.get("dateline", "No date")

                    all_articles.append({"Title": title, "Summary": summary, "URL": url, "Date": date})

                    # print(f"\nArticle {total_articles + i}")
                    # print(f"Title   : {title}")
                    # print(f"Summary : {summary}")
                    # print(f"URL     : {url}")
                    # print(f"Date    : {date}")

                total_articles += len(articles)
                page += 1

                # Prepare for the next iteration with the nextCursormark
                if next_cursor:
                    cursor = next_cursor  # Update the cursor for the next request
                else:
                    has_more = False  # No more pages, end the loop

            except ValueError:
                print("Error: Response is not valid JSON.")
                break
        else:
            print(f"Request failed with status code {response.status_code}")
            break

    print(f"\n✅ Total articles fetched: {total_articles}")
    return all_articles
