import os
import random
import requests
import logging
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from firebase_admin import credentials, firestore, initialize_app
from google.oauth2 import service_account
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# Flask app
app = Flask(__name__)

# Load environment variables from the .env file
load_dotenv()

# Retrieve values from environment variables
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")
PORT = int(os.getenv("PORT", 5000))  # Default to 5000 if not set

print(f"Slack Bot Token: {SLACK_BOT_TOKEN[:10]}... (hidden for security)")
print(f"Slack Channel ID: {SLACK_CHANNEL}")
print(f"Running on Port: {PORT}")

# Firebase setup
#cred = credentials.Certificate("C:/Users/lapid/firebase-credentials.json")
cred = service_account.Credentials.from_service_account_file(
    'C:/Users/lapid/firebase-credentials.json'
)
initialize_app(cred)
#db = firestore.client()
db = firestore.Client(credentials=cred)

# Firestore collection references
#users_ref = firestore.Client().collection('virtual_users')  # Adjust the collection name if necessary
users_ref = db.collection('virtual_users')
pairings_ref = db.collection("pairings")

# Add virtual users to Firestore (for testing purposes)
def add_virtual_users():
    test_users = [
        {"id": "U12345", "name": "Alice", "is_bot": False, "deleted": False},
        {"id": "U67890", "name": "Bob", "is_bot": False, "deleted": False},
        {"id": "U11223", "name": "Charlie", "is_bot": False, "deleted": False},
        {"id": "U44556", "name": "David", "is_bot": False, "deleted": False},
        {"id": "U78901", "name": "Eve", "is_bot": False, "deleted": False},
    ]
    for user in test_users:
        users_ref.add(user)
    logger.info("Virtual users added to Firestore.")

# Function to fetch virtual users from Firestore
def fetch_virtual_users():
    logger.debug("Fetching virtual users from Firestore...")
    docs = users_ref.stream()
    users = [doc.to_dict() for doc in docs if not doc.to_dict().get("is_bot") and not doc.to_dict().get("deleted")]
    logger.debug(f"Fetched {len(users)} virtual users.")
    return users

# Function to pair users randomly
def pair_users(users):
    logger.debug(f"Pairing {len(users)} users...")
    random.shuffle(users)
    return [(users[i], users[i+1]) for i in range(0, len(users)-1, 2)]

# Function to store pairings in Firestore
def store_pairings(pairs):
    for user1, user2 in pairs:
        pair_data = {
            "user1_id": user1['id'],
            "user2_id": user2['id'],
            "status": "paired"
        }
        pairings_ref.add(pair_data)
        logger.debug(f"Stored pairing for <@{user1['id']}> & <@{user2['id']}>.")

# Function to manually trigger pairing
def manual_trigger():
    logger.info("Manually triggering the pairing function...")
    users = fetch_virtual_users()  # Fetch virtual users instead of Slack users
    if users:
        pairs = pair_users(users)  # Randomly pair users
        store_pairings(pairs)  # Store pairings in Firestore
        for user1, user2 in pairs:
            send_slack_message(user1, user2)  # Simulate sending message
        logger.info("Pairing complete!")
    else:
        logger.error("No virtual users found to pair.")

# Function to simulate sending Slack messages
def send_slack_message(user1, user2):
    text = f"☕ Hey <@{user1['id']}> & <@{user2['id']}>, you've been matched for a coffee chat!"
    logger.info(f"Sending message: {text}")  # Just log instead of sending

# Scheduled pairing function
def run_pairing():
    logger.info("Running weekly pairing...")
    users = fetch_virtual_users()  # Change to fetch_virtual_users() for testing
    if users:
        pairs = pair_users(users)
        store_pairings(pairs)  # Store pairings in Firestore
        for user1, user2 in pairs:
            send_slack_message(user1, user2)
        logger.info("Pairing complete!")
    else:
        logger.error("No users to pair.")

# Schedule job to run every Monday at 9 AM
scheduler = BackgroundScheduler()
scheduler.add_job(run_pairing, "cron", day_of_week="mon", hour=9)
scheduler.start()

# Flask route to trigger pairing manually via a web request
@app.route("/trigger", methods=["GET"])
def trigger():
    manual_trigger()
    return "Pairing triggered manually!", 200

if __name__ == "__main__":
    logger.info("Scheduler started. Waiting for scheduled task...")
    app.run(port=int(os.getenv("PORT", 5000)))  # Keep app running
