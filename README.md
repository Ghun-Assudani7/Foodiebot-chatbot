**Foodie Bot 🍽️**
Foodie Bot is an intelligent chatbot designed to simplify the food ordering process. It allows users to add items to their cart, track orders, and complete orders with ease. The bot integrates with a MySQL backend for order management and real-time tracking, providing a smooth and efficient food ordering experience.

**Features 📋**
1. Add Items to Order: Users can add multiple food items with quantities to an ongoing order.
2. Order Completion: The bot completes the order, calculates the total cost, and generates an order ID.
3. Order Tracking: Users can track the status of their order using the order ID provided by the bot.
4. Error Handling: The bot manages incomplete or incorrect user inputs to ensure smooth interaction.
Tech Stack 🛠️
1. Framework: FastAPI
2. Backend: Python
3. Database: MySQL
4. Chatbot: Custom NLP integration



**Installation & Setup 🚀**
Prerequisites
Python 3.7+
FastAPI
MySQL
Virtual environment (optional, but recommended)

**API Endpoints 🔥
POST /:**

Description: Main handler for chatbot requests.
Payload: Expects JSON input with queryResult (intent, parameters, and outputContexts).
Order Management Functions:

add_to_order: Adds food items to the current order session.
complete_order: Completes the order, saves it in the database, and generates an order ID.
track_order: Provides the current status of the order by ID.

Project Structure 📂:
📦foodie-bot
 ┣ 📂db_helper.py              # Contains MySQL database operations
 ┣ 📂generic_helper.py         # General helper functions for chatbot logic
 ┣ 📂main.py                   # Main FastAPI server and intent handling logic
 ┣ 📜requirements.txt          # Python dependencies
 ┣ 📜README.md                 # Project documentation
