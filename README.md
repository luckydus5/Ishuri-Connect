# Ishuri-Connect

A student-school matching platform that helps students find educational institutions that match their academic profile and course interests.

## Features

- ✨ **Beautiful colored CLI interface** with icons and professional formatting
- 👤 Student registration with profile creation
- 📊 Academic marks tracking and average calculation
- 📧 Email validation
- 🎯 School recommendation based on:
  - Course interest
  - Academic performance (average marks)
  - School admission requirements
- 💾 Database support for persistent storage (optional)
- 🎨 Modern user experience with visual feedback

## Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher (optional, for database features)
- Virtual environment (recommended)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/luckydus5/Ishuri-Connect.git
   cd Ishuri-Connect
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv ishuri
   .\ishuri\Scripts\Activate.ps1
   
   # Linux/Mac
   python3 -m venv ishuri
   source ishuri/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   This will install:
   - `mysql-connector-python` - MySQL database driver
   - `python-dotenv` - Environment variable management
   - `colorama` - Colored terminal output

4. **Configure database (optional)**
   - Create a MySQL database
   - Run the schema: `mysql -u root -p < sql/schema.sql`
   - Update `.env` file with your database credentials:
     ```
     DB_HOST=localhost
     DB_USER=root
     DB_PASSWORD=your_password
     DB_NAME=ishuri_connect
     ```

## Usage

### Run the application

**Easiest way - Double-click:**
- Windows: Double-click `run.bat`
- PowerShell: Right-click `run.ps1` → Run with PowerShell

**Or from command line:**

**Windows (Command Prompt):**
```cmd
run.bat
```

**Windows (PowerShell):**
```powershell
.\run.ps1
```

**With virtual environment (recommended):**
```bash
# Windows
.\ishuri\Scripts\python.exe main.py

# Linux/Mac
./ishuri/bin/python main.py
```

**⚠️ Important:** Don't run `python main.py` directly - it will use your system Python which doesn't have the required packages. Always use the virtual environment or the run scripts!

### Registration Flow

1. Enter your first name
2. Enter your last name
3. Provide a valid email address
4. Specify your course interest
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
├── main.py              # Application entry point
├── cli.py               # CLI interface and user interaction
├── utils.py             # Utility functions (validation, calculations)
├── models.py            # Data models (placeholder)
├── db.py                # Database operations (placeholder)
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in git)
├── .gitignore          # Git ignore file
├── sql/
│   └── schema.sql      # Database schema
└── ishuri/             # Virtual environment (not in git)
```

## Available Schools (Default)

The application comes with pre-configured schools:

- **University of Rwanda** - Computer Science (min: 70%)
- **Mount Kenya University** - Business (min: 55%)
- **AUCA** - Nursing (min: 60%)
- **ULK** - Law (min: 65%)

## Future Enhancements

- [ ] Complete database integration for persistent storage
- [ ] Application tracking system
- [ ] Multiple course options per school
- [ ] Admin panel for school management
- [ ] Email notifications
- [ ] Web interface
- [ ] Student dashboard
- [ ] Application status tracking

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

For issues or questions, please open an issue on GitHub.

## Author

**luckydus5**
- GitHub: [@luckydus5](https://github.com/luckydus5)