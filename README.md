# Flask Expense Tracker Application

A simple Expense Tracker Web Application built using Flask and SQLite.

---

## Features

* Add Expenses
* View Expenses
* Update Expenses
* Delete Expenses
* SQLite Database Integration
* Flask Routing
* HTML Templates

---

## Technologies Used

* Python
* Flask
* SQLite
* HTML
* CSS

---

## CRUD Operations

### Create

Users can add new expenses.

### Read

Users can view all saved expenses.

### Update

Users can edit expense details.

### Delete

Users can remove expenses from the database.

---

## Expense Details

Each expense contains:

| Field    | Description      |
| -------- | ---------------- |
| Name     | Expense name     |
| Category | Expense category |
| Amount   | Expense amount   |
| Date     | Expense date     |

---

## Project Structure

```text
ExpenseTracker/
│
├── app.py
├── expenses.db
│
└── templates/
    ├── expense.html
    ├── view.html
    └── update.html
```

---

## Database Information

Database Name:

```text
expenses.db
```

Table Name:

```sql
expenses
```

Columns:

| Column   | Type    |
| -------- | ------- |
| id       | INTEGER |
| name     | TEXT    |
| category | TEXT    |
| amount   | REAL    |
| date     | TEXT    |

---

## Installation

### Clone Repository

```bash
https://github.com/kavyasrichittiboina-hue/Flask-Expense-Tracker-Application.git
```

---

### Move Into Project Folder

```bash
cd flask-expense-tracker
```

---

### Install Flask

```bash
pip install flask
```

---

## Run Application

```bash
python app.py
```

---

## Open Browser

```text
http://127.0.0.1:5000/
```

---

## Flask Routes

| Route          | Purpose           |
| -------------- | ----------------- |
| `/`            | Add expenses      |
| `/view`        | View all expenses |
| `/update/<id>` | Update expense    |
| `/delete/<id>` | Delete expense    |

---

## SQL Operations Used

### INSERT

```sql
INSERT INTO expenses(name,category,amount,date)
VALUES(?,?,?,?)
```

### SELECT

```sql
SELECT * FROM expenses
```

### UPDATE

```sql
UPDATE expenses
SET name=?,category=?,amount=?,date=?
WHERE id=?
```

### DELETE

```sql
DELETE FROM expenses WHERE id=?
```

---

## Future Improvements

* Expense charts
* Monthly reports
* User login system
* Search functionality
* Expense filtering
* Export to Excel/PDF

---

## Author

Created for Flask CRUD and SQLite practice.

