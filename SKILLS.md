# SKILLS.md - Home Engine Procedures

> This file defines exactly how I handle kitchen and finance tasks.

## 🛡️ Input Integrity Protocol (CRITICAL)

**Rule #1: No Guessing.**
- Every input (Purchase, Recipe, Consumption) **MUST** have complete data.
- **Missing Data:** If a receipt scan is blurry or a unit is missing (e.g., "2 Milk"), I **MUST** ask: "Is that 2 Liters or 2 Bottles? What is the size?"
- **Mandatory Fields:**
  - `Item Name` (Standardized)
  - `Quantity` (Exact numeric)
  - `Unit` (Standardized: g, ml, L, kg, piece)
  - `Price` (Total DH paid)
  - `Expiry Date` (New! If visible, extract it)

**Rule #2: Atomic Verification.**
- Before logging a meal, I check if ingredients exist.
- If the database says you have 0 Eggs, but you are cooking an Omelet, I will ask: *"I thought you had 0 Eggs. Did you buy more? Please send the receipt first so I can track the cost."*

---

## 🧾 Processing Invoices
1. **Analyze:** Use Vision to read the receipt.
2. **Extract:** Get Date, Store Name, Item Name, Quantity, Unit, Price (DH), and **Expiry Date** (if present).
3. **Database:** 
   - Add entry to `purchases`.
   - Update `price_history` to track inflation.
   - Upsert item in `inventory` with new quantity and location.
   - Calculate new `avg_price_per_unit`.
4. **Report:** Update `STATUS.md`.

## 🥘 Cooking a Recipe
1. **Selection:** User picks a recipe.
2. **Time Check:** *New!* "This takes 45 mins. Do you have time?"
3. **Verification:** Check `inventory` for quantity AND expiry (use oldest first).
4. **Guidance:** Present `recipe_steps` one by one.
5. **Completion:** On "Done", trigger `meal_log` entry and subtract ingredients from `inventory`.

## 📦 Nutrition Tracking
1. **Label Scan:** When a product label is provided, extract Protein/100g.
2. **Unit Conversion:** Convert to `total_protein_per_unit` in `inventory`.
3. **Calculation:** Recipes now automatically show "Total Protein" based on ingredients used.

## 🧠 Smart Analysis (Phase 2)
1. **Inflation Alert:** If `price_per_unit` is > 10% higher than last time, warn the user.
2. **Waste Alert:** Once a week, check `expiry_date` in `inventory` and suggest recipes to use dying food.

---

## Technical Maintenance
- **Sync:** After every major change, I will `git commit` and `git push` to the repo.
- **Reporting:** Keep `STATUS.md` as the source of truth for the human.
