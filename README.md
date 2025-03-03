# Slack Coffee Bot – Random Coffee Pairing for Remote Teams

## 🚀 What is this?
The Slack Coffee Bot is a simple yet powerful tool designed to connect remote team members for informal coffee chats. It randomly pairs users each week and sends them a Slack message, helping to foster connections and reduce isolation in remote work environments.

## 🎯 Why This Project? (The Problem & Solution)
### Problem:
In remote teams, employees often lack informal, spontaneous conversations that are common in an office environment. This can lead to isolation and weaker team relationships.

### Solution:
This Slack bot randomly pairs teammates for weekly coffee chats, encouraging more interaction and stronger team bonding.

## 🛠️ How It Works
1. Employees opt in to participate.
2. Every Monday at 9 AM, the bot randomly pairs two teammates.
3. The bot sends a Slack message to introduce the pair.
4. Employees schedule their chat and enjoy their coffee! ☕

## 🔧 Tech Stack
- ✅ **Python** – Core bot logic
- ✅ **Flask** – API server
- ✅ **Firestore** – Database for storing users & pairings
- ✅ **APScheduler** – Used for scheduling the weekly pairing job (Not implemented)
- ✅ **Slack API** – Sends messages to matched users (Not implemented)

## 📂 Project Setup

1️⃣ Clone the Repository
bash
git clone https://github.com/yourusername/slack-coffee-bot.git
cd slack-coffee-bot

2️⃣ Set Up a Virtual Environment
Create a virtual environment to manage dependencies:
  bash
  Copy
  Edit
  python -m venv venv

Activate the virtual environment:
On macOS/Linux:
  bash
  Copy
  Edit
  source venv/bin/activate
  On Windows:
  bash
  Copy
  Edit
  venv\Scripts\activate
  
3️⃣ Install Dependencies
Install all required dependencies by running:
  bash
  Copy
  Edit
  pip install -r requirements.txt

4️⃣ Set Environment Variables
Create a .env file in the root folder and add your environment variables:
  SLACK_BOT_TOKEN=your-slack-bot-token
  SLACK_CHANNEL=your-slack-channel-id
  PORT=5000
5️⃣ Run the Bot
Run the bot using the following command:
  python slack_bot_coffee.py
6️⃣ Trigger Pairing Manually (for testing)
You can trigger a pairing manually by visiting the following URL:
  http://127.0.0.1:5000/trigger
  
🚀 Features & Roadmap
✅ Current Features:
Random pairing of users
Firestore integration to store user data and pairings
Scheduled weekly pairing (every Monday at 9 AM)
Slack notifications for the paired users
🔜 Upcoming Features:
  Opt-in & opt-out system for users
  User preferences (team-based pairing, time zone matching)
  Web dashboard for admins to monitor pairings
  Feedback collection from users after coffee chats
  
📸 Demo
Add a screenshot or GIF demonstrating how the bot works in Slack. You can upload it to GitHub or link it from an external source:

🤝 Contributing
Want to improve this bot? Contributions are welcome! Feel free to submit a pull request (PR) with your changes.

Steps to Contribute:
Fork the repository.
Create a new branch for your feature/bugfix.
Implement your changes.
Open a pull request.
📩 Contact & Socials
💡 Made by [Your Name]
📧 Email: your.email@example.com
🔗 LinkedIn: your-linkedin-profile
💻 GitHub: your-github-profile
