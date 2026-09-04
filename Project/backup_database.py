import shutil
from datetime import datetime

# CREATE TIMESTAMP
time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# BACKUP FILE NAME
backup_name = f"backup_{time_now}.db"

# COPY DATABASE
shutil.copy(
    "payroll.db",
    backup_name
)

print(f"Backup created: {backup_name}")