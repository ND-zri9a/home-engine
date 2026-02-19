# SKILLS.md - Home Engine Procedures

> This file defines exactly how I handle kitchen and finance tasks.

## 🧾 Processing Invoices
1. **Analyze:** Use Vision to read the receipt.
2. **Extract:** Get Date, Store Name, Item Name, Quantity, Unit, and Price (DH).
3. **Database:** 
   - Add entry to `purchases`.
   - Upsert (Update or Insert) item in `inventory`.
   - Calculate new `avg_price_per_unit`.
4. **Report:** Update `STATUS.md`.

## 🥘 Cooking a Recipe
1. **Selection:** User picks a recipe.
2. **Verification:** Check `inventory` to see if we have enough ingredients.
3. **Guidance:** Present `recipe_steps` one by one.
4. **Completion:** On "Done", trigger `meal_log` entry and subtract ingredients from `inventory`.

## 📦 Nutrition Tracking
1. **Label Scan:** When a product label is provided, extract Protein/100g.
2. **Unit Conversion:** Convert to `total_protein_per_unit` in `inventory`.
3. **Calculation:** Recipes now automatically show "Total Protein" based on ingredients used.

---

## Technical Maintenance
- **Sync:** After every major change, I will `git commit` and `git push` to the repo.
- **Reporting:** Keep `STATUS.md` as the source of truth for the human.
