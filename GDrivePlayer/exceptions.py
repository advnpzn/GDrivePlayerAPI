
class StatusCodeError(Exception):
    pass


class SearchLimitError(Exception):
    
    def __init__(self, limit) -> None:
        self.limit = limit
        self.message = f"Limit cannot exceed 100 animes. But you requested {limit} animes."
        super().__init__(self.message)


class AnimeIDNotFoundError(Exception):

    def __init__(self, id) -> None:
        self.message = f"The Specified Anime ID {id} is not Found."
        super().__init__(self.message)
