from typing import Optional


class ApplicationError(BaseException):
    def __init__(self, message: str, extra_info: Optional[object] = None):
        super().__init__(message)
        self.extra_info = extra_info


class NoDataAvailableError(ApplicationError): ...


class TooMuchDataError(ApplicationError): ...


class WordLengthError(ApplicationError): ...