# Database

This folder contains the SQLite database used in the Mutual Fund Analytics project.

## Database File

* `bluestock_mf.db` — SQLite database containing the cleaned and processed mutual fund datasets.

## Database Loading

The cleaned datasets were loaded into SQLite using **SQLAlchemy** and **Pandas**.

Example:

```python
engine = create_engine("sqlite:///bluestock_mf.db")

df.to_sql("fact_nav", engine, if_exists="replace", index=False)
```

The database provides a structured storage layer for SQL analysis and analytics.
