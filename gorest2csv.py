#!/usr/bin/env python3
"""
SE Phone Coding Screen Solution with pagination progress

1) active_test_users.csv: id,email of active users with '.test' emails
2) domain_counts.csv: Domain,count of all users by email domain suffix
"""

import requests   # for making HTTP requests to the GoRest API
import csv        # for writing CSV output files
from collections import Counter  # for counting occurrences of each domain suffix

# Base URL for the GoRest users endpoint
API_URL   = 'https://gorest.co.in/public/v2/users'
# Number of users to fetch per page (GoRest supports up to 100)
PER_PAGE  = 100

def fetch_all_users():
    """
    Fetch all users from the API by iterating through paginated responses.
    Prints progress to the console as each page is retrieved.
    Returns a list of user dictionaries.
    """
    users = []   # list to accumulate all users
    page = 1     # start with the first page
    while True:
        # GET request with page and per_page parameters
        resp = requests.get(API_URL, params={'page': page, 'per_page': PER_PAGE})
        resp.raise_for_status()               # raise exception on HTTP error
        batch = resp.json()                  # parse JSON body into Python list

        # print progress for this page
        print(f"Page {page}: Retrieved {len(batch)} users")

        if not batch:                        # if empty list, no more pages
            print("No more users to fetch; ending pagination.")
            break

        users.extend(batch)                  # add this page's users to main list
        page += 1                            # advance to next page

    print(f"Total users fetched: {len(users)}\n")
    return users

def write_active_test_users(users, filename='active_test_users.csv'):
    """
    Write a CSV file of active users whose emails end with '.test'.
    Each row: id,email
    """
    print(f"Writing filtered active .test users to {filename}...")
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'email'])     # header row
        # iterate through all user dicts
        for u in users:
            email = u.get('email', '')       # safely get the email field
            # filter: must be active and email must end with '.test'
            if u.get('status') == 'active' and email.endswith('.test'):
                writer.writerow([u['id'], email])  # write id and email
    print(f"Done: {filename}\n")

def write_domain_counts(users, filename='domain_counts.csv'):
    """
    Count all users by the suffix of their email domain and write CSV.
    Each row: Domain,count
    """
    print(f"Counting domains and writing to {filename}...")
    counter = Counter()  # Counter to tally occurrences of each suffix
    for u in users:
        email = u.get('email', '')
        if '@' in email:                      # ensure email contains '@'
            # split to get domain (after '@'), then split on last '.' to get suffix
            suffix = email.split('@')[1].rsplit('.', 1)[-1]
            counter[suffix] += 1              # increment count for this suffix

    # write the tallied counts to a CSV file
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Domain', 'count'])           # header row
        # write each suffix and its count, capitalizing the suffix
        for suffix, cnt in counter.items():
            writer.writerow([suffix.capitalize(), cnt])
    print(f"Done: {filename}\n")

def main():
    """
    Main execution flow:
    1. Fetch all users (with progress prints)
    2. Generate active_test_users.csv
    3. Generate domain_counts.csv
    """
    users = fetch_all_users()               # retrieve full user list
    write_active_test_users(users)          # create filtered CSV
    write_domain_counts(users)              # create domain count CSV

if __name__ == '__main__':
    main()  # entry point when script is run directly