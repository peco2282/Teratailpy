class BadRequest(Exception):
    pass


class Forbidden(Exception):
    pass


class NotFound(Exception):
    pass


class MethodNotAllowed(Exception):
    pass


class InvalidLimitRequested(Exception):
    pass


class InternalServerError(Exception):
    pass
