from typing import Any

import boto3  # type: ignore
import psycopg
from psycopg import Connection
from psycopg.rows import TupleRow

from config.env import MinioEnv, PostgresEnv


class DBConnection:
    @staticmethod
    def connect() -> Connection[TupleRow]:
        env = PostgresEnv()
        return psycopg.connect(
            host=env.get_host_of_private_value(),
            port=env.get_port_of_private_value(),
            user=env.get_user_of_private_value(),
            password=env.get_password_of_private_value(),
            database=env.get_database_of_private_value(),
        )


class MinioConnection:
    @staticmethod
    def connect() -> Any:
        env = MinioEnv()
        return boto3.resource(  # type: ignore
            service_name=env.get_service_name_of_private_value(),
            endpoint_url=env.get_endpoint_of_private_value(),
            aws_access_key_id=env.get_access_key_of_private_value(),
            aws_secret_access_key=env.get_secret_key_of_private_value(),
        )
