import json
from typing import Union, List


def plus_encode(query: str):
    return query.replace(' ', '+')


def jsonify(content: str):
    return json.loads(content)


def gen_ep_from_player_url(url: str, total_ep: Union[int, str]) -> List[str]:
    url = url[:url.index('{')]
    player_urls = []
    for i in range(1, int(total_ep) + 1):
        player_urls.append(f"{url}{i}")
    return player_urls
