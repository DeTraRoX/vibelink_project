<p align="center">
  <img src="https://placehold.co/800x250/8e44ad/ffffff?text=VibeLink" alt="Project Banner" />
</p>

<h1 align="center">VibeLink 🤝</h1>

<p align="center">
A smart, real-time friend suggestion and chat platform designed to help users connect based on shared interests.
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
<img src="https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
<img src="https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
</p>

---

## 🌟 Project Overview
In today’s digital world, finding meaningful connections can be challenging. **VibeLink** makes this process effortless by suggesting friends based on shared interests and enabling real-time chat.  

The platform combines simplicity with functionality — from account creation to chatting, everything is seamless and interactive. VibeLink ensures users can build their social circle and stay connected with ease.  

---

## ✨ Key Features

- **🔐 User Authentication**  
  Secure login and registration system with session-based authentication.  

- **🎯 Smart Friend Suggestions**  
  Get recommended friends based on shared interests and profile compatibility.  

- **📌 Multiple Interests**  
  Users can select multiple interests, making suggestions more accurate and relevant.  

- **👥 Sidebar Friend List**  
  Always stay updated with a dynamic sidebar displaying your added friends.  

- **💬 Real-time Chat**  
  Built-in chat feature directly in the same template, so you can message friends without switching pages.  

- **📱 Responsive Design**  
  Fully responsive and user-friendly interface built with HTML, CSS, and JavaScript.  

---

## 📸 Demo & Screenshots

### 🔑 Authentication
Register and log in to get started with VibeLink.  

### 🧭 Dashboard / Suggestions
View suggested friends and connect instantly.  

### 💬 Chat Interface
Seamless one-on-one chat with live updates.  

*(Add your screenshots here)*  

---

## ⚙️ Installation and Setup

Follow these steps to run **VibeLink** locally:

### 1. Clone the Repository
```bash
git clone https://github.com/DeTraRoX/VibeLink.git
cd VibeLink

2. Create a Virtual Environment
python -m venv .venv
# Activate it
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py migrate

5. Run the Development Server
python manage.py runserver


Open your browser at http://127.0.0.1:8000
 🎉

📂 Project Structure
VibeLink/
├── vibelink/           # Django project settings
├── core/               # App containing main logic (auth, suggestions, chat)
├── templates/          # HTML templates
├── static/             # CSS, JS, and images
├── db.sqlite3          # SQLite database
├── manage.py           # Django project manager
└── requirements.txt    # Project dependencies

❤️ Contributing

Contributions are welcome! Here’s how you can help:

🐛 Report issues and bugs

✨ Suggest new features

🔥 Submit pull requests

📜 License

This project is licensed under the MIT License – feel free to use and modify it.
