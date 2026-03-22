# VMA STEAM Department Website

> Official website for the Vanke Meisha Academy (VMA) STEAM & Computer Science Department — a modern, single-page web application showcasing courses, faculty, events, and resources.

🌐 **Live Site**: [vmasteam.edu](https://vma-steam.example.com) *(replace with your actual URL)*

---

## 🎯 Overview

The VMA STEAM Department Website is a responsive, single-page application built for Vanke Meisha Academy's Science, Technology, Engineering, Arts, and Mathematics (STEAM) department. It serves as the central hub for prospective and current students, parents, and educators to explore the department's academic offerings, meet the faculty, and stay updated on events.

The site emphasizes the department's focus on **advanced computing**, **creative technology**, and **interdisciplinary learning** — reflecting VMA's reputation for academic excellence.

---

## ✨ Features

### 🧭 Navigation & Layout
- **Sticky header** with glassmorphism effect — stays visible while scrolling
- **Smooth-scroll navigation** to all sections
- **Mobile-responsive layout** — adapts gracefully to all screen sizes

### 🎨 Visual Design
- **Dark theme** with a teal/cyan accent color scheme
- **Matrix rain canvas animation** — subtle animated background for a tech-forward aesthetic
- **Gradient logo text** with hover effects on all interactive elements
- **Font Awesome 6** icon library for consistent, expressive iconography

### 👤 Hero Section
- Full-viewport hero with department branding and call-to-action
- Animated entrance of text and buttons

### 📖 About Section
- Department mission and overview
- **Animated statistics** (student count, courses offered, faculty, labs) that count up on scroll

### 👨‍🏫 Faculty Section
- Faculty profiles loaded **dynamically from JSON** (`data/faculty.json`)
- Each card displays: name, role, bio, education, email, and portfolio/research link
- Hover effects with smooth transitions
- **AI Agent Integration** (`agent.py`) — a Python agent that can answer questions about faculty using natural language

### 📚 Courses Section
- **Dynamic course catalog** loaded from `data/courses.json`
- Displays: course title, description, duration, prerequisites, languages/tech stack, and certifications
- 6 courses covering: Advanced Programming, AI, Web Development, Digital Arts, Cybersecurity, and Data Science

### 📅 Events Section
- Timeline-style events loaded from `data/events.json`
- Each event shows date, title, description, and registration link

### 🔗 Resources & Contributors Sections
- Quick-link cards to internal and external learning resources
- Acknowledgment of contributors

### 🔧 Developer Features
- **JSON-driven content** — all content sections (courses, faculty, events) are data-driven, making updates easy without touching HTML
- **AI Agent** (`agent.py`) powered by OpenAI for answering department-related questions
- **Flask web server** (`app.py`) for local development and API endpoints
- **GitHub Actions CI/CD** (`.github/workflows/agent.yml`) for automated testing
- **Dev Container** (`.devcontainer/`) for consistent development environments

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | HTML5, CSS3, Vanilla JavaScript (ES6+) |
| **Icons** | Font Awesome 6.4 |
| **Backend** | Python, Flask |
| **AI** | OpenAI API (`agent.py`) |
| **Data** | JSON (no database required) |
| **CI/CD** | GitHub Actions |
| **Dev Environment** | Dev Container (VS Code) |

---

## 📁 Project Structure

```
vmaSteamwebsite/
├── index.html          # Main HTML — single-page application structure & CSS
├── js/
│   └── main.js         # Dynamic content loader (courses, faculty, events from JSON)
├── css/
│   └── style.css       # All styles — dark theme, animations, responsive design
├── data/
│   ├── courses.json    # Course catalog
│   ├── events.json     # Department events
│   └── faculty.json     # Faculty profiles
├── website/            # Static assets / production build output
├── agent.py            # AI agent — answers questions about faculty & department
├── app.py              # Flask web server & API routes
├── requirements.txt    # Python dependencies
├── .devcontainer/      # Dev Container config
├── .github/
│   └── workflows/
│       └── agent.yml   # GitHub Actions CI workflow
└── README.md           # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key (for the AI agent)

### Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/JasonZeng24/vmaSteamwebsite.git
cd vmaSteamwebsite

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"

# 5. Run the Flask server
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

> **Note**: You can also open `index.html` directly in a browser for frontend-only development (no server needed for the main site).

### Updating Content

All content is managed via JSON files — no code changes needed:

- **`data/faculty.json`** — Add/edit faculty profiles
- **`data/courses.json`** — Add/edit courses
- **`data/events.json`** — Add/edit upcoming events

---

## 🤖 AI Agent

The included `agent.py` is a Python AI agent that uses OpenAI's GPT models to answer natural language questions about the STEAM department — faculty backgrounds, course details, event info, and more.

```bash
# Run as a CLI chat
python agent.py

# Or import into app.py to power a web-based Q&A endpoint
```

---

## 🎓 Courses Offered

| # | Course | Duration | Prerequisites |
|---|---|---|---|
| 1 | Advanced Programming (Java, Python, C++) | Full Year | Intro to CS |
| 2 | Artificial Intelligence & Machine Learning | Semester | Advanced Programming |
| 3 | Web Development (React, Node.js) | Semester | Intro to Programming |
| 4 | Digital Arts & Media (Blender, Unity) | Full Year | None |
| 5 | Cybersecurity & Ethical Hacking | Semester | Networking Fundamentals |
| 6 | Data Science (Python, Pandas, Tableau) | Semester | Statistics, Programming |

---

## 👨‍🏫 Faculty

- **Jason Hum** — Department Chair | Ph.D. CS, Stanford | Distributed Systems & Cloud Computing
- **Harry** — Programming & Algorithms | M.S. CS, MIT | Former Google Engineer, Competitive Programming
- **Joey** — AI & Robotics | Ph.D. Robotics, Carnegie Mellon | Former NASA JPL Researcher
- **Gabriel** — Digital Arts & Design | M.F.A. Digital Arts, RISD | Game Design & Animation

---

## 📜 License

This project is for educational use by Vanke Meisha Academy. All rights reserved.
