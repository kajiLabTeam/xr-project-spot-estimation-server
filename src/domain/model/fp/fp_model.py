class FpModel:
    def __init__(self, extension: str):
        if len(extension) > 10:
            raise ValueError("Invalid extension")
        self.__extension = extension
