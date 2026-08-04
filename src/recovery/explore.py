# explore.py
import requests

def explore_data(url: str, offset: int = 0, limit: int = 100, refine: dict | None = None) -> tuple[list, int]:
    if refine is None:
        refine = {}
    params={
        "offset":offset,
        "limit": limit,
        }
    params = params | {f"refine.{key}": value for key, value in refine.items()}

    r = requests.get(
        url,
        params=params,
        timeout=10
        )

    print(r.url)
    r.raise_for_status()
    response = r.json()
    results = response["results"]
    total_count = response["total_count"]
    return results, total_count

def paginate(url: str, limit: int = 100, refine: dict | None = None) -> list:
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
