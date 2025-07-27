class SQLQueryBuilder:
    @staticmethod
    def select(table, columns='*', where=None):
        query = f"SELECT {', '.join(columns) if isinstance(columns, list) else columns} FROM {table}"
        if where:
            conditions = [f"{key}='{value}'" for key, value in where.items()]
            query += f" WHERE {' AND '.join(conditions)}"
        return query

    @staticmethod
    def insert(table, data):
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{value}'" for value in data.values())
        return f"INSERT INTO {table} ({columns}) VALUES ({values})"

    @staticmethod
    def delete(table, where=None):
        query = f"DELETE FROM {table}"
        if where:
            conditions = [f"{key}='{value}'" for key, value in where.items()]
            query += f" WHERE {' AND '.join(conditions)}"
        return query

    @staticmethod
    def update(table, data, where=None):
        sets = ', '.join(f"{key}='{value}'" for key, value in data.items())
        query = f"UPDATE {table} SET {sets}"
        if where:
            conditions = [f"{key}='{value}'" for key, value in where.items()]
            query += f" WHERE {' AND '.join(conditions)}"
        return query