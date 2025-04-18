# GoRest CSV Reporting Tool

A small Python utility that pulls user data from the [GoRest public API](https://gorest.co.in/public/v2/users) and generates two CSV reports:

1. **active_test_users.csv** – a list of all **active** users whose emails end in `.test`.  
2. **domain_counts.csv** – a count of **all** users, grouped by the suffix of their email domain (e.g. `com`, `org`, `io`).

---

## 🚀 Features

- **Pagination‑aware**: will fetch **all** pages of results from the GoRest API.
- **Progress logging**: prints “Page N: Retrieved X users” as it goes.
- **Zero dependencies** beyond `requests` (no external CSV or parsing libs).
- **.gitignore** included to keep your repo clean of byte‑compiled files, virtual environments, generated CSVs, etc.

---

## 🛠️ Prerequisites

- Python 3.7+  
- [requests](https://pypi.org/project/requests/) library

---

## 📝 Installation

1. Clone your repository:  
   ```bash
   git clone https://github.com/hshanka/gorest2csv.git
   cd gorest2csv
   ```
2. Install dependencies:
   ```
   pip install requests
   ```
3. Run the script to fetch all users and write both reports:
   ```
   python3 gorest_report.py
   ```

You’ll see console output like:
```
Page 1: Retrieved 100 users
Page 2: Retrieved 100 users
Page 3: Retrieved 45 users
No more users to fetch; ending pagination.
Total users fetched: 245

Writing filtered active .test users to active_test_users.csv...
Done: active_test_users.csv

Counting domains and writing to domain_counts.csv...
Done: domain_counts.csv
```
