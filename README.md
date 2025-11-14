# Ishuri-Connect

An intelligent student-school matching platform that helps Rwandan students find universities and programs that match their academic profile, subject combination, and preferences.

## 🌟 Features

- ✨ **Beautiful colored CLI interface** with icons and professional formatting
- 👤 **Comprehensive student registration**: Profile with secondary school, aggregate marks, subject combination, location preferences, desired program
- 📊 **Intelligent matching algorithm**: Multi-criteria scoring (marks 30%, program 30%, location 20%, subjects 20%)
- 🎓 **10 Rwandan universities**: Real institutions with 30+ programs
- 📚 **Subject combinations**: PCM, PCB, MEG, HEG, LKE, MCB, and more
- 🌍 **Location-based matching**: Preferences by district and province
- 📧 **Email validation** and duplicate checking
- 🎯 **School recommendations** with match scores and reasons
- 💾 **MySQL database**: Persistent storage with automatic initialization
- 🎨 **Modern user experience** with color-coded match quality

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher
- Virtual environment (recommended)

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/luckydus5/Ishuri-Connect.git
cd Ishuri-Connect
```

### 2. Create and activate virtual environment
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

### 4. Configure database
Create `.env` file in project root:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=ishuri_connect
```

**For Team Collaboration:** See [DATABASE_SETUP.md](DATABASE_SETUP.md) for cloud database options (FreeSQLDatabase, Railway, PlanetScale)

### 5. Run the application
```bash
python main.py
```

**That's it!** The database will be created automatically on first run with:
- ✅ 10 universities (UR, ALU, KIU, AUCA, MKU, etc.)
- ✅ 30+ programs with realistic cutoffs and requirements
- ✅ All tables and relationships

## 💻 Usage

### Simply run:
```bash
python main.py
```

### What happens:
1. **First run**: Database auto-created with sample universities and programs
2. **Subsequent runs**: Uses existing database

