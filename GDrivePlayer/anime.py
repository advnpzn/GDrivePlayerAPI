from GDrivePlayer.gdriveplayer import GDrivePlayer
from GDrivePlayer.exceptions import SearchLimitError, IDNotFoundError
from typing import Union, Optional, List
from GDrivePlayer.utils import plus_encode, jsonify, gen_ep_from_player_url


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

    def search(self, title: Optional[str] = '', limit: Optional[Union[int, str]] = 10,
               page: Optional[Union[int, str]] = 1) -> List[Anime]:
        if limit > 100:
            raise SearchLimitError(limit=limit)
        url = f"{self.__url_anime}search?title={plus_encode(title)}&limit={limit}&page={page}"
        res = jsonify(super().request(url))
        animeList = []
        for a in res:
            a["player_url"] = gen_ep_from_player_url(a["player_url"], a["total_episode"])
            animeList.append(Anime(**a))

        return animeList

    def latestAnimes(self, limit: Optional[Union[str, int]] = 10, page: Optional[Union[str, int]] = 1,
                     order: Optional[str] = "last_updated", sort: Optional[str] = "DESC") -> List[Anime]:
        if limit > 100:
            raise SearchLimitError(limit=limit)
        url = f"{self.__url_anime}newest?limit={limit}&page={page}&order={order}&sort={sort}"
        res = jsonify(super().request(url))
        animeList = []
        for a in res:
            animeList.append(LatestAnime(**a))

        return animeList

    def animeDetail(self, id: Union[str, int]) -> Anime:
        url = f"{self.__url_anime}id/{id}"
        try:
            res = jsonify(super().request(url))
            return Anime(**res[0])
        except KeyError:
            raise IDNotFoundError(id=id)
