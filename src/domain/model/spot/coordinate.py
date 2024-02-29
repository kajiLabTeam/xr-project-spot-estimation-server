class Coordinate:
    def __init__(
        self,
        latitude: float,
        longitude: float,
    ):
        if not -90 <= latitude <= 90:
            raise ValueError("Latitude must be between -90 and 90")

        if not -180 <= longitude <= 180:
            raise ValueError("Longitude must be between -180 and 180")

        self.__latitude = latitude
        self.__longitude = longitude

    def get_latitude_of_private_value(self):
        return self.__latitude

    def get_longitude_of_private_value(self):
        return self.__longitude
