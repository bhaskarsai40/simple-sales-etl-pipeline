# Sales Data ETL Pipeline
A simple Python-based ETL (Extract, Transform, Load) pipeline that processes messy sales data and loads it into a SQL database.

### 🛠️ Technologies
- **Python:** Core logic and processing.
- **Pandas:** Data cleaning and validation.
- **SQLite:** Relational database storage.

### 🚀 How it Works
1. **Extract:** Reads raw sales data from a CSV file.
2. **Transform:** - Handles missing price values by calculating averages.
   - Validates data by removing negative quantities.
   - Standardizes date formats.
3. **Load:** Automatically creates a SQL table and inserts the cleaned records.
