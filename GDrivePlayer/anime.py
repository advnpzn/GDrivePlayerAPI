from gdriveplayer import GDrivePlayer
from exceptions import SearchLimitError
from typing import Union, Optional, List
from utils import  plus_encode, jsonify, gen_ep_from_player_url

class Anime:

    def __init__(
                    self, 
                    id, 
                    title,
                    poster,
                    genre,
                    summary,
                    status,
                    type,
                    total_episode,
                    sub,
                    player_url
                ) -> None:

        self.id = id
        self.title = title
        self.poster = poster 
        self.genre = genre
        self.summary = summary
        self.status = status
        self.type = type
        self.total_episode = total_episode
        self.sub = sub
        self.player_url = player_url 


class LatestAnime:

    def __init__(
                    self, 
                    id, 
                    title,
                    poster,
                    genre,
                    status,
                    type,
                    total_episode,
                    sub,
                    player_url
                ) -> None:

        self.id = id
        self.title = title
        self.poster = poster 
        self.genre = genre
        self.status = status
        self.type = type
        self.total_episode = total_episode
        self.sub = sub
        self.player_url = player_url 


class GAnime(GDrivePlayer):

    def __init__(self) -> None:
        self.__url_anime = super().url_anime

        super().__init__()

    def search(self, title: Optional[str] = '', limit: Optional[Union[int, str]] = 10, page: Optional[Union[int, str]] = 1) -> List[Anime]:
        if limit > 100:
            raise SearchLimitError(100, f"Limit cannot exceed 100 animes. But you requested {limit} animes.")
        url = f"{self.__url_anime}search?title={plus_encode(title)}&limit={limit}&page={page}"
        res = jsonify(super().request(url))
        animeList = []
        for a in res:
            animeList.append(self.__json_to_animeObj(a, 1))

        return animeList


    def latestAnimes(self, limit: Optional[Union[str, int]] = 10, page: Optional[Union[str, int]] = 1, order: Optional[str] = "last_updated", sort: Optional[str] = "DESC") -> List[Anime]:
        if limit > 100:
            raise SearchLimitError(100, f"Limit cannot exceed 100 animes. But you requested {limit} animes.")
        url = f"{self.__url_anime}newest?limit={limit}&page={page}&order={order}&sort={sort}"
        res = jsonify(super().request(url))
        animeList = []
        for a in res:
            animeList.append(self.__json_to_animeObj(a, 0))

        return animeList

    def __json_to_animeObj(self, an: dict, obj: bool):

        if obj is True:

            return Anime(
                    id=an["id"],
                    title=an["title"],
                    poster=an["poster"],
                    genre=an["genre"],
                    summary=an["summary"],
                    status=an["status"],
                    type=an["type"],
                    total_episode=an["total_episode"],
                    sub=an["sub"],
                    player_url=gen_ep_from_player_url(an["player_url"], an["total_episode"])
                )
        else:

            return LatestAnime(
                    id=an["id"],
                    title=an["title"],
                    poster=an["poster"],
                    genre=an["genre"],
                    status=an["status"],
                    type=an["type"],
                    total_episode=an["total_episode"],
                    sub=an["sub"],
                    player_url=gen_ep_from_player_url(an["player_url"], an["total_episode"])
                )

a = GAnime().latestAnimes()
for i in a:
    print(i.title)