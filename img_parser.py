import os
import random
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.environ.get('SERPAPI_KEY')


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
