import sqlite3
import os

db_path = "/home/sphiniix/.openclaw/novlume_workspace/home_engine/data/home.db"

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Table for general inventory (current stock)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT UNIQUE NOT NULL,
        quantity REAL DEFAULT 0,
        unit TEXT NOT NULL, -- g, L, pack, etc.
        avg_price_per_unit REAL DEFAULT 0,
        total_protein_per_unit REAL DEFAULT 0,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Table for individual purchases (from invoices)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        quantity REAL NOT NULL,
        unit TEXT NOT NULL,
        cost_dh REAL NOT NULL,
        invoice_id TEXT, -- For tracking back to a photo/receipt
        purchase_date DATE DEFAULT CURRENT_DATE,
        FOREIGN KEY (item_name) REFERENCES inventory(item_name)
    )
    ''')

    # Table for recipes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_name TEXT UNIQUE NOT NULL,
        description TEXT,
        serving_size INTEGER DEFAULT 1,
        total_estimated_cost_dh REAL DEFAULT 0,
        total_estimated_protein REAL DEFAULT 0
    )
    ''')

    # Table for recipe ingredients (atomic links to inventory)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipe_ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_id INTEGER,
        inventory_item_name TEXT,
        quantity_needed REAL NOT NULL,
        unit TEXT NOT NULL,
        FOREIGN KEY (recipe_id) REFERENCES recipes(id),
        FOREIGN KEY (inventory_item_name) REFERENCES inventory(item_name)
    )
    ''')

    # Table for micro-steps in a recipe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipe_steps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_id INTEGER,
        step_number INTEGER NOT NULL,
        instruction TEXT NOT NULL,
        FOREIGN KEY (recipe_id) REFERENCES recipes(id)
    )
    ''')

    # Table for logging meals eaten (to track consumption)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS meal_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_id INTEGER,
        date_eaten TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        actual_cost_dh REAL,
        actual_protein REAL,
        FOREIGN KEY (recipe_id) REFERENCES recipes(id)
    )
    ''')

    conn.commit()
    conn.close()
    print(f"Database initialized at {db_path}")

if __name__ == "__main__":
    init_db()
