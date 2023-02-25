import requests
from data_models import ResponseSchema, FilterApi
from dataclasses import asdict

api_url = "https://rickandmortyapi.com/api"


def get_endpoint_response(endpoint: str, 
                          params: FilterApi)-> ResponseSchema:
    response = requests.get(url=f"{api_url}/{endpoint}", params=asdict(params))
    response.raise_for_status()
    response = ResponseSchema(**response.json())

    return response