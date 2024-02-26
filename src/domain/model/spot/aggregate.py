from coordinate_id import CoordinateId
from transmitter.transmitter_id import TransmitterId


class Spot:
    def __init__(
        self,
        name: str,
        floors: int,
        location_type: str,
        coordinate_id: CoordinateId,
        transmitter_id_collection: list[TransmitterId],
    ):
        if location_type not in ["indoor", "outdoor"]:
            raise ValueError("Invalid location type")
        self.name = name
        self.floors = floors
        self.locationType = location_type
        self.coordinate_id = coordinate_id
        transmitter_id_collection = transmitter_id_collection
