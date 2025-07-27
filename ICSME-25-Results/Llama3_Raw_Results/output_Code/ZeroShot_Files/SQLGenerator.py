class SQLGenerator:
    def __init__(self, table_name):
        # Initialize the table name
        self.table_name = table_name

    def select(self, fields=None, condition=None):
        # Start building the SELECT statement
        sql = "SELECT "
        
        # If fields are specified, use them; otherwise, use '*'
        if fields:
            # Convert the fields list to a comma-separated string
            sql += ", ".join(fields)
        else:
            sql += "*"
        
        # Specify the table name
        sql += f" FROM {self.table_name}"
        
        # If a condition is specified, add it to the statement
        if condition:
            sql += f" WHERE {condition}"
        
        # Return the generated SQL statement
        return sql

    def insert(self, data):
        # Start building the INSERT statement
        sql = f"INSERT INTO {self.table_name} "
        
        # Get the column names and values from the data dictionary
        columns = list(data.keys())
        values = list(data.values())
        
        # Add the column names to the statement
        sql += f"({', '.join(columns)}) "
        
        # Add the VALUES keyword and the values
        sql += "VALUES ("
        # Convert the values to a comma-separated string, wrapping each value in single quotes
        sql += ", ".join(f"'{value}'" for value in values)
        sql += ")"
        
        # Return the generated SQL statement
        return sql

    def update(self, data, condition):
        # Start building the UPDATE statement
        sql = f"UPDATE {self.table_name} "
        
        # Add the SET keyword and the column-value pairs
        sql += "SET "
        # Convert the data dictionary to a comma-separated string of column-value pairs
        sql += ", ".join(f"{column} = '{value}'" for column, value in data.items())
        
        # Add the WHERE keyword and the condition
        sql += f" WHERE {condition}"
        
        # Return the generated SQL statement
        return sql

    def delete(self, condition):
        # Start building the DELETE statement
        sql = f"DELETE FROM {self.table_name} "
        
        # Add the WHERE keyword and the condition
        sql += f"WHERE {condition}"
        
        # Return the generated SQL statement
        return sql

    def select_female_under_age(self, age):
        # Generate a SQL statement to select females under a specified age
        # Assuming the table has columns 'gender' and 'age'
        return self.select(condition=f"gender = 'female' AND age < {age}")

    def select_by_age_range(self, min_age, max_age):
        # Generate a SQL statement to select records within a specified age range
        # Assuming the table has a column 'age'
        return self.select(condition=f"age >= {min_age} AND age <= {max_age}")