
class StatusCodeError(Exception):
    pass


class SearchLimitError(Exception):
    
    def __init__(self, limit) -> None:
        self.limit = limit
        self.message = f"Limit cannot exceed 100. But you requested {limit} Objects."
        super().__init__(self.message)


class IDNotFoundError(Exception):

    def __init__(self, id) -> None:
        self.message = f"The Specified ID {id} is not Found."
        super().__init__(self.message)
