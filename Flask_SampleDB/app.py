from flask import Flask, render_template, g, request, redirect, url_for
import sqlite3

DATABASE = 'sampleDB.db'
app = Flask(__name__)

def get_db_connection():
    """Connect to the database and return the connection."""

    db connection = getattr(g, '_database_connection', None)
