from raw_data_id import RawDataId


class RawData:
    def __init__(
        self,
        raw_data: bytes,
    ):
        self.__id = RawDataId()
        self.__raw_data = raw_data
