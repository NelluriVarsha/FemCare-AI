import sqlite3
import pandas as pd

conn = sqlite3.connect("users.db")

print("\nACCOUNTS TABLE")
try:
    accounts = pd.read_sql_query(
        "SELECT * FROM accounts",
        conn
    )
    print(accounts)
except Exception as e:
    print(e)

print("\nUSERS TABLE")
try:
    users = pd.read_sql_query(
        "SELECT * FROM users",
        conn
    )
    print(users)
except Exception as e:
    print(e)

print("\nHEALTH_LOGS TABLE")
try:
    logs = pd.read_sql_query(
        "SELECT * FROM health_logs",
        conn
    )
    print(logs)
except Exception as e:
    print(e)

conn.close()