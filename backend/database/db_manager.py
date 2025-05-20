import sqlite3
import os
from datetime import datetime

from .schema import DB_PATH

class DatabaseManager:
    def __init__(self):
        self.db_path = DB_PATH
        
    def _get_connection(self):
        """Get a database connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        return conn
        
    def save_event(self, event):
        """Save an event to the database, avoid duplicates based on title and date"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Check if event already exists
        cursor.execute(
            "SELECT id FROM events WHERE title = ? AND date_time = ? AND ticket_link = ?",
            (event['title'], event['date_time'], event['ticket_link'])
        )
        existing = cursor.fetchone()
        
        if existing:
            # Update existing event
            cursor.execute(
                """UPDATE events 
                   SET location = ?, description = ?, source = ?
                   WHERE id = ?""",
                (event['location'], event['description'], event['source'], existing['id'])
            )
            event_id = existing['id']
        else:
            # Insert new event
            cursor.execute(
                """INSERT INTO events (title, date_time, location, description, ticket_link, source)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (event['title'], event['date_time'], event['location'], 
                 event['description'], event['ticket_link'], event['source'])
            )
            event_id = cursor.lastrowid
            
        conn.commit()
        conn.close()
        return event_id
        
    def get_all_events(self):
        """Get all events from the database"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM events ORDER BY date_time")
        events = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return events
        
    def save_email(self, email, event_id):
        """Save user email when they click on an event"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO emails (email, event_id) VALUES (?, ?)",
            (email, event_id)
        )
        
        conn.commit()
        conn.close()
        
    def clear_old_events(self, days=30):
        """Remove events older than specified days"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "DELETE FROM events WHERE date_time < datetime('now', ?)",
            (f'-{days} days',)
        )
        
        conn.commit()
        conn.close() 