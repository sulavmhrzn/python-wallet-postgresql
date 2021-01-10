import psycopg2
from utils.database import Database
from utils.exceptions import NegetiveAmount

database_name = "pywallet"
user = "postgres"
password = "postgres"

database = Database(database_name, user, password)


def create_table():
    """ Creates a table named wallet """
    with database as cur:
        wallet_query = """
        create table wallet(
            wallet_id serial primary key,
            total_amount integer default 0,
            amount_added integer default 0 check(amount_added >= 0),
            amount_spent integer default 0 check(amount_spent <= total_amount)
        )
        """
        try:
            cur.execute(wallet_query)
            print("Table created successfully")
        except psycopg2.Error as e:
            raise e


def create_account():
    """Creates account inside wallet table
    uses serial data type to auto increase the primary key
    """
    with database as cur:
        query = """
        insert into wallet(total_amount)
        values(0)
        """
        fetch_query = """ select * from wallet"""
        try:
            cur.execute(query)
            cur.execute(fetch_query)
            results = cur.fetchall()
            print("Your wallet id is: {}".format(results[-1][0]))
        except psycopg2.Error as e:
            raise e


def add_amount(wallet_id, amount):
    with database as cur:
        query = """
        update wallet
        set amount_added = amount_added + (%s),
            total_amount = total_amount + (%s)
        where wallet_id = (%s)
        """
        try:
            if amount < 0:
                raise NegetiveAmount("Amount must not be negetive")
            cur.execute(query, (amount, amount, wallet_id))
        except psycopg2.Error as e:
            raise e


def spend_amount(wallet_id, amount):
    with database as cur:
        query = """
        update wallet
        set amount_spent = amount_spent + (%s),
            total_amount = total_amount - (%s)
        where wallet_id = (%s)
        """
        try:
            if amount < 0:
                raise NegetiveAmount("Amount must not be negetive")
            cur.execute(query, (amount, amount, wallet_id))
        except psycopg2.Error as e:
            raise e


def view_amounts(wallet_id):
    with database as db:
        query = """
        SELECT * from wallet
        where wallet_id = (%s)
        """
        try:
            db.execute(query, (wallet_id,))
            result = db.fetchone()
            return result
        except psycopg2.Error as e:
            raise e


def drop_table():
    with database as cur:
        query = """drop table wallet"""
        cur.execute(query)
