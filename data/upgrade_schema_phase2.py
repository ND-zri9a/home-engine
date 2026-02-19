import sqlite3
import os

db_path = "/home/sphiniix/.openclaw/novlume_workspace/home_engine/data/home.db"

def upgrade_schema_phase2():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Upgrade 'inventory' table with Expiry & Storage Location
    cursor.execute("PRAGMA table_info(inventory)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'expiry_date' not in columns:
        cursor.execute("ALTER TABLE inventory ADD COLUMN expiry_date DATE")
    if 'storage_location' not in columns:
        cursor.execute("ALTER TABLE inventory ADD COLUMN storage_location TEXT DEFAULT 'Pantry'") # Fridge, Freezer, Pantry
    if 'category' not in columns:
        cursor.execute("ALTER TABLE inventory ADD COLUMN category TEXT") # Dairy, Produce, Meat, etc.

    # 2. Upgrade 'recipes' table with Time & Complexity
    cursor.execute("PRAGMA table_info(recipes)")
    columns = [column[1] for column in cursor.fetchall()]

    if 'prep_time_mins' not in columns:
        cursor.execute("ALTER TABLE recipes ADD COLUMN prep_time_mins INTEGER DEFAULT 0")
    if 'cook_time_mins' not in columns:
        cursor.execute("ALTER TABLE recipes ADD COLUMN cook_time_mins INTEGER DEFAULT 0")
    if 'total_time_mins' not in columns:
        cursor.execute("ALTER TABLE recipes ADD COLUMN total_time_mins INTEGER DEFAULT 0")
    if 'difficulty' not in columns:
        cursor.execute("ALTER TABLE recipes ADD COLUMN difficulty TEXT DEFAULT 'Medium'") # Easy, Medium, Hard

    # 3. Create 'price_history' table for Inflation Tracking
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS price_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        price_per_unit REAL NOT NULL,
        date_recorded DATE DEFAULT CURRENT_DATE,
        store_name TEXT,
        FOREIGN KEY (item_name) REFERENCES inventory(item_name)
    )
    ''')

    conn.commit()
    conn.close()
    print("Database Schema Upgraded to Phase 2 (Smart Features).")

if __name__ == "__main__":
    upgrade_schema_phase2()
