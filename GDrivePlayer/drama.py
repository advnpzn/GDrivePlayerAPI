from GDrivePlayer.gdriveplayer import GDrivePlayer
from GDrivePlayer.exceptions import SearchLimitError, IDNotFoundError
from typing import Union, Optional, List
from GDrivePlayer.utils import plus_encode, jsonify, gen_ep_from_player_url


class Drama:

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


class LatestDrama:

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


class GDrama(GDrivePlayer):

    def __init__(self) -> None:
        self.__url_Drama = super().url_drama

        super().__init__()

    def search(self, title: Optional[str] = '', limit: Optional[Union[int, str]] = 10,
               page: Optional[Union[int, str]] = 1) -> List[Drama]:
        if limit > 100:
            raise SearchLimitError(limit=limit)
        url = f"{self.__url_Drama}search?title={plus_encode(title)}&limit={limit}&page={page}"
        res = jsonify(super().request(url))
        DramaList = []
        for a in res:
            a["player_url"] = gen_ep_from_player_url(a["player_url"], a["total_episode"])
            DramaList.append(Drama(**a))

        return DramaList

    def latestDramas(self, limit: Optional[Union[str, int]] = 10, page: Optional[Union[str, int]] = 1,
                     order: Optional[str] = "last_updated", sort: Optional[str] = "DESC") -> List[Drama]:
        if limit > 100:
            raise SearchLimitError(limit=limit)
        url = f"{self.__url_Drama}newest?limit={limit}&page={page}&order={order}&sort={sort}"
        res = jsonify(super().request(url))
        DramaList = []
        for a in res:
            DramaList.append(LatestDrama(**a))

        return DramaList

    def DramaDetail(self, id: Union[str, int]) -> Drama:
        url = f"{self.__url_Drama}id/{id}"
        try:
            res = jsonify(super().request(url))
            return Drama(**res[0])
        except KeyError:
            raise IDNotFoundError(id=id)



