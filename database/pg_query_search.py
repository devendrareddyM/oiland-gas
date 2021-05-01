from psycopg2.extras import RealDictCursor
from supports.response_module import *
from django.db import connection as conn

from api_framework.settings import DATABASES
from database.pg_conn import pg_connection


# function to Return all rows from a cursor as a dict
def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    final_data = [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]
    if len(final_data) is 0:
        return None
    else:
        return final_data[0]


# Function to get the data from table without any role
def django_search_query(sql):
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            data = dictfetchall(cursor)
            return data
    else:
        return response_nodbconn()


# Query function with any role
def django_query_search_all_any_role(role_id, sql):
    if role_id == 'Admin':
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                data = dictfetchall(cursor)
                return data
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function with any role return one
def django_query_search_one_any_role(role_id, sql):
    if role_id:
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                data = dictfetchone(cursor)
                return data
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function
def django_query_search_one_auth(role_id, sql):
    if role_id == 1 or role_id == 2:
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                data = dictfetchone(cursor)
                return data
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function
def django_query_search_many_auth(role_id, sql):
    if role_id == 1 or role_id == 2:
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                data = dictfetchall(cursor)
                return data
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function with any role
def django_query_search_all_super_admin_role(role_id, sql):
    if role_id == 1:
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                data = dictfetchall(cursor)
                return data
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function with any role
def django_query_search_one_super_admin_role(role_id, sql):
    if role_id == 1:
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                data = dictfetchone(cursor)
                return data
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function with no role
def django_query_search_no_role_one(sql):
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            data = dictfetchone(cursor)
            return data
    else:
        return response_nodbconn()


############################################################################################################
# Query function
def query_search_one(role_id, sql):
    conn = pg_connection(DATABASES)
    if role_id:
        if conn:
            with conn.cursor(
                    cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sql)
                data = cursor.fetchone()
                return data
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function with no role
def query_search_no_role_all(sql):
    conn = pg_connection(DATABASES)
    if conn:
        with conn.cursor(
                cursor_factory=RealDictCursor) as cursor:

            cursor.execute(sql)
            data = cursor.fetchall()
            return data
    else:
        return response_nodbconn()
