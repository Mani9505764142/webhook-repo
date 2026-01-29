# webhook-repo

A Flask-based GitHub webhook receiver that captures repository events,
stores them in MongoDB, and displays recent activity on a simple UI.

This project was built as part of a technical assessment to demonstrate:
- GitHub webhook handling
- Backend event processing
- MongoDB data storage
- A minimal frontend view (no React or heavy frameworks)

## 🚀 Features

- Receives GitHub webhook events
- Supports the following GitHub actions:
  - **PUSH**
  - **PULL_REQUEST**
  - **MERGE**
- Stores minimal and relevant event data in **MongoDB**
- Displays recent repository activity on a simple UI
- UI automatically refreshes every **15 seconds**
- Clean and minimal implementation using Flask and plain HTML

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **Database:** MongoDB Atlas
- **Frontend:** HTML (Jinja2 templates)
- **Webhook Tunneling:** Ngrok
- **Version Control:** Git & GitHub

  ## 📂 Project Structure

webhook-repo/
│
├── app.py # Flask application (webhook receiver + UI routes)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore
├── .env # Environment variables (MongoDB URI)
│
├── templates/
│ └── events.html # UI template for displaying GitHub events
│
└── test_mongo.py # MongoDB connection test script



---

## ⚙️ Setup Instructions
```bash
##1️⃣ Clone the Repository

git clone https://github.com/Mani9505764142/webhook-repo.git
cd webhook-repo

##2️⃣ Create Virtual Environment & Install Dependencies
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## 3️⃣ Configure Environment Variables
mongodb+srv://username:password@cluster0.mongodb.net/github_events

## 4️⃣ Run the Application

python app.py
The server will start at:
http://127.0.0.1:5000

## 5️⃣ Expose Local Server Using Ngrok
 https://overglaze-wynona-boringly.ngrok-free.dev -> http://localhost:5000

## 6️⃣ Configure GitHub Webhook

1. Open your GitHub repository  
   **Settings → Webhooks → Add webhook**

2. Fill the webhook details:
   - **Payload URL**
     ```
     https://overglaze-wynona-boringly.ngrok-free.dev/webhook
     ```
   - **Content type**
     ```
     application/json
     ```
   - **Secret**
     ```
     (leave empty – this project does not use webhook secrets)
     ```
   - **SSL verification**
     ```
     Enable
     ```

3. Select events:
   - Choose **Let me select individual events**
   - Enable:
     - **Pushes**
     - **Pull requests**

4. Click **Add webhook**

## 7️⃣ Verify Webhook Events

1. Push a commit to the connected GitHub repository  
   or open / merge a pull request.

2. Open the GitHub webhook:
   **Settings → Webhooks → Recent Deliveries**

3. Confirm:
   - Delivery status is **200 OK**
   - Event payload is sent successfully

4. Open the UI in your browser:
   http://127.0.0.1:5000


5. Verify that the event appears in the dashboard.

The webhook integration is now fully working.

## 8️⃣ MongoDB Data Format

Each webhook event is stored in MongoDB with only relevant fields.

Example document structure:

```json
{
  "_id": "ObjectId",
  "event_type": "PUSH | PULL_REQUEST | MERGE",
  "repository": "repository-name",
  "author": "github-username",
  "message": "commit message or PR title",
  "timestamp": "ISODate"
}
Database: github_events
Collection is created automatically on first insert
::contentReference[oaicite:0]{index=0}

## 9️⃣ UI Auto Refresh

- The events dashboard automatically refreshes every **15 seconds**
- No manual reload is required
- Implemented using a simple JavaScript timer inside the HTML template

This ensures the UI always shows the latest GitHub activity.

## 🔍 Troubleshooting

- **Webhook not triggering**
  - Verify ngrok is running
  - Ensure the webhook Payload URL matches the ngrok URL exactly
  - Check that the `/webhook` route exists in `app.py`

- **Events not showing in UI**
  - Confirm MongoDB Atlas connection is active
  - Check that events are being inserted into the collection
  - Refresh the page after 15 seconds

- **GitHub shows failed delivery**
  - Open **Webhooks → Recent Deliveries**
  - Inspect the response body and status code
  - Ensure Flask server is running
## 📄 License

This project is open-source and available under the **MIT License**.
## 👤 Author

Developed by **Sai Manikanta Vivek**  
GitHub: https://github.com/Mani9505764142

## ✅ Project Status

- Flask backend implemented and verified
- GitHub webhook events received successfully
- MongoDB data storage working
- UI displaying live repository activity
- Auto-refresh confirmed
- Webhook deliveries returning **200 OK**






