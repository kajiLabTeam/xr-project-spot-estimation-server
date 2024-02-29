from uuid import UUID, uuid4


class SpotAggregateId:
    def __init__(self, id: UUID = uuid4()):
        self.__id = id
