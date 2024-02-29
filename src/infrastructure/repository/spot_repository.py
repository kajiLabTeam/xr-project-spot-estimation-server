import uuid

import psycopg
from psycopg import sql
from psycopg.rows import TupleRow

from domain.model.spot.aggregate import SpotAggregate
from domain.model.spot.coordinate import Coordinate
from domain.model.spot.spot_aggregate_id import SpotAggregateId
from domain.repository_impl.spot_repository_impl import (FpModelAggregateId,
                                                         SpotRepositoryImpl)


class SpotRepository(SpotRepositoryImpl):
    def find_for_spot_id(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
    ) -> SpotAggregate:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    sql.SQL("SELECT * FROM spots WHERE id = %s;"), (spot_id,)
                )
                spot_result = cursor.fetchone()
                if spot_result is None:
                    raise ValueError("Error: SpotRepository.find_for_spot_id")
                spot_id = spot_result[0]
                spot_name = spot_result[1]
                spot_floors = spot_result[2]
                spot_location_type = spot_result[3]

                cursor.execute(
                    sql.SQL("SELECT * FROM coordinates WHERE spot_id = %s;"), (spot_id,)
                )
                coordinate_result = cursor.fetchone()
                if coordinate_result is None:
                    raise ValueError("Error: SpotRepository.find_for_spot_id")

                latitude = coordinate_result[1]
                longitude = coordinate_result[2]

                coordinate = Coordinate(
                    latitude,
                    longitude,
                )
                return SpotAggregate(
                    id=spot_id,
                    name=spot_name,
                    floors=spot_floors,
                    location_type=spot_location_type,
                    coordinate=coordinate,
                )

    def find_for_fp_model_id(
        self,
        conn: psycopg.Connection[TupleRow],
        fp_model_id: FpModelAggregateId,
    ) -> SpotAggregate:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    sql.SQL(
                        "SELECT * FROM spots WHERE id = (SELECT spot_id FROM fp_models WHERE id = %s);"
                    ),
                    (fp_model_id,),
                )
                spot_result = cursor.fetchone()
                if spot_result is None:
                    raise ValueError("Error: SpotRepository.find_for_fp_model_id")
                spot_id = spot_result[0]
                spot_name = spot_result[1]
                spot_floors = spot_result[2]
                spot_location_type = spot_result[3]

                cursor.execute(
                    sql.SQL("SELECT * FROM coordinates WHERE spot_id = %s;"), (spot_id,)
                )
                coordinate_result = cursor.fetchone()
                if coordinate_result is None:
                    raise ValueError("Error: SpotRepository.find_for_fp_model_id")

                latitude = coordinate_result[1]
                longitude = coordinate_result[2]

                coordinate = Coordinate(
                    latitude,
                    longitude,
                )
                return SpotAggregate(
                    id=spot_id,
                    name=spot_name,
                    floors=spot_floors,
                    location_type=spot_location_type,
                    coordinate=coordinate,
                )

    def save(
        self,
        conn: psycopg.Connection[TupleRow],
        spot: SpotAggregate,
    ) -> SpotAggregate:
        with conn as conn:
            with conn.cursor() as cursor:
                # spotテーブルにインサート
                spot_id = spot.get_id_of_private_value()
                spot_name = spot.get_name_of_private_value()
                spot_floors = spot.get_floors_of_private_value()
                spot_location_type = spot.get_location_type_of_private_value()

                cursor.execute(
                    sql.SQL(
                        "INSERT INTO spots (id, name, floors, location_type) VALUES (%s, %s, %s, %s);"
                    ),
                    (spot_id, spot_name, spot_floors, spot_location_type),
                )

                # 最新のカラム（インサートしたもの）を取得
                insert_spot_id_result = cursor.fetchone()
                if insert_spot_id_result is None:
                    raise ValueError("Error: SpotRepository.create_spot")
                # 最新のカラムのうち、idを取得
                insert_spot_id: SpotAggregateId = insert_spot_id_result[0]

                # coordinatesテーブルにインサート
                coordinate_id = uuid.uuid4()
                latitude = (
                    spot.get_coordinate_of_private_value().get_latitude_of_private_value()
                )
                longitude = (
                    spot.get_coordinate_of_private_value().get_longitude_of_private_value()
                )

                cursor.execute(
                    sql.SQL(
                        "INSERT INTO coordinates (id, latitude, longitude, spot_id) VALUES (%s, %s, %s, %s);"
                    ),
                    (coordinate_id, latitude, longitude, insert_spot_id),
                )

                # インサート結果をコミット
                conn.commit()

                return spot
