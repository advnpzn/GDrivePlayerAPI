from GDrivePlayer.gdriveplayer import GDrivePlayer
from GDrivePlayer.exceptions import SearchLimitError, IDNotFoundError
from typing import Union, Optional, List
from GDrivePlayer.utils import plus_encode, jsonify


class Movie:

    def __init__(
            self,
            title,
            year,
            imdb,
            poster,
            genre,
            runtime,
            director,
            country,
            rating,
            votes,
            sub,
            quality
    ) -> None:
        self.title = title
        self.year = year
        self.imdb = imdb
        self.poster = poster
        self.genre = genre
        self.runtime = runtime
        self.director = director
        self.country = country
        self.rating = rating
        self.votes = votes
        self.sub = sub
        self.quality = quality

    def getPlayer(self) -> str:
        return f"http://database.gdriveplayer.us/player.php?imdb={self.imdb}"


class MovieIMDB:

    def __init__(
            self,
            Title,
            Year,
            Rated,
            Released,
            Runtime,
            Genre,
            Director,
            Writer,
            Actors,
            Plot,
            Language,
            Country,
            Awards,
            Poster,
            imdbRating,
            imdbVotes,
            imdbID,
            Type,
            Production,
            Response,
            player_url
    ) -> None:
        self.title = Title
        self.year = Year
        self.rated = Rated
        self.released = Released
        self.runtime = Runtime
        self.genre = Genre
        self.director = Director
        self.writer = Writer
        self.actors = Actors
        self.plot = Plot
        self.language = Language
        self.country = Country
        self.awards = Awards
        self.poster = Poster
        self.imdb_rating = imdbRating
        self.imdb_votes = imdbVotes
        self.imdb_id = imdbID
        self.type = Type
        self.production = Production
        self.response = Response
        self.player_url = player_url


class GMovie(GDrivePlayer):

    def __init__(self) -> None:
        self.__url_movie = super().url_movie

        super().__init__()

    def search(self, title: Optional[str] = '', year: Optional[Union[str, int]] = '', genre: Optional[str] = '',
               country: Optional[str] = '', actor: Optional[str] = '', limit: Optional[Union[int, str]] = 10,
               page: Optional[Union[int, str]] = 1) -> List[Movie]:
        if limit > 100:
            raise SearchLimitError(limit=limit)
        url = f"{self.__url_movie}search?title={plus_encode(title)}&limit={limit}&page={page}&year={year}&genre={genre}&country={country}&actor={actor}"
        res = jsonify(super().request(url))
        movieList = []
        for a in res:
            movieList.append(Movie(**a))

        return movieList

    def latestMovies(self, limit: Optional[Union[str, int]] = 10, page: Optional[Union[str, int]] = 1,
                     order: Optional[str] = "last_updated", sort: Optional[str] = "DESC") -> List[Movie]:
        if limit > 100:
            raise SearchLimitError(limit=limit)
        url = f"{self.__url_movie}newest?limit={limit}&page={page}&order={order}&sort={sort}"
        res = jsonify(super().request(url))
        movieList = []
        for a in res:
            movieList.append(Movie(**a))

        return movieList

    def movieDetail(self, imdb_id: Union[str, int]) -> Movie:
        url = f"{self.__url_movie[:-6]}imdb/{imdb_id}"
        try:
            res = jsonify(super().request(url))
            return MovieIMDB(**res)
        except KeyError:
            raise IDNotFoundError(id=id)
