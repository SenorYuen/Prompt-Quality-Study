class SQLGenerator:
    """
    This class generates SQL statements for common operations on a table, such as SELECT, INSERT, UPDATE, and DELETE.
    """

    def __init__(self, table_name):
        """
        Initialize the table name.
        :param table_name: str
        """
        self.table_name = table_name

    # Generate a SELECT SQL statement based on the specified fields and conditions
    def select(self, fields=None, condition=None):
        # If fields are not specified, select all fields
        if fields is None:
            fields_str = "*"
        else:
            # Convert the list of fields to a comma-separated string
            fields_str = ", ".join(fields)
        
        # Start building the SQL statement
        sql = f"SELECT {fields_str} FROM {self.table_name}"
        
        # If a condition is specified, add the WHERE clause
        if condition is not None:
            sql += f" WHERE {condition};"
        else:
            sql += ";"
        
        return sql

    # Generate an INSERT SQL statement based on the given data
    def insert(self, data):
        # Get the field names and values from the data dictionary
        fields = list(data.keys())
        values = list(data.values())
        
        # Convert the list of fields to a comma-separated string
        fields_str = ", ".join(fields)
        
        # Convert the list of values to a comma-separated string, enclosing each value in single quotes
        values_str = ", ".join(f"'{value}'" for value in values)
        
        # Build the SQL statement
        sql = f"INSERT INTO {self.table_name} ({fields_str}) VALUES ({values_str});"
        
        return sql

    # Generate an UPDATE SQL statement based on the given data and condition
    def update(self, data, condition):
        # Get the field names and new values from the data dictionary
        fields = list(data.keys())
        values = list(data.values())
        
        # Build the SET clause
        set_clause = ", ".join(f"{field} = '{value}'" for field, value in zip(fields, values))
        
        # Build the SQL statement
        sql = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition};"
        
        return sql

    # Generate a DELETE SQL statement based on the given condition
    def delete(self, condition):
        # Build the SQL statement
        sql = f"DELETE FROM {self.table_name} WHERE {condition};"
        
        return sql

    # Generate a SQL statement to select females under a specified age
    def select_female_under_age(self, age):
        # Build the SQL statement
        sql = f"SELECT * FROM {self.table_name} WHERE age < {age} AND gender = 'female';"
        
        return sql

    # Generate a SQL statement to select records within a specified age range
    def select_by_age_range(self, min_age, max_age):
        # Build the SQL statement
        sql = f"SELECT * FROM {self.table_name} WHERE age BETWEEN {min_age} AND {max_age};"
        
        return sql