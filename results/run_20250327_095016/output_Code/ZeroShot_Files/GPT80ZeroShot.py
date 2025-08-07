class SQLQueryBuilder:

    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the name of the table.
        :param columns: list or str, the columns to select.
        :param where: str, the WHERE clause.
        :return query: str, the SQL query statement.
        """
        # Convert columns to a comma-separated string if it's a list
        if isinstance(columns, list):
            columns = ', '.join(columns)
        
        # Start building the query
        query = f"SELECT {columns} FROM {table}"
        
        # Add the WHERE clause if provided
        if where:
            query += f" WHERE {where}"
        
        return query

    @staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the name of the table.
        :param data: dict, the data to insert (column-value pairs).
        :return query: str, the SQL insert statement.
        """
        # Extract columns and values from the data dictionary
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{v}'" for v in data.values())
        
        # Build the insert query
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        
        return query

    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the name of the table.
        :param where: str, the WHERE clause.
        :return query: str, the SQL delete statement.
        """
        # Start building the delete query
        query = f"DELETE FROM {table}"
        
        # Add the WHERE clause if provided
        if where:
            query += f" WHERE {where}"
        
        return query

    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the name of the table.
        :param data: dict, the data to update (column-value pairs).
        :param where: str, the WHERE clause.
        :return query: str, the SQL update statement.
        """
        # Create the SET part of the query from the data dictionary
        set_clause = ', '.join(f"{k}='{v}'" for k, v in data.items())
        
        # Start building the update query
        query = f"UPDATE {table} SET {set_clause}"
        
        # Add the WHERE clause if provided
        if where:
            query += f" WHERE {where}"
        
        return query