# 🌸 Heavenly Archive (天官赐福档案馆)

<div align="center">

![Heaven Official's Blessing](https://img.shields.io/badge/Inspired%20By-Heaven%20Official's%20Blessing-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green?style=for-the-badge&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A beautiful event logging and achievement tracking system inspired by Heaven Official's Blessing**

*Record your journey with celestial elegance* ✨

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

</div>

---

## 📖 About

**Heavenly Archive** is an elegant event logging and achievement tracking system that brings the mystical aesthetic of *Heaven Official's Blessing (天官赐福)* to your personal documentation. Just as the heavens keep records of mortal deeds, this system helps you track your accomplishments, challenges, and milestones in a beautiful, organized manner.

### Inspiration

Inspired by the celestial realm's record-keeping in TGCF, where every deed is documented and achievements are celebrated with divine elegance, this project transforms mundane logging into an experience worthy of the heavenly courts.

---

## ✨ Features

### 🏯 Core Features
- **📜 Event Logging**: Record events with categories like Virtues, Trials, Victories, and Legendary Deeds
- **🎖️ Achievement System**: Earn celestial badges and divine honors
- **🌙 Beautiful UI**: Anime-inspired interface with traditional Chinese aesthetics
- **🔍 Smart Search**: Find events by keywords, dates, categories, or tags
- **📊 Statistics Dashboard**: Track your progress with elegant visualizations
- **🎨 Customizable Themes**: Choose from various celestial color schemes
- **📝 Rich Text Support**: Add formatted notes, images, and links
- **🔒 Encryption**: Secure your records with "heavenly seals"
- **☁️ Cloud Sync**: Sync across devices (optional)
- **📤 Export**: Generate beautiful PDF reports

### 🎭 Achievement Categories
- **👑 Crown Prince**: Major life achievements
- **👻 Ghost King**: Overcoming significant challenges  
- **⚔️ Martial God**: Skills and expertise milestones
- **🌸 Heavenly Official**: Daily virtues and good deeds
- **📚 Scholar**: Learning and knowledge acquisition
- **🎮 Gaming Legends**: Game-specific achievements

---

## 🚀 Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Git

### Quick Start

```bash
# Clone the repository
git clone https://github.com/KaizerAE/heavenly-archive.git
cd heavenly-archive

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python scripts/init_db.py

# Run the application
python main.py
```

The application will be available at `http://localhost:8000`

---

## 🎯 Usage

### Creating Your First Event

```python
from heavenly_archive import EventLogger

# Initialize logger
logger = EventLogger()

# Create an event
event = logger.create_event(
    title="Completed First Project",
    category="virtue",
    description="Successfully launched my first web application",
    tags=["programming", "milestone"],
    importance="legendary"
)
```

### Web Interface

1. **Dashboard**: View your recent events and statistics
2. **Events**: Browse, search, and filter all your records  
3. **Achievements**: Track your celestial badges
4. **Calendar**: View events in a heavenly calendar format
5. **Reports**: Generate beautiful PDF summaries

### CLI Usage

```bash
# Add a new event
python cli.py add --title "My Achievement" --category virtue

# List recent events
python cli.py list --limit 10

# Search events
python cli.py search --query "programming"

# View statistics
python cli.py stats
```

---

## 📁 Project Structure

```
heavenly-archive/
├── backend/
│   ├── api/              # FastAPI routes
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Business logic
│   └── utils/            # Helper functions
├── frontend/
│   ├── assets/           # Images, icons, fonts
│   ├── components/       # React components
│   ├── pages/            # Page components
│   └── styles/           # CSS/SCSS files
├── database/
│   └── migrations/       # DB migrations
├── scripts/
│   └── init_db.py        # Database initialization
├── tests/                # Test files
├── docs/                 # Documentation
├── main.py               # Application entry point
├── cli.py                # Command-line interface
├── requirements.txt      # Python dependencies
└── README.md
```

---

## 🎨 Screenshots

### Dashboard
![Dashboard](docs/images/dashboard.png)
*Your celestial command center*

### Event Log
![Events](docs/images/events.png)
*Beautifully organized event records*

### Achievements
![Achievements](docs/images/achievements.png)
*Track your divine accomplishments*

---

## 🛠️ Technologies

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: ORM for database operations
- **Pydantic**: Data validation
- **SQLite/PostgreSQL**: Database options
- **Python-Jose**: JWT authentication

### Frontend (Planned)
- **React**: UI framework
- **TypeScript**: Type-safe JavaScript
- **TailwindCSS**: Utility-first styling
- **Framer Motion**: Smooth animations
- **Recharts**: Data visualization

---

## 🗺️ Roadmap

- [x] Project initialization
- [x] Basic README structure
- [ ] Backend API implementation
- [ ] Database schema design
- [ ] Event CRUD operations
- [ ] Achievement system
- [ ] Frontend UI design
- [ ] Authentication system
- [ ] Cloud sync feature
- [ ] Mobile app (Future)
- [ ] AI-powered event suggestions (Future)

---

## 🤝 Contributing

Contributions are welcome! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **MXTX**: Creator of Heaven Official's Blessing (天官赐福)
- **Bilibili**: For the beautiful anime adaptation
- All contributors and supporters of this project

---

## 📧 Contact

**KaizerAE**
- GitHub: [@KaizerAE](https://github.com/KaizerAE)
- Project Link: [https://github.com/KaizerAE/heavenly-archive](https://github.com/KaizerAE/heavenly-archive)

---

<div align="center">

### "May this humble archive serve you well on your journey" 🌸

*Built with ❤️ and inspired by 天官赐福*

⭐ Star this repo if you find it useful!

</div>
