import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Number of rows for the dummy dataset
num_rows = 500

# Generate random dates within a specific range
start_date = datetime(2023, 1, 1)
end_date = start_date + timedelta(days=365)
date_range = pd.date_range(start_date, end_date).to_pydatetime().tolist()

# Generate random times
time_range = pd.date_range("08:00", "21:00", freq="H").time

dummy_data = {
    'reservation_id': np.arange(1, num_rows + 1),
    'unit_id': np.random.randint(1, 100, size=num_rows),
    'unit_type': np.random.choice(['type1', 'type2', 'type3', 'type4'], size=num_rows),
    'date': np.random.choice(date_range, size=num_rows),
    'head_count': np.random.randint(1, 150, size=num_rows),
    'host_user': np.random.randint(100000, 999999, size=num_rows),
    'option1': [None] * num_rows,
    'option2': [None] * num_rows,
    'prop_id': np.random.randint(1, 100, size=num_rows),
    'reserve_code': np.random.randint(1, 5, size=num_rows),
    'slot_length': np.random.choice([10, 15, 20], size=num_rows),
    'slot_minutes': np.random.choice([30, 60, 90], size=num_rows),
    'special_req': np.random.choice(['None', 'Confirmed', 'Pending', 'Booked'], size=num_rows),
    'status': np.random.choice(['Booked', 'Pending', 'Cancelled'], size=num_rows),
    'time': [random.choice(time_range) for _ in range(num_rows)],
    'time_slots': np.random.choice([1, 2, 3], size=num_rows),
    'user_id': np.random.randint(1000, 9999, size=num_rows)
}

# Create a DataFrame
dummy_df = pd.DataFrame(dummy_data)

# Save the DataFrame to a CSV file
dummy_df.to_csv('dummy_reservations.csv', index=False)

print("Dummy dataset generated and saved to 'dummy_reservations.csv'")
print(dummy_df.head())
