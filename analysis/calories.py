import json
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def return_plot():
    """
    Returns a matplotlib plot showing calories consumed in the last 7 days.
    Handles missing data gracefully.
    """
    # Load JSON data
    try:
        with open("db/database.json", "r") as file:
            data = json.load(file)
    except Exception as e:
        raise RuntimeError(f"❌ Failed to load JSON: {e}")

    if not data:
        raise ValueError("⚠️ No data found in database.json")

    # Convert data into DataFrame
    try:
        df = pd.Series(data, name='calories').rename_axis('date').reset_index()
        df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
    except Exception as e:
        raise ValueError(f"❌ Error parsing data or dates: {e}")

    # Get last 7 days
    today = datetime.datetime.now().date()
    week = today - datetime.timedelta(days=6)
    all_days = pd.date_range(start=week, end=today)

    # Filter to only the last 7 days and convert date to just date (no time)
    df_last_week = df[df['date'].dt.date >= week]
    df_last_week['date'] = df_last_week['date'].dt.date  # Ensure date type

    # Create a DataFrame for all 7 days
    filled = pd.DataFrame({'date': all_days.date})

    # Merge and fill missing calories with 0
    filled = filled.merge(df_last_week, on='date', how='left').fillna({'calories': 0})
    filled['date'] = pd.to_datetime(filled['date'])

    # Plot
    plt.figure(figsize=(8, 4))
    plt.bar(x=filled['date'].dt.strftime('%d-%m'), height=filled['calories'])
    plt.plot(filled['date'].dt.strftime('%d-%m'), filled['calories'],
             color='orange', marker='o', linestyle='-', linewidth=2, ms=5)
    plt.xlabel('Date')
    plt.ylabel('Calories')
    plt.title('Calories Consumed in the Last 7 Days')
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt.gcf()
