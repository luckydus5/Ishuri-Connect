# Ishuri-Connect

An intelligent student-school matching platform that helps Rwandan students find universities and programs that match their academic profile, subject combination, and preferences.

## 🌟 Features

- ✨ **Beautiful colored CLI interface** with icons and professional formatting
- 👤 **Comprehensive student registration**: Profile with secondary school, aggregate marks, subject combination, location preferences, desired program
- 📊 **Intelligent matching algorithm**: Multi-criteria scoring (marks 30%, program 30%, location 20%, subjects 20%)
- 🎓 **10 Rwandan universities**: Real institutions with 26+ programs
- 📚 **Subject combinations**: PCM, PCB, MEG, HEG, LKE, MCB, and more
- 🌍 **Location-based matching**: Preferences by district and province
- 📧 **Email validation** and duplicate checking
- 🎯 **School recommendations** with match scores and reasons
- 💾 **MySQL database**: Persistent storage with automatic initialization
- 🎨 **Modern user experience** with color-coded match quality

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher (or Aiven cloud database)
- Virtual environment (recommended)

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/luckydus5/Ishuri-Connect.git
cd Ishuri-Connect
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv ishuri
.\ishuri\Scripts\Activate.ps1

# Linux/Mac
python3 -m venv ishuri
source ishuri/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

This installs:
- `mysql-connector-python` - MySQL database driver
- `python-dotenv` - Environment variable management
- `colorama` - Colored terminal output

### 4. Configure database connection
Create a `.env` file in the project root:

```env
DB_HOST=your_host
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=ishuri_connect
```

### 5. Run the application
```bash
python main.py
```

**That's it!** The database will be created automatically on first run with sample data.

## 💻 Usage

### Registration Flow:
1. 👤 Enter basic info (name, email)
2. 🏫 Previous education (secondary school, aggregate marks)
3. 📚 Subject combination (PCM, PCB, MEG, HEG, etc.)
4. 🌍 Location preferences (where you're from, where you want to study)
5. 🎓 Desired program (Computer Science, Medicine, Engineering, etc.)
6. 🏠 Boarding preference

### Get Recommendations:
- See intelligent matches sorted by compatibility
- View match scores (🌟 Excellent, ✅ Good, 📊 Possible)
- Filter by desired program with keyword search
- See why each school matches (marks, program, combination, location)

### Apply to Schools:
- Submit applications to matched schools
- Track application status
- View application history

## 📁 Project Structure

```
Ishuri-Connect/
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (not in git)
├── .gitignore                # Git ignore rules
├── README.md                  # This file
│
├── src/                       # Application source code
│   ├── __init__.py           # Package initializer
│   ├── cli.py                # CLI interface with menus
│   ├── models.py             # Data models (Student, School, Application)
│   └── utils.py              # Utility functions
│
├── database/                  # Database layer
│   ├── __init__.py           # Package initializer
│   ├── db.py                 # Database operations (CRUD)
│   └── sql/
│       └── schema.sql        # Database schema
│
├── config/                    # Configuration files (reserved)
│
└── ishuri/                    # Virtual environment (not in git)
```

### Key Files:

**`main.py`**
- Application entry point
- Auto-initializes database on first run
- Displays welcome banner

**`src/cli.py`**
- Complete CLI interface
- Menu systems (main menu, student menu)
- Registration, recommendations, applications
- Keyword-based program search

**`src/models.py`**
- `Student` class - student profiles
- `School` class - university data
- `Application` class - application tracking
- Matching algorithms and scoring

**`database/db.py`**
- `Database` class - MySQL operations
- CRUD operations for all tables
- Complex queries with JOINs
- Program and school search

**`src/utils.py`**
- Email validation
- Helper functions

## 🗄️ Database Schema

### Tables:

**students**
- Basic info (name, email)
- Academic (secondary school, aggregate marks, subject combination)
- Preferences (location, desired program, boarding)

**schools**
- University details (name, district, province, type)
- Admission (cutoff range, required subjects, competencies)
- Contact (email, website)

**programs**
- Program details (name, code, description)
- Requirements (cutoff marks, combination, duration)
- Fees information

**applications**
- Student applications to schools
- Status tracking (pending, accepted, rejected)
- Timestamps

## 🧠 Matching Algorithm

### Multi-Criteria Scoring (0-100 points)

**1. Marks Match (30 points)**
- Student aggregate ≥ school cutoff
- Higher marks = higher score

**2. Program Match (30 points)**
- School offers student's desired program
- Keyword-based search for flexibility

**3. Location Match (20 points)**
- Same district = 20 points
- Same province = 15 points  
- Different location = 5 points

**4. Subject Compatibility (20 points)**
- School accepts student's combination
- PCM, PCB, MEG, HEG, etc.

### Match Quality
- 🌟 **Excellent**: Perfect match
- ✅ **Good**: Strong candidate
- ❌ **Marks Too Low**: Doesn't meet minimum

## 📚 Technical Stack

**Backend:**
- Python 3.8+
- MySQL 8.0+
- mysql-connector-python

**Libraries:**
- `colorama` - Terminal colors
- `python-dotenv` - Environment configuration
- `re` - Email validation

**Concepts:**
- Object-Oriented Programming (OOP)
- Database Design (MySQL)
- CRUD Operations
- Multi-criteria Algorithms
- CLI Development

## 🎓 Universities Included

10 Rwandan universities with 26+ programs:
- University of Rwanda (UR)
- African Leadership University (ALU)
- Kigali Independent University (KIU)
- AUCA, MKU, UNILAK, INES-Ruhengeri, and more

Programs: Computer Science, Medicine, Engineering, Business, Law, Nursing, IT, Architecture, and more.

## 🐛 Troubleshooting

**"Access denied for user"**
- Check password in `.env`
- Verify database exists

**"Can't connect to MySQL server"**
- Verify MySQL is running
- Check host/port in `.env`

**"ModuleNotFoundError"**
- Activate virtual environment
- Run `pip install -r requirements.txt`

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push: `git push origin feature-name`
5. Open Pull Request

## 📄 License

MIT License

## 👤 Author

**Lucky D. (@luckydus5)**
- GitHub: [@luckydus5](https://github.com/luckydus5)
- Project: School Project - OOP with MySQL

---

# Built with love for Rwandan students seeking higher education

# Get Involved
We welcome contributions! Suggest features, report bugs, or improve documentation.

#Acknowledgements 
Thanks to all universities, mentors, and contributors who helped make this project possible.

# Our Contacts for questions or feedback 

gabrielmugisha@gmail.com
garymurasira@gmail.com
benitor@gmail.com
micoprince@gmail.com
 lucky@gmail.com

# Telephone: +250788358933
