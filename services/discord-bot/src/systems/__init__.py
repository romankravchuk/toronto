from ..database import Session


class BaseSystem(object):
    def __init__(self) -> None:
        self.session = Session()