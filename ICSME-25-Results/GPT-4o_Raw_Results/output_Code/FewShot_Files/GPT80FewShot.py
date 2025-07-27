class SQLQueryBuilder:
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """

    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'] or '*'.
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return query: str, the SQL query statement.
        """
        # If columns is a list, join them with a comma, otherwise use '*'
        columns_str = ', '.join(columns) if isinstance(columns, list) else columns
        query = f"SELECT {columns_str} FROM {table}"
        
        # If where condition is provided, append it to the query
        if where:
            conditions = [f"{k}='{v}'" for k, v in where.items()]
            query += " WHERE " + " AND ".join(conditions)
        
        return query

    @staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement
        :return query: str, the SQL insert statement.
        """
        # Extract columns and values from the data dictionary
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{v}'" for v in data.values())
        
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        return query

    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be executed with DELETE operation in database
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return query: str, the SQL delete statement.
        """
        query = f"DELETE FROM {table}"
        
        # If where condition is provided, append it to the query
        if where:
            conditions = [f"{k}='{v}'" for k, v in where.items()]
            query += " WHERE " + " AND ".join(conditions)
        
        return query

    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be executed with UPDATE operation in database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return query: str, the SQL update statement.
        """
        # Create the SET part of the query from the data dictionary
        set_clause = ', '.join(f"{k}='{v}'" for k, v in data.items())
        query = f"UPDATE {table} SET {set_clause}"
        
        # If where condition is provided, append it to the query
        if where:
            conditions = [f"{k}='{v}'" for k, v in where.items()]
            query += " WHERE " + " AND ".join(conditions)
        
        return query