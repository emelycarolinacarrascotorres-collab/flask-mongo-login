---
title: Flask Mongo Login
emoji: 🐨
colorFrom: purple
colorTo: red
sdk: docker
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

---

# Flask MongoDB Login System

A secure web application built with Flask and MongoDB that provides user authentication with signup, login, logout, and "Remember Me" functionality.

## 🚀 Live Demo

Visit the live application: [https://lovnishverma-flask-mongo-login.hf.space/](https://lovnishverma-flask-mongo-login.hf.space/)

## ✨ Features

- **User Registration**: Secure signup with username and password
- **User Authentication**: Login with username/password validation
- **Password Security**: Passwords are hashed using Werkzeug's security utilities
- **Remember Me**: Optional persistent login using secure cookies (7 days)
- **Session Management**: Server-side session handling
- **Flash Messages**: User feedback for actions (success, error, info)
- **Responsive Design**: Clean and modern UI
- **Database Integration**: MongoDB for user data storage
- **Environment Variables**: Secure configuration using .env files

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: MongoDB
- **Authentication**: Werkzeug Security
- **Frontend**: HTML templates with Jinja2
- **Environment**: Python-dotenv for configuration
- **Timezone**: PyTZ for datetime handling

## 📋 Prerequisites

- Python 3.7+
- MongoDB instance (local or cloud)
- pip (Python package manager)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd flask-mongo-login
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask pymongo python-dotenv werkzeug pytz
   ```

4. **Environment Setup**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key-here
   MONGO_URI=mongodb://localhost:27017/
   # For MongoDB Atlas: mongodb+srv://username:password@cluster.mongodb.net/
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

## 🏗️ Project Structure

```
flask-mongo-login/
│
├── app.py                 # Main Flask application
├── .env                   # Environment variables (not in repo)
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── index.html        # Home page
│   ├── login.html        # Login page
│   └── signup.html       # Signup page
└── static/              # CSS, JS, images (if any)
```

## 🔐 Security Features

- **Password Hashing**: All passwords are hashed using `generate_password_hash()`
- **Session Security**: Flask sessions with secret key
- **Input Validation**: Username and password trimming
- **Secure Cookies**: Remember me functionality with expiration
- **Environment Variables**: Sensitive data stored in .env file

## 📱 API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page (requires login) |
| `/signup` | GET, POST | User registration |
| `/login` | GET, POST | User authentication |
| `/logout` | GET | User logout and session clearing |

## 🎯 Usage

### User Registration
1. Navigate to `/signup`
2. Enter unique username and password
3. Click "Sign Up"
4. Redirected to login page upon success

### User Login
1. Navigate to `/login` (or root `/`)
2. Enter username and password
3. Optionally check "Remember Me" for persistent login
4. Access granted to home page upon successful authentication

### Remember Me Feature
- When enabled, creates a secure cookie lasting 7 days
- Automatically logs in users on subsequent visits
- Cookie is cleared upon manual logout

## 🗄️ Database Schema

### Users Collection
```javascript
{
  "_id": ObjectId("..."),
  "username": "string",
  "password": "hashed_string"
}
```

## 🚀 Deployment

The application is deployed on Hugging Face Spaces using Docker. For your own deployment:

1. **Hugging Face Spaces**: Upload your code and configure environment variables
2. **Heroku**: Add MongoDB Atlas connection string to config vars
3. **Local**: Ensure MongoDB is running locally

## 🔧 Configuration

### Environment Variables
- `SECRET_KEY`: Flask secret key for sessions
- `MONGO_URI`: MongoDB connection string

### Database Configuration
- Database: `login_app`
- Collection: `login`

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Known Issues

- None currently reported

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Contact: princelv84@gmail.com

## 🙏 Acknowledgments

- Flask framework for web development
- MongoDB for database solutions
- Werkzeug for security utilities
- Hugging Face Spaces for hosting

---

**Note**: Remember to keep your `.env` file private and never commit it to version control. Always use environment variables for sensitive configuration data.
