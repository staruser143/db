
# main.py
from models import customers, create_tables, User, Address
from db_operations import fetch_users_with_pagination,insert_records, fetch_records, fetch_users_with_addresses,execute_raw_sql

import logging

# Enable SQLAlchemy logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)  # Adjust the logging level as needed


if __name__ == '__main__':
 # Ensure tables are created
    create_tables()

    # Create records
    records = [
        customers(id=1, name='Alice', age=30),
        customers(id=2, name='Bob', age=25),
        customers(id=3, name='Charlie', age=35)
    ]

    # Insert records
    #
    #insert_records(records)
    # Fetch and print records
    fetched_records = fetch_records()
    for record in fetched_records:
        print(f"Fetched -> id: {record.id}, name: {record.name}, age: {record.age}")


     #Create records
    users = [
        User(id=1, name='Alice', age=30),
        User(id=2, name='Bob', age=25)
    ]

    addresses = [
        Address(id=1, user_id=1, address='123 Main St'),
        Address(id=2, user_id=1, address='456 Maple Ave'),
        Address(id=3, user_id=2, address='789 Oak Dr')
    ]

    # Insert records
    #insert_records(users)
    #nsert_records(addresses)

    # Fetch and print joined records
    #fetch_users_with_addresses()
  # Execute raw SQL query
    sql_query = """
    SELECT u.name, u.age,a.address
    FROM users u
    JOIN addresses a ON u.id = a.user_id
    WHERE u.age > :age
    """
    params = {'age': 20}
    execute_raw_sql(sql_query, params)


 # Fetch and print records with pagination
    offset = 1
    limit = 2
    print(f"Fetching users with offset {offset} and limit {limit}")
    fetch_users_with_pagination(offset, limit)

