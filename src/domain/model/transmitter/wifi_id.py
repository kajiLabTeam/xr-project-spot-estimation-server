import uuid


class WifiId:
    def __init__(self):
        self.__id = uuid.uuid4()

    def get_id_of_private_value(self):
        return self.__id
