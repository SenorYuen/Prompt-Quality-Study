# This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements.
class SQLQueryBuilder:

    # Generate the SELECT SQL statement from the given parameters.
    @staticmethod
    def select(table, columns='*', where=None):
        # Initialize the query with the SELECT statement
        query = f"SELECT {columns} FROM {table}"
        
        # Add the WHERE clause if provided
        if where:
            query += f" WHERE {where}"
        
        # Return the generated query
        return query

    # Generate the INSERT SQL statement from the given parameters.
    @staticmethod
    def insert(table, data):
        # Initialize the query with the INSERT statement
        query = f"INSERT INTO {table} ("
        
        # Extract the column names and values from the data
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{value}'" for value in data.values())
        
        # Add the column names and values to the query
        query += f"{columns}) VALUES ({values})"
        
        # Return the generated query
        return query

    # Generate the DELETE SQL statement from the given parameters.
    @staticmethod
    def delete(table, where=None):
        # Initialize the query with the DELETE statement
        query = f"DELETE FROM {table}"
        
        # Add the WHERE clause if provided
        if where:
            query += f" WHERE {where}"
        
        # Return the generated query
        return query

    # Generate the UPDATE SQL statement from the given parameters.
    @staticmethod
    def update(table, data, where=None):
        # Initialize the query with the UPDATE statement
        query = f"UPDATE {table} SET "
        
        # Extract the column names and values from the data
        updates = ', '.join(f"{key} = '{value}'" for key, value in data.items())
        
        # Add the updates to the query
        query += updates
        
        # Add the WHERE clause if provided
        if where:
            query += f" WHERE {where}"
        
        # Return the generated query
        return query

# Example usage:
if __name__ == "__main__":
    print(SQLQueryBuilder.select('users', 'name, email', 'age > 18'))
    print(SQLQueryBuilder.insert('users', {'name': 'John Doe', 'email': 'john@example.com'}))
    print(SQLQueryBuilder.delete('users', 'age < 18'))
    print(SQLQueryBuilder.update('users', {'name': 'Jane Doe', 'email': 'jane@example.com'}, 'id = 1'))