# 🏠 Home Engine

**Your Personal Kitchen & Finance Assistant.** Isolated, Atomic, and Automated.

> **Mission:** To automate the mental load of home management. You shouldn't have to remember how many grams of chicken are left or how much you spent on eggs last month. I do the tracking; you do the living.

---

## 🚀 Core Workflows (Input-Process-Output)

### 1. The Shopping Trip (Restocking)
**Goal:** Update your fridge and track your spending.
- **INPUT:** You send a **Photo** of a supermarket receipt (e.g., Marjane/Carrefour).
- **PROCESS:**
  1. **Vision/Parsing:** I scan the image to extract Store Name, Date, Line Items, and Prices.
  2. **Normalization:** I convert units (e.g., "1 KG" -> `1000g`) and match items to the database ID.
  3. **Database Transaction:**
     - `purchases`: Logs the expense.
     - `inventory`: Updates stock (`current_qty + new_qty`).
     - `finance_summary`: Deducts total cost from your balance.
  4. **Averaging:** I recalculate the *Average Cost per Gram* based on price fluctuations.
- **OUTPUT:** "✅ **Receipt Processed.** Added 1kg Chicken. 💰 **Spending:** 60 DH deducted. 📊 **Insight:** Chicken is 5% cheaper than last time."

### 2. The Cooking Session (Consumption)
**Goal:** Cook a meal and automatically update inventory.
- **INPUT:** "Guide me step-by-step through the Beef Tagine."
- **PROCESS:**
  1. **Availability Check:** I verify you have enough ingredients (e.g., 500g Beef, 2 Onions).
  2. **Guidance Loop:** I serve one instruction at a time from `recipe_steps`.
  3. **Completion Trigger:** On "Done", I execute a **Consumption Transaction**.
  4. **Deduction:**
     - `inventory`: Beef decreases by 500g.
     - `meal_log`: Records the meal.
     - `finance_summary`: Calculates the *Real Cost* of the meal based on ingredient prices.
- **OUTPUT:** "👨‍🍳 **Bon Appétit!** Meal logged. 📉 **Stock Update:** 500g Beef remaining. 💡 **Cost:** This meal cost 45 DH."

### 3. The Analysis (Questions)
**Goal:** Answer complex questions about habits and money.
- **INPUT:** "How much do I spend on Protein per week?"
- **PROCESS:** I generate a SQL query to aggregate costs from `purchases` for the 'Protein' category over the last 7 days.
- **OUTPUT:** "🥩 **Weekly Protein Spend:** 250 DH. 📅 **Trend:** +20 DH vs average."

### 4. The Bank Reconciliation
**Goal:** Ensure digital balance matches real bank account.
- **INPUT:** "Here is my bank statement PDF."
- **PROCESS:** I extract lines, match expenses to `subscriptions` or categories, and reconcile `finance_summary` with the closing balance.
- **OUTPUT:** "🏦 **Bank Synced.** Current Balance: 12,450 DH. ⚠️ **Alert:** New subscription detected."

---

## 📁 Directory Structure
- `/data`: SQLite database (`home.db`) and maintenance scripts.
- `/recipes`: Atomic recipe definitions and micro-steps.
- `/vault`: Storage for original invoice images and product labels.
- `STATUS.md`: Real-time dashboard of your kitchen.
- `SCHEMA.md`: Technical details of the data structure.
- `DB_QUESTIONS.md`: A history of every question the user expects the database to answer.

---

## 📊 Features
- **Atomic Inventory Tracking:** Tracks every gram and milliliter in your kitchen.
- **Financial Ledger:** Links every grocery item to its real cost in Moroccan Dirhams (DH).
- **Micro-Step Recipes:** Automated cooking guidance with instant inventory deduction.
- **Vision Integration:** Scan invoices and nutrition labels to update the database.
- **Bank Integration:** Track total wealth and reconcile with statements.
- **Habit Analysis:** Learn what you eat and when to predict shopping needs.

---\n*Created and managed by your AI Assistant.*
