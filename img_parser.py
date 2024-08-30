import os
import random
from serpapi import GoogleSearch

# Ваш API-ключ для SerpAPI
SERPAPI_KEY = 'cc1754ef7f1e1d415856fe67b0513997d711a0e6920e9e3e1b7ca9944bb163d4'


async def get_random_img(query='пустой запрос'):
    search = GoogleSearch({
        "q": query,
        "tbm": "isch",  # image search
        "api_key": SERPAPI_KEY,
        "ijn": "0",  # first page of results
    })

    results = search.get_dict()
    images_results = results.get("images_results", [])

    if images_results:
        random_image = random.choice(images_results)
        return random_image["original"]
    else:
        return 'null'
