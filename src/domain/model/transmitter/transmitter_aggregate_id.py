import uuid


class TransmitterAggregateId:
    def __init__(self):
        self.__id = uuid.uuid4()
