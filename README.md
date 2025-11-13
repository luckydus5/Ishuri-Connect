# Ishuri-Connect

A student-school matching platform that helps students find educational institutions that match their academic profile and course interests.

## Features

- Student registration with profile creation
- Academic marks tracking and average calculation
- Email validation
- School recommendation based on:
  - Course interest
  - Academic performance (average marks)
  - School admission requirements
- Database support for persistent storage (optional)
- User-friendly CLI interface

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

```bash
python main.py
```

### Registration Flow

1. Enter your first name
2. Enter your last name
3. Provide a valid email address
4. Specify your course interest
5. Enter your marks (press Enter without input to finish)
6. View your average and school recommendations

### Example Session

```
==================================================
    ISHURI CONNECT - School Matching Platform
==================================================

Welcome! This platform helps students find schools
that match their academic profile and interests.

Press Ctrl+C at any time to exit.

==================================================

 === Student Registration Process Initiated. =======

Enter your first name: John
Enter your last name: Doe
Enter your email address: john.doe@example.com
Which course are you interested in? Computer Science

Thank you John Doe for registering with email: john.doe@example.com
Now enter your marks (press Enter without typing to finish):

Enter marks 1: 85
Enter marks 2: 90
Enter marks 3: 78
Enter marks 4: 

==================================================
Registration Successful!
Welcome to Ishuri Connect, John Doe!
Your average marks: 84.33
==================================================

Searching for schools offering Computer Science...

Found 1 school(s) that match your profile:

1. University of Rwanda
   Required minimum: 70%
   Your average: 84.33%
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