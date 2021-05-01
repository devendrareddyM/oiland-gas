from psycopg2.extras import RealDictCursor
from supports.response_module import *
from django.db import connection as conn
from api_framework.settings import DATABASES
from database.pg_conn import pg_connection


# Query function
def django_query_insert_any(role_id, sql):
    """

    :param role_id: role id of the user
    :param sql: query to be executed must be in array
    :return: connection status
    """
    if role_id == 'Admin':
        if conn:
            with conn.cursor() as cursor:
                try:
                    for each_sql in sql:
                        cursor.execute(each_sql)
                    conn.commit()
                    return conn, 0

                except Exception as err:
                    return 0, err
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function
def django_query_insert_specific_role(role_id, sql):
    if role_id == 'Admin':
        if conn:
            with conn.cursor() as cursor:
                try:
                    for each_sql in sql:
                        cursor.execute(each_sql)
                    conn.commit()
                    return conn, 0

                except Exception as err:
                    return 0, err

        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function
def query_insert_no_role(sql):
    conn = pg_connection(DATABASES)

    if conn:
        with conn.cursor(
                cursor_factory=RealDictCursor) as cursor:
            try:
                for each_sql in sql:
                    cursor.execute(each_sql)
                conn.commit()
                return conn, 0

            except Exception as err:
                return 0, err

    else:
        return response_nodbconn()


def django_query_insert_csv(role_id,query, data):
    """

    :param role_id:
    :param query:
    :param data:
    :return: connection status
    """
    if role_id == 'Admin':
        if conn:
            with conn.cursor() as cursor:
                try:
                    cursor.executemany(query, data)
                    conn.commit()
                    return conn, 0

                except Exception as err:
                    return 0, err
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()
