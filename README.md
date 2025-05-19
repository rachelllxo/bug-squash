🌟 Project Name: BugSquash 
A multi-agent Python-based system that automatically finds, fixes, and reviews bugs in Python code.
Built with Google Cloud Pub/Sub, Firestore, and OpenAI API — designed to improve code quality effortlessly.

📌 Table of Contents
About the Project
Tech Stack
Features
Installation
Usage
Folder Structure
Contributing
License
Author

📖 About the Project
BugSquash is an AI-powered bug-fixing and reviewing system that uses a multi-agent architecture. It:
Accepts Python code as input
Detects logical and syntactic bugs
Fixes issues and provides explanations
Reviews the final output and suggests improvements
The system is designed to work in real-time with message queues (Google Pub/Sub) and cloud-based storage (Firestore), enabling scalable and modular processing of tasks.

🛠 Tech Stack
Language: Python 3.10+
Cloud Platform: Google Cloud (Pub/Sub, Firestore)
AI/LLM: OpenAI GPT-4 API
Environment: Docker (optional), local virtualenv
Other: Flask (if web interface), Firestore Emulator (for local testing)

✨ Features
📥 Accepts Python files via Pub/Sub
🐞 Analyzes code for bugs using GPT-4
🔧 Suggests and applies bug fixes
✅ Reviews final code with reasoning
☁️ Stores original and modified files in Firestore
🔄 Fully asynchronous pipeline with modular agents

📦 Installation
bash
# Clone the repository
git clone https://github.com/yourusername/autobugsquash.git
cd autobugsquash

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
You’ll need:

A Google Cloud project Pub/Sub topic and subscription
Firestore setup
OpenAI API key

🚀 Usage
1. Start the Listener
bash
python src/agents/listener.py
2. Send Test Code to Pub/Sub
Use the CLI or a script in src/test/
bash
python src/test/publish_sample.py
3. Output
Fixed code stored in Firestore
Logs available in terminal

📁 Folder Structure
bash
Copy
Edit
autobugsquash/
│
├── src/
│   ├── agents/
│   │   ├── bug_fixer.py
│   │   ├── code_agent.py│
├── .env.example
├── requirements.txt
└── README.md
🤝 Contributing
Pull requests are welcome! If you’d like to improve or extend the project:

Fork the repo

Create a new branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m 'Add your feature')

Push to the branch (git push origin feature/your-feature)

Open a pull request

📜 License
This project is licensed under the MIT License.
See the LICENSE file for details.

👩‍💻 Author
E Rachel
CSE Student | AI/ML Enthusiast | Open Source Contributor
GitHub · LinkedIn · Email

