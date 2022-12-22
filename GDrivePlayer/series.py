from GDrivePlayer.gdriveplayer import GDrivePlayer
from GDrivePlayer.exceptions import SearchLimitError, IDNotFoundError
from typing import Union, Optional, List
from GDrivePlayer.utils import plus_encode, jsonify


class Series:

    def __init__(
            self,
            id,
            imdb,
            title,
            poster,
            summary,
            genre,
            status,
            type,
            total_episode,
            sub,
            detail
    ) -> None:
        self.id = id
        self.title = title
        self.poster = poster
        self.genre = genre
        self.imdb = imdb
        self.summary = summary
        self.status = status
        self.type = type
        self.total_episode = total_episode
        self.sub = sub
        self.detail = detail


class SeriesDetail:

    def __init__(
            self,
            id,
            imdb,
            title,
            poster,
            summary,
            genre,
            status,
            type,
            total_episode,
            sub,
            list_episode
    ) -> None:
        self.id = id
        self.title = title
        self.poster = poster
        self.genre = genre
        self.imdb = imdb
        self.status = status
        self.summary = summary
        self.type = type
        self.total_episode = total_episode
        self.sub = sub
        self.list_episode: List[EpisodeList] = list_episode


class EpisodeList:

    def __init__(self, episode, player_url) -> None:
        self.episode = episode
        self.player_url = player_url


class GSeries(GDrivePlayer):

    def __init__(self) -> None:
        self.__url_Series = super().url_series

        super().__init__()

    def search(self, title: Optional[str] = '', limit: Optional[Union[int, str]] = 10,
               page: Optional[Union[int, str]] = 1) -> List[Series]:
        if limit > 100:
            raise SearchLimitError(limit=limit)
        url = f"{self.__url_Series}search?title={plus_encode(title)}&limit={limit}&page={page}"
        res = jsonify(super().request(url))
        SeriesList = []
        for a in res:
            SeriesList.append(Series(**a))

        return SeriesList

    def latestSeries(self, limit: Optional[Union[str, int]] = 10, page: Optional[Union[str, int]] = 1,
                     order: Optional[str] = "last_updated", sort: Optional[str] = "DESC") -> List[Series]:
        if limit > 100:
            raise SearchLimitError(limit=limit)
        url = f"{self.__url_Series}newest?limit={limit}&page={page}&order={order}&sort={sort}"
        res = jsonify(super().request(url))
        SeriesList = []
        for a in res:
            SeriesList.append(Series(**a))

        return SeriesList

    def seriesDetail(self, id: Union[str, int], season: Optional[Union[int, str]] = 1) -> SeriesDetail:
        url = f"{self.__url_Series}imdb/{id}/season{season}"

        try:
            res = jsonify(super().request(url))
            ep_list = []
            for i in res[0]["list_episode"]:
                ep_list.append(EpisodeList(**i))
            res[0]["list_episode"] = ep_list
            return SeriesDetail(**res[0])
        except KeyError:
            raise IDNotFoundError(id=id)
