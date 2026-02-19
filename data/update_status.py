import sqlite3
from datetime import datetime

db_path = "/home/sphiniix/.openclaw/novlume_workspace/home_engine/data/home.db"
status_path = "/home/sphiniix/.openclaw/novlume_workspace/home_engine/STATUS.md"

def update_status():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get inventory count
    cursor.execute("SELECT COUNT(*) FROM inventory")
    inv_count = cursor.fetchone()[0]

    # Get total spent
    cursor.execute("SELECT SUM(cost_dh) FROM purchases")
    total_spent = cursor.fetchone()[0] or 0.0

    # Get recipe count
    cursor.execute("SELECT COUNT(*) FROM recipes")
    recipe_count = cursor.fetchone()[0]

    # Get last 5 purchases
    cursor.execute("SELECT item_name, quantity, unit, cost_dh, purchase_date FROM purchases ORDER BY purchase_date DESC LIMIT 5")
    last_purchases = cursor.fetchall()

    # Get last 5 meals
    cursor.execute("""
        SELECT r.recipe_name, m.date_eaten, m.actual_cost_dh 
        FROM meal_log m 
        JOIN recipes r ON m.recipe_id = r.id 
        ORDER BY m.date_eaten DESC LIMIT 5
    """)
    last_meals = cursor.fetchall()

    conn.close()

    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    with open(status_path, "w") as f:
        f.write("# 🏠 Home Engine Dashboard\n\n")
        f.write("Welcome to your Home Assistant dashboard. This file provides a real-time summary of your kitchen inventory and financial tracking.\n\n")
        f.write("## 📊 Current Status\n")
        f.write(f"- **Total Inventory Items:** {inv_count}\n")
        f.write(f"- **Total Spent (DH):** {total_spent:.2f} DH\n")
        f.write(f"- **Recipes Available:** {recipe_count}\n\n")

        f.write("## 🛒 Last 5 Purchases\n")
        if last_purchases:
            for p in last_purchases:
                f.write(f"- {p[4]}: {p[0]} ({p[1]} {p[2]}) - {p[3]:.2f} DH\n")
        else:
            f.write("*No purchases logged yet.*\n\n")

        f.write("## 🥘 Recent Meals\n")
        if last_meals:
            for m in last_meals:
                f.write(f"- {m[1]}: {m[0]} - {m[2]:.2f} DH\n")
        else:
            f.write("*No meals logged yet.*\n\n")

        f.write(f"---\n*Last updated: {now}*\n")

if __name__ == "__main__":
    update_status()
