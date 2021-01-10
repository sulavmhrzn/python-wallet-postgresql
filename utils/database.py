import psycopg2 as pg2


class Database:
    def __init__(self, database, user, password, host="localhost", port=5432):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.cursor = None

    def __enter__(self):
        self.connection = pg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )
        self.cursor = self.connection.cursor()
        print("ENTEERRR")
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.commit()
        self.connection.close()
        print("EXIT")