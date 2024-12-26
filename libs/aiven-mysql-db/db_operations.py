# Database interaction logic

from db_config import get_connection

def store_chat(user_id, message, is_bot_response):
    """Store chat history in the database."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = "INSERT INTO ChatHistory (user_id, message, is_bot_response) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, message, is_bot_response))
        connection.commit()
    finally:
        connection.close()

def get_chat_history(user_id):
    """Retrieve chat history for a user."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = "SELECT message, is_bot_response, timestamp FROM ChatHistory WHERE user_id = %s ORDER BY timestamp"
            cursor.execute(query, (user_id,))
            return cursor.fetchall()
    finally:
        connection.close()
