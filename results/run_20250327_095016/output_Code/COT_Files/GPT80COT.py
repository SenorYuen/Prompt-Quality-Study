class SQLQueryBuilder:
    @staticmethod
    def select(table, columns='*', where=None):
        columns_part = ', '.join(columns) if isinstance(columns, list) else columns
        where_part = ''
        if where:
            where_conditions = [f"{key}='{value}'" for key, value in where.items()]
            where_part = f" WHERE {' AND '.join(where_conditions)}"
        return f"SELECT {columns_part} FROM {table}{where_part}"

    @staticmethod
    def insert(table, data):
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{value}'" for value in data.values())
        return f"INSERT INTO {table} ({columns}) VALUES ({values})"

    @staticmethod
    def delete(table, where=None):
        where_part = ''
        if where:
            where_conditions = [f"{key}='{value}'" for key, value in where.items()]
            where_part = f" WHERE {' AND '.join(where_conditions)}"
        return f"DELETE FROM {table}{where_part}"

    @staticmethod
    def update(table, data, where=None):
        set_part = ', '.join(f"{key}='{value}'" for key, value in data.items())
        where_part = ''
        if where:
            where_conditions = [f"{key}='{value}'" for key, value in where.items()]
            where_part = f" WHERE {' AND '.join(where_conditions)}"
        return f"UPDATE {table} SET {set_part}{where_part}"