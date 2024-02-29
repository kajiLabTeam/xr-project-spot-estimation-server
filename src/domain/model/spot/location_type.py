class LocationType:
    def __init__(
        self,
        location_type: str,
    ) -> None:
        if location_type not in ["indoor", "outdoor"]:
            raise ValueError("Invalid location type")
        self.__location_type = location_type

    def get_location_type_of_private_value(self) -> str:
        return self.__location_type
