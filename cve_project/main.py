import sqlite3
import unittest


# Establish SQLite connection
conn = sqlite3.connect('cve_database.db')
cursor = conn.cursor()

# Read and Filter by CVE ID


def get_cve_by_id(cve_id):
    cursor.execute("SELECT * FROM cve_table WHERE cve_id = ?", (cve_id,))
    return cursor.fetchall()

# Filter by Specific Year


def get_cves_by_year(year):
    cursor.execute("SELECT * FROM cve_table WHERE year = ?", (year,))
    return cursor.fetchall()

# Filter by CVE Score


def get_cves_by_score(score):
    cursor.execute("SELECT * FROM cve_table WHERE score = ?", (score,))
    return cursor.fetchall()

# Filter by last modified in N days


def get_cves_last_modified_days(days):
    cursor.execute("SELECT * FROM cve_table WHERE last_modified <= ?", (days,))
    return cursor.fetchall()


class TestCVEFunctions(unittest.TestCase):
    def setUp(self):
        # Create the test database and table for testing
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''CREATE TABLE cve_table (cve_id text, description text, year int, score int, last_modified int)''')
        self.cursor.execute(
            "INSERT INTO cve_table (cve_id, description, year, score, last_modified) VALUES ('CVE-2024-1234', 'Test Description', 2024, 5, 5)")

    def test_get_cve_by_id(self):
        self.assertEqual(len(get_cve_by_id("CVE-2024-1234")), 1)

    def test_get_cves_by_year(self):
        self.assertGreaterEqual(len(get_cves_by_year(2024)), 1)

    def tearDown(self):
        self.conn.close()


if __name__ == '__main__':
    unittest.main()
