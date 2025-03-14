# 📝 Notes App

A simple Notes app built with **Django Rest Framework (DRF) and React**, supporting basic **CRUD (Create, Read, Update, Delete)** operations without authentication.

## 🚀 Features  
- Create new notes  
- View all notes  
- Edit existing notes  
- Delete notes  
- RESTful API built using Django Rest Framework  
- Frontend built with React  

## 🛠️ Tech Stack  
- **Backend:** Django, Django Rest Framework (DRF)  
- **Frontend:** React, JavaScript  
- **Database:** SQLite (default, can be changed)  
- **Others:** Axios (for API requests), React Hooks  

---

## 📂 Project Structure  

/note-app

│── /backend # Django backend (DRF API)

│── /frontend # React frontend

│── /venv # Virtual environment (optional)

│── manage.py # Django management script

│── README.md # Project documentation


---

## 🎯 Installation & Setup  

### 1️⃣ Clone the repository  
```sh
git clone https://github.com/hamzaraftar/Notes-App.git
cd frontend
cd backend
python -m venv venv  # Create a virtual environment (optional)
source venv/bin/activate  # Activate virtual environment (Mac/Linux)
venv\Scripts\activate  # Activate virtual environment (Windows)
pip install -r requirements.txt  # Install dependencies
python manage.py migrate  # Apply migrations
python manage.py runserver  # Start Django server

cd frontend
npm install  # Install dependencies
npm run dev  # Start React development server

🔗 API Endpoints (Django DRF)
Method	Endpoint        Description
GET	/api/notes/	        Get all notes
POST	/api/notes/       Create a new note
GET	/api/notes/{id}/	  Get a specific note
PUT	/api/notes/{id}/	  Update a note
DELETE	/api/notes/{id}/Delete a note

📌 Notes
The frontend communicates with the backend using Fetch to perform API requests.
You can modify the database settings in settings.py if you want to use PostgreSQL, MySQL, or any other database.
Make sure the backend server is running before starting the frontend.
🤝 Contributing
Feel free to fork this repository and submit pull requests! 🚀

📧 Contact
If you have any questions, feel free to reach out:
📩 Email: hamzaraftar765@gmail.com
GitHub: hamzaraftar

⭐ Don't forget to star the repository! 😊🚀
