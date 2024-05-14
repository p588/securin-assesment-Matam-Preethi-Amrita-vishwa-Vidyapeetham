import unittest
import sqlite3


class TestCVEFunctions(unittest.TestCase):
    def setUp(self):
        # Create the test database and table for testing
        self.conn = sqlite3.connect('C:\Users\HP\OneDrive - Amrita Vishwa Vidyapeetham\Desktop\cve_project\cve_database.db')
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
