import random
from datetime import datetime, timedelta




start_date = datetime(2021, 1, 1)
end_date = datetime(2024, 11, 20)

random_days = random.randint(0, (end_date - start_date).days)
random_date = start_date + timedelta(days=random_days)
print(random_date)
print(random_date + timedelta(days=6*30))