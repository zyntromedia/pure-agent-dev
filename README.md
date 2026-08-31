# 🤖 Pure Agent Dev — ZyntroMedia

> **AI-Powered Monitoring & Automation Platform** — Built with Python, GitHub Actions, and enterprise-grade workflows

---

## 📋 Overview

**pure-agent-dev** is an automation and monitoring platform designed to run continuously on GitHub Actions — no servers required. Currently includes **link availability monitoring** with LINE notifications, with expandable architecture for additional AI agents, providers, and workflows.

---

## ✨ Features

### 🔗 Link Monitor (Active)
- 🔍 **Auto-check status** of every product link periodically
- 📨 **LINE notifications** — only sends when status changes (no spam)
- 🔁 **Auto-retry** on network hiccups (up to 3 attempts)
- 📝 **Full logging** on every run
- 🤖 **Zero-cost automation** via GitHub Actions scheduler
- ✅ **Idempotent** — safe to run concurrently or repeatedly

### 🏗️ Platform Capabilities
- 📁 **Modular structure** — providers, schemas, workflows separated
- ✅ **Pre-commit hooks** + CI quality checks
- 🔒 **CodeQL security scanning** enabled
- 🧪 **Test suite** with automated run workflows
- 📋 **Standardized schemas** for compute & automation tasks

---

## 📁 Project Structure

```
pure-agent-dev/
├── .github/
│   └── workflows/           # CI, monitoring, security workflows
├── .skills/                 # AI skill definitions
├── docs/                    # Documentation
├── providers/               # Integration providers (base + impl)
│   └── base.py
├── schemas/                 # Data models & schemas
│   └── compute.py
├── tests/                   # Test suite
├── workflows/               # Compliance & automation workflows
├── compute.service.py       # Core compute service
├── pyproject.toml           # Project metadata & config
├── requirement.txt          # Python dependencies
├── .ci.yaml                 # CI configuration
├── .pre-commit-config.yaml  # Pre-commit hooks
├── .env                     # Local environment variables (NOT committed)
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/zyntromedia/pure-agent-dev.git
cd pure-agent-dev
```

### 2. Install Dependencies
```bash
pip install -r requirement.txt
```

### 3. Local Environment Setup
Create `.env` file in root:
```env
MY_LINE_KEY=your_channel_access_token
MY_LINE_USER_ID=your_line_user_id
```

> ⚠️ **Never commit `.env`** — already in `.gitignore`

---

## ⚙️ GitHub Actions Setup

### Add Repository Secrets
Go to **Settings → Secrets and variables → Actions** → Add these secrets:

| Secret Name | Purpose |
|---|---|
| `MY_LINE_KEY` | LINE Channel Access Token |
| `MY_LINE_USER_ID` | LINE User ID for notifications |

### Configure Schedule
Edit workflow file `.github/workflows/monitor.yml`:
```yaml
on:
  schedule:
    - cron: '0 */2 * * *'    # Every 2 hours
    # - cron: '*/30 * * * *'  # Every 30 minutes
    # - cron: '0 9 * * *'      # Daily at 09:00
```

### Manual Trigger
Go to **Actions → Link Monitor → Run workflow** → Click **Run**

---

## 📨 Notification Examples

| Scenario | Message Sent to LINE |
|---|---|
| Link just went down | 🚫 **{Name}** — Link just stopped working! |
| Link recovered | ✅ **{Name}** — Link is back online! 🎉 |
| Still down | *(No notification — suppressed)* |
| Still healthy | *(No notification — suppressed)* |

---

## 🛠 Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.11+ |
| HTTP Client | `requests` |
| Env Management | `python-dotenv` |
| Notifications | LINE Messaging API |
| CI/CD | GitHub Actions |
| Security | CodeQL scanning |
| Pre-commit | `pre-commit` framework |
| Hosting | GitHub Actions runners (free) |

---

## 🧪 Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=. --cov-report=term-missing
```

---

## 🔒 Security & Compliance

- ✅ **CodeQL Analysis** — Runs on every push
- ✅ **Pre-commit Hooks** — Linting, secrets detection, formatting
- ✅ **Secrets in GitHub Only** — Never committed to repo
- ✅ **Comprehensive `.gitignore`** — Prevents accidental leaks
- ✅ **Branch Protection Rules** — Configurable via repo settings

---

## 📌 Roadmap

- [x] Link availability monitor + LINE alerts
- [ ] Add Google Search / Shopee/Lazada/TikTok scraping
- [ ] SQLite database for history & analytics
- [ ] Email/Slack notification providers
- [ ] Dashboard & analytics reporting
- [ ] Docker containerization
- [ ] More AI agent skills in `.skills/`

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`feature/description`)
3. Commit your changes
4. Open a Pull Request — CI will automatically run tests & security scans

---

## 📄 License

**Private Repository** — Copyright © 2026 ZyntroMedia. All rights reserved.

---

Would you like me to save this directly as `README.md` content for you to commit? Or should I adjust the tone/sections further? 😊
