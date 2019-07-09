### SQL practice today!

We'll use the Chinook_Sqlite.sqlite database in this directory to run a few queries. First import libraries and connect to the database.

`import sqlite3`

`import pandas as pd`

`conn = sqlite3.connect('Chinook_Sqlite.sqlite')`

`c = conn.cursor`

Check out the tables in the database

`c.execute('''SELECT name FROM sqlite_master
        WHERE type ='table' ''')`
        
`tables_df = pd.DataFrame(c.fetchall())`

`df.columns = [i[0] for i in c.description]`

`tables_df`

1. Who are the top 3 customers (last name) by average money spent per purchase and how many individual purchases did each make? (Check Invoice and Customer tables)

2. What are the top 5 genres (genre name) by most total track sales (by quantity)? And how many sales were made in each of those genres? (Check InvoiceLine and Track tables)

3. [Stretch] What are the top 5 countries (use BillingCountry) for rock album sales (by quantity sold)?