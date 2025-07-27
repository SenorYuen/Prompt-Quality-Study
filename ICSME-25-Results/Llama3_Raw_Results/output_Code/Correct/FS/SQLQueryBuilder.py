class SQLQueryBuilder:
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """

    @staticmethod
    def select(table, columns='*', where=None):
        # Start building the SELECT query
        query = "SELECT "
        
        # If columns is a list, join the columns with a comma
        if isinstance(columns, list):
            query += ", ".join(columns)
        else:
            query += columns
        
        # Specify the table
        query += f" FROM {table}"
        
        # If a WHERE condition is provided, add it to the query
        if where:
            query += " WHERE "
            conditions = []
            for key, value in where.items():
                # Append each condition to the list
                conditions.append(f"{key}='{value}'")
            # Join the conditions with AND
            query += " AND ".join(conditions)
        
        return query

    @staticmethod
    def insert(table, data):
        # Start building the INSERT query
        query = f"INSERT INTO {table} "
        
        # Get the columns and values from the data dictionary
        columns = list(data.keys())
        values = list(data.values())
        
        # Add the columns to the query
        query += f"({', '.join(columns)}) "
        
        # Add the values to the query
        query += f"VALUES ({', '.join([f"'{value}'" for value in values])})"
        
        return query

    @staticmethod
    def delete(table, where=None):
        # Start building the DELETE query
        query = f"DELETE FROM {table}"
        
        # If a WHERE condition is provided, add it to the query
        if where:
            query += " WHERE "
            conditions = []
            for key, value in where.items():
                # Append each condition to the list
                conditions.append(f"{key}='{value}'")
            # Join the conditions with AND
            query += " AND ".join(conditions)
        
        return query

    @staticmethod
    def update(table, data, where=None):
        # Start building the UPDATE query
        query = f"UPDATE {table} SET "
        
        # Get the columns and values from the data dictionary
        columns = list(data.keys())
        values = list(data.values())
        
        # Add the columns and values to the query
        query += ", ".join([f"{column}='{value}'" for column, value in zip(columns, values)])
        
        # If a WHERE condition is provided, add it to the query
        if where:
            query += " WHERE "
            conditions = []
            for key, value in where.items():
                # Append each condition to the list
                conditions.append(f"{key}='{value}'")
            # Join the conditions with AND
            query += " AND ".join(conditions)
        
        return query