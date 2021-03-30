class Error(Exception):
    """Base class for other exceptions"""

    pass


class DriverNotFound(Error):
    """Raised when driver doesnot exists"""

    pass


class NoNearByCabsFound(Error):
    """Raised when no cabs are found"""

    pass