### Registration Flow:
1. 👤 Enter basic info (name, email)
2. 🏫 Previous education (secondary school, aggregate marks)
3. 📚 Subject combination (PCM, PCB, MEG, HEG, etc.)
4. 🌍 Location preferences (where you're from, where you want to study)
5. 🎓 Desired program (Computer Science, Medicine, Engineering, etc.)
6. 🏠 Boarding preference

### Get Recommendations:
- See intelligent matches sorted by compatibility
- View match scores (🌟 Excellent 80+, ✅ Good 60+, 📊 Possible <60)
- See why each school matches (marks, program, combination, location)

### Apply to Schools:
- Submit applications to matched schools
- Track application status
- View application history
5. Enter your marks (press Enter without input to finish)
6. View your average and school recommendations

### Example Session

```
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║        🎓  ISHURI CONNECT - School Matching Platform  🎓        ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝

  Welcome! This platform helps students find schools
  that match their academic profile and interests.

  💡 Tip: Press Ctrl+C at any time to exit.

  ──────────────────────────────────────────────────────────────────

  ┌─────────────────────────────────────────────────────────────────┐
  │ 📝  STUDENT REGISTRATION                                         │
  └─────────────────────────────────────────────────────────────────┘

  Please provide your details below:

  👤 First name: John
  👤 Last name: Doe
  📧 Email address: john.doe@example.com
  📚 Course interest: Computer Science

  ✅ Thank you John Doe!
  📊 Now enter your marks (press Enter without typing to finish):

  📝 Enter mark #1 (or press Enter to finish): 85
     ✓ Mark 1: 85.0% added
  📝 Enter mark #2 (or press Enter to finish): 90
     ✓ Mark 2: 90.0% added
  📝 Enter mark #3 (or press Enter to finish): 78
     ✓ Mark 3: 78.0% added
  📝 Enter mark #4 (or press Enter to finish):

  ┌───────────────────────────────────────────────────┐
  │ ✨ Registration Successful! ✨                    │
  │ Welcome John Doe!                                 │
  │ 📊 Your Average: 84.33%                           │
  └───────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────┐
  │ 🎯  SCHOOL RECOMMENDATIONS FOR COMPUTER SCIENCE                  │
  └─────────────────────────────────────────────────────────────────┘

  🔍 Searching for matching schools...

  ✨ Found 1 school(s) that match your profile!

  ┌────────────────────────────────────────────────────────────┐
  │ 1. University of Rwanda                                    │
  │    📌 Required minimum: 70%                                │
  │    ✅ Your average:     84.33%                             │
  └────────────────────────────────────────────────────────────┘

  ──────────────────────────────────────────────────────────────────
  ✨ Thank you for using Ishuri Connect! ✨
  ──────────────────────────────────────────────────────────────────
```

## Project Structure

```
Ishuri-Connect/
├── main.py              # Application entry point (auto-initializes database)
├── cli_new.py           # Enhanced CLI with intelligent matching
├── models.py            # OOP classes (Student, School, Application)
├── db.py                # Database operations (CRUD, matching)
├── utils.py             # Utility functions (validation, calculations)
├── setup_db.py          # Database setup script (optional)
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in git)
├── .gitignore          # Git ignore rules
├── sql/
│   └── schema.sql      # Database schema with sample data
└── ishuri/             # Virtual environment (not in git)
```

---

## 🗄️ Database Setup

### Local Development

1. **Install MySQL**
   - **Windows**: [Download MySQL](https://dev.mysql.com/downloads/installer/)
   - **Mac**: `brew install mysql`
   - **Linux**: `sudo apt install mysql-server`

2. **Configure `.env`** (already done in Quick Start)

3. **Run** - Database creates automatically!

### ☁️ Cloud Database (For Teams)

For remote team collaboration, use a cloud MySQL provider:

#### **1. FreeSQLDatabase** (FREE - Best for Students)
- Website: https://www.freesqldatabase.com/
- ✅ 5MB free, no credit card
- Setup: Create account → Get credentials → Update `.env`

#### **2. Railway.app** (FREE - $5/month credit)
- Website: https://railway.app/
- ✅ Easy GitHub integration, auto backups
- Setup: Sign in → New Project → MySQL → Copy credentials

#### **3. PlanetScale** (FREE - 10GB storage)
- Website: https://planetscale.com/
- ✅ Industry-standard, database branching
- Setup: Create database → Get connection string → Update `.env`


#### **5. Aiven** (FREE Trial - 30 days)
- Website: https://aiven.io/
- ✅ Professional features, multi-cloud

### Team Collaboration Setup

1. **Team Leader**: Set up cloud database
2. **Share `.env` securely** (encrypted email, password manager)
3. **All Members**: Clone repo → Add `.env` → Run `python main.py`
4. **Everyone accesses same database** - real-time collaboration!

---

## 📚 Technical Concepts Demonstrated

This project demonstrates mastery of:

### Object-Oriented Programming
- **Classes**: `Student`, `School`, `Application`
- **Methods**: `calculate_average()`, `matches_program()`, `accepts_combination()`
- **Encapsulation**: Data + behavior in objects
- **Inheritance**: Class hierarchies (if needed)

### MySQL Database
- **CREATE**: Tables with foreign keys, constraints
- **INSERT**: Add students, schools, programs, applications
- **SELECT**: Queries with JOINs, WHERE, ORDER BY
- **UPDATE**: Modify records
- **DELETE**: Remove records
- **Complex Queries**: FIND_IN_SET, multi-condition WHERE

### Python Data Structures
- **Lists**: `marks = []`, `schools = []`, list comprehension
- **Tuples**: `(school, score, details)`, return multiple values
- **Dictionaries**: `{'student_id': 1, 'name': 'John'}`, menu options

### Functions
- **Parameters**: `def calculate_match_score(student, school, program=None)`
- **Return values**: Single values, lists, tuples, dictionaries
- **Helper functions**: `validate_email()`, `get_subject_combination()`

### Real-World Skills
- ✅ File I/O (reading `.env`, `schema.sql`)
- ✅ Error handling (try/except)
- ✅ Environment variables
- ✅ Multi-criteria algorithms
- ✅ User input validation
- ✅ Colored terminal output

---

## 🎓 Universities & Programs Included

### 10 Rwandan Universities:
1. **University of Rwanda** (Public, 60-85% cutoff)
2. **African Leadership University** (Private, 65-80%)
3. **Kigali Independent University** (Private, 50-70%)
4. **AUCA** (Private, 55-72%)
5. **Mount Kenya University** (Private, 48-68%)
6. **University of Kigali** (Private, 50-70%)
7. **UNILAK** (Private, 48-65%)
8. **INES-Ruhengeri** (Private, 52-70%)
9. **Catholic University** (Private, 53-72%)
10. **UTTBS** (Private, 45-62%)

### 30+ Programs:
Computer Science, Medicine, Engineering, Business, Law, Nursing, IT, Architecture, Agriculture, Biotechnology, Tourism, Education, Economics, and more!

---

## 🧠 How the Matching Algorithm Works

### Multi-Criteria Scoring (0-100 points)

1. **Marks Match (30 points)**
   - Student aggregate ≥ school cutoff
   - Higher marks = higher score

2. **Program Match (30 points)**
   - School offers student's desired program
   - Exact match = 30 points
   - Related program = 25 points

3. **Location Match (20 points)**
   - Same district = 20 points
   - Same province = 15 points  
   - Different location = 5 points

4. **Subject Compatibility (20 points)**
   - School accepts student's combination (PCM, PCB, MEG, etc.)
   - Match = 20 points, partial = 5 points

### Match Quality Display
- 🌟 **Excellent** (80-100): Perfect match!
- ✅ **Good** (60-79): Strong candidate
- 📊 **Possible** (<60): Consider applying

---

## 🔒 Security Best Practices

### Never Commit Sensitive Data
- `.env` already in `.gitignore`
- Share credentials securely (not via GitHub)

### For Cloud Databases
- Use strong passwords
- Restrict IP access (if provider supports)
- Create read-only users for viewers:
  ```sql
  CREATE USER 'viewer'@'%' IDENTIFIED BY 'password';
  GRANT SELECT ON ishuri_connect.* TO 'viewer'@'%';
  ```

---

## 🐛 Troubleshooting

### "Access denied for user"
- ✅ Check password in `.env`
- ✅ Verify user has remote access (for cloud DBs)
- ✅ Check if IP is whitelisted

### "Can't connect to MySQL server"
- ✅ Verify MySQL is running
- ✅ Check host/port in `.env`
- ✅ Firewall not blocking connection

### "ModuleNotFoundError"
- ✅ Activate virtual environment: `.\ishuri\Scripts\Activate.ps1`
- ✅ Install dependencies: `pip install -r requirements.txt`

### "Database already exists"
- ✅ Normal! App uses existing database
- ✅ To reset: Drop database and rerun

---

## 📊 Database Schema

### Tables Created:
1. **students** - Comprehensive profiles (aggregate, combination, preferences)
2. **schools** - Universities with cutoffs, locations, requirements
3. **programs** - Programs offered (cutoffs, fees, duration, requirements)
4. **applications** - Student applications with status tracking

### Relationships:
- Students → Applications (1:many)
- Schools → Programs (1:many)
- Schools → Applications (1:many)

---

## 🚀 Innovation Roadmap

### Phase 1: Core Features (v1.0)
1. ✅ Intelligent school matching algorithm
2. ✅ Comprehensive student profiles (aggregate, combinations, location)
3. ✅ Detailed school database (10 universities, 30+ programs)
4. ✅ Multi-criteria scoring (marks, program, location, subjects)
5. ✅ Auto-database initialization

### Phase 2: Enhanced Features (v2.0)
6. 🔄 Application status tracking system
7. 🔄 Document upload (transcripts, IDs)
8. 🔄 Email notifications
9. 🔄 Export recommendations to PDF
10. 🔄 SMS integration for updates

### Phase 3: Advanced Features (v3.0)
11. 🔄 Web interface (Flask/Django)
12. 🔄 Student dashboard with analytics
13. 🔄 Admin panel for school management
14. 🔄 AI-powered program suggestions based on trends

### Competitive Advantages
- 🎯 Local focus: Rwandan universities & programs
- 🧠 Intelligent matching: Multi-criteria algorithm
- 🚀 Easy setup: Auto-initialization, cloud database
- 📚 Educational: Demonstrates OOP, MySQL, algorithms
- 👥 Team-friendly: Cloud database collaboration

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push: `git push origin feature-name`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 💬 Support

For issues or questions, please open an issue on GitHub.

---

## 👤 Author

**Lucky D. (@luckydus5)**
- GitHub: [@luckydus5](https://github.com/luckydus5)
- Project: Ishuri-Connect
- Purpose: School Project - OOP with MySQL

---

## 🙏 Acknowledgments

- **Python Community**: For mysql-connector-python, colorama, python-dotenv
- **MySQL**: For robust database management
- **Rwanda Education Board**: For inspiration on university admission processes
- **Learning**: This project demonstrates OOP fundamentals learned in class

---

**Built with ❤️ for Rwandan students seeking higher education**
