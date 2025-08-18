'''
# This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 

class SQLQueryBuilder:

    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        return query: str, the SQL query statement.
        """

    @staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :return query: str, the SQL insert statement.
        """

    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :return query: str, the SQL delete statement.
        """

    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        """
'''

class SQLQueryBuilder:

    @staticmethod
    def select(table, columns='*', where=None):
        if columns != '*':
            columns = ', '.join(columns)
        query = f"SELECT {columns} FROM {table}"
        if where:
            query += " WHERE " + ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query

    @staticmethod
    def insert(table, data):
        keys = ', '.join(data.keys())
        values = ', '.join(f"'{v}'" for v in data.values())
        return f"INSERT INTO {table} ({keys}) VALUES ({values})"

    @staticmethod
    def delete(table, where=None):
        query = f"DELETE FROM {table}"
        if where:
            query += " WHERE " + ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query

    @staticmethod
    def update(table, data, where=None):
        update_str = ', '.join(f"{k}='{v}'" for k, v in data.items())
        query = f"UPDATE {table} SET {update_str}"
        if where:
            query += " WHERE " + ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query
