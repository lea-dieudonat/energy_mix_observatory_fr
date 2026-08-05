# explore.py
import requests

def explore_data(url: str, offset: int = 0, limit: int = 100, refine: str = "") -> tuple[list, int]:
    params={
        "offset":offset,
        "limit": limit,
        "refine": refine
        }

    r = requests.get(
        url,
        params=params,
        timeout=10
        )

    r.raise_for_status()
    response = r.json()
    results = response["results"]
    total_count = response["total_count"]
    return results, total_count

def paginate(url: str, limit: int = 100, refine: str = "") -> list:
    offset = 0
    result_list = []
    results, total_count = explore_data(url, offset, limit, refine)
    result_list += results
    offset = limit
    while offset < total_count:
        results, total_count = explore_data(url, offset, limit, refine)
        result_list.extend(results)
        offset += limit
    return result_list

def fetch_by_year(url: str, year: int) -> list:
    result_list = []
    for month in range(1, 13):
        refine = f"date_heure:\"{year}/{month:02d}\""
        result_list += paginate(url, refine=refine)
    return result_list