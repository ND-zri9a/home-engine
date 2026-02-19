# 🗄️ Home Engine Database Schema

This schema is designed to be **atomic**. Every gram and every Dirham is tracked through these connected tables.

## 1. `inventory` (The "Fridge" State)
Tracks what you currently have in stock.
| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER | Unique ID |
| `item_name` | TEXT | Primary name (e.g., "Chicken Breast") |
| `quantity` | REAL | Current amount (e.g., 500) |
| `unit` | TEXT | g, ml, L, kg, pack, piece |
| `avg_price_per_unit` | REAL | Calculated cost per unit (DH/unit) |
| `total_protein_per_unit` | REAL | Grams of protein per unit |
| `last_updated` | TIMESTAMP | Last time the stock was changed |

## 2. `purchases` (The Ledger)
Every item from every invoice is logged here.
| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER | Unique ID |
| `item_name` | TEXT | Linked to inventory |
| `quantity` | REAL | Amount bought |
| `unit` | TEXT | Unit bought in |
| `cost_dh` | REAL | Total price paid for this item |
| `invoice_id` | TEXT | Reference to the photo in `/vault/` |
| `purchase_date` | DATE | Date of shopping |

## 3. `recipes` (The Cookbook)
Core recipe information.
| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER | Unique ID |
| `recipe_name` | TEXT | e.g., "Beef Tagine" |
| `description` | TEXT | Brief overview |
| `serving_size` | INTEGER | Number of people it feeds |
| `total_estimated_cost_dh`| REAL | Auto-calculated cost based on inventory |
| `total_estimated_protein`| REAL | Auto-calculated protein |

## 4. `recipe_ingredients` (The Atomic Links)
Connects recipes to specific items in your inventory.
| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER | Unique ID |
| `recipe_id` | INTEGER | Linked to `recipes` |
| `inventory_item_name` | TEXT | Linked to `inventory` |
| `quantity_needed` | REAL | Amount required |
| `unit` | TEXT | Unit (must match inventory unit) |

## 5. `recipe_steps` (Micro-Instructions)
The step-by-step cooking guide.
| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER | Unique ID |
| `recipe_id` | INTEGER | Linked to `recipes` |
| `step_number` | INTEGER | Sequence (1, 2, 3...) |
| `instruction` | TEXT | The micro-step text |

## 6. `meal_log` (Consumption Tracking)
Every time you eat, it's recorded here to update inventory.
| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER | Unique ID |
| `recipe_id` | INTEGER | Which recipe you ate |
| `date_eaten` | TIMESTAMP | Date/Time of consumption |
| `actual_cost_dh` | REAL | Final cost based on used ingredients |
| `actual_protein` | REAL | Final protein count |
