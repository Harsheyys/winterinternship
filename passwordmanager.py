import random
import string
import sqlite3
import tkinter as tk
from tkinter import messagebox

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def store_password(self, account, password):
        self.passwords[account] = password

        # Store the password in the database
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute("INSERT INTO passwords (account, password) VALUES (?, ?)", (account, password))
        conn.commit()
        conn.close()

    def retrieve_password(self, account):
        password = self.passwords.get(account)
        if password:
            return password
        else:
            # Retrieve the password from the database
            conn = sqlite3.connect('passwords.db')
            c = conn.cursor()
            c.execute("SELECT password FROM passwords WHERE account=?", (account,))
            result = c.fetchone()
            conn.close()

            if result:
                return result[0]
            else:
                return None

