import sqlite3
import os

db_path = "/home/sphiniix/.openclaw/novlume_workspace/home_engine/data/home.db"

def expand_schema():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Subscriptions Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service_name TEXT UNIQUE NOT NULL,
        cost_dh REAL NOT NULL,
        billing_cycle TEXT NOT NULL, -- Monthly, Yearly
        next_payment_date DATE NOT NULL,
        category TEXT -- Entertainment, Software, Gym, etc.
    )
    ''')

    # 2. Bank / Wallet Balance Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS finance_summary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        current_balance_dh REAL DEFAULT 0,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Initialize balance if empty
    cursor.execute("SELECT COUNT(*) FROM finance_summary")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO finance_summary (current_balance_dh) VALUES (0)")

    # 3. Enhanced Meal Log (Adding Cooking Duration)
    # Check if duration column exists, if not add it
    cursor.execute("PRAGMA table_info(meal_log)")
    columns = [column[1] for column in cursor.fetchall()]
    if 'cooking_duration_mins' not in columns:
        cursor.execute("ALTER TABLE meal_log ADD COLUMN cooking_duration_mins INTEGER")

    conn.commit()
    conn.close()
    print("Database schema expanded successfully.")

if __name__ == "__main__":
    expand_schema()
