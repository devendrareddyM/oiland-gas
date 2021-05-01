from psycopg2.extras import RealDictCursor
from supports.response_module import *

from api_framework.settings import DATABASES
from database.pg_conn import pg_connection
from django.db import connection as conn


# Query function
def django_query_modify_any_role(role_id, sql):
    if role_id:
        if conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(sql)
                    conn.commit()
                    return conn, 0

                except Exception as err:
                    return 0, err
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function
def django_query_modify_auth(role_id, sql):
    if role_id == 'Admin':
        if conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(sql)
                    conn.commit()
                    return conn, 0

                except Exception as err:
                    return 0, err
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function
def django_query_modify_by_super_admin(role_id, sql):
    if role_id == 1:
        if conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(sql)
                    conn.commit()
                    return conn, 0

                except Exception as err:
                    return 0, err
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function
def django_query_modify_no_role(sql):
    if conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                conn.commit()

            except Exception as err:
                return response_conflict(kind='update', err=str(err))

            return 1
    else:
        return response_nodbconn()
