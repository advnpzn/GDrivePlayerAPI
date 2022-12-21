
class StatusCodeError(Exception):
    pass


class SearchLimitError(Exception):
    
    def __init__(self, limit, message) -> None:
        self.limit = limit
        self.message = message
        super().__init__(self.message)