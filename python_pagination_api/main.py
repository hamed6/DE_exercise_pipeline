from typing import List
from data_models import FilterApi, ResponseSchema
from send_request import get_endpoint_response


endpoint = "Character"

def get_all_pages_results(endpoint: str,
                          pages: int, 
                          params: FilterApi 
                          ) -> List[ResponseSchema]:
    list_of_results=[]
    for page in range(1, pages+1):
        params.page = page
        print(f"Get result from page {page}")
        one_page_response = get_endpoint_response(endpoint, params)
        list_of_results.extend(one_page_response.results)
    
    return list_of_results


if __name__ == "__main__":
    params = FilterApi()
    response = get_endpoint_response(endpoint, params)
    list_of_results = get_all_pages_results(endpoint, response.info.pages, params)
    print(f"Total records: {len(list_of_results)}")
