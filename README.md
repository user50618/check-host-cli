# 🌐 Check-Host.net CLI Tool

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/) [![Requests Library](https://img.shields.io/badge/requests-2.25%2B-green.svg)](https://docs.python-requests.org/) [![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE) [![GitHub Stars](https://img.shields.io/badge/stars-⭐-yellow.svg)]()

**یک ابزار خط فرمان قدرتمند و کاربرپسند برای بررسی میزبان‌ها با استفاده از API سرویس check-host.net**

[English](#english) | [فارسی](#persian)

</div>

---

## 🇬🇧 English <a id="english"></a>

### 🎯 Overview

Check-Host.net CLI Tool is a comprehensive command-line interface for the [Check-Host.net](https://check-host.net) service. It allows you to perform various network checks from multiple global locations directly from your terminal with beautiful, formatted output.

### ✨ Features

- **🌐 Multiple Check Types**
  - Ping check with detailed statistics
  - HTTP/HTTPS website availability and response time
  - TCP port connection testing
  - DNS record resolution (A, AAAA records)

- **🎨 Beautiful Output**
  - Colored and formatted tables
  - Human-readable summaries
  - Raw JSON output option for debugging
  - Real-time status indicators

- **🌍 Global Network**
  - Access to 60+ check nodes worldwide
  - View complete node list with locations
  - Specify custom nodes for checks
  - Support for short node names (e.g., `ir1`, `de1`, `us1`)

- **⚡ User-Friendly**
  - Interactive menu system
  - Default values for quick usage
  - Clear error messages
  - No API key required (free service)

### 🚀 Installation

#### Prerequisites
- Python 3.6 or higher
- pip package manager

#### Quick Install

```bash
# Clone the repository
git clone https://github.com/mehdirzfx/check-host-cli.git
cd check-host-cli

# Install requirements
pip install requests

# Run the tool
python check_host.py
```

Or download the script directly:

```bash
wget https://raw.githubusercontent.com/mehdirzfx/check-host-cli/main/check_host.py
pip install requests
python check_host.py
```

### 📖 Usage Guide

#### Main Menu

```
============================================================
🖥  Host Check Tool using check-host.net API
============================================================

📋 Main Menu:
   1. 🌐 Ping Check
   2. 🌐 HTTP Check
   3. 🌐 TCP Check
   4. 🌐 DNS Check
   5. 📡 View Nodes List
   6. 🚪 Exit
```

#### Examples

**1. HTTP Check with Specific Nodes**

```bash
🔷 Select option (1-6): 2
🔷 Enter host address: example.com
🔷 Maximum number of nodes: 3
🔷 Specify specific nodes? (y/n): y
🔷 Enter node names: ir1,de1,us1
```

**Sample Output:**

```
================================================================================
📊 HTTP CHECK RESULTS SUMMARY
================================================================================
Node     Country  Status     Code   Time(ms)   IP              Message
--------------------------------------------------------------------------------
ir1      IR       ✅ Success  200    143.9      93.184.216.34   OK
de1      DE       ✅ Success  200    89.5       93.184.216.34   OK
us1      US       ✅ Success  200    184.3      93.184.216.34   OK
================================================================================
```

**2. View Available Nodes**

```bash
🔷 Select option (1-6): 5

🌍 AVAILABLE CHECK NODES SUMMARY
================================================================================
#    Node Name                      Country      City                 IP              ASN
--------------------------------------------------------------------------------
1    ir1.node.check-host.net        IR - Iran    Tehran              5.253.30.82     AS18978
2    de1.node.check-host.net        DE - Germany Falkenstein         46.4.143.48     AS24940
3    us1.node.check-host.net        US - USA     Los Angeles         5.253.30.82     AS18978
...
================================================================================
```

### 🛠️ Advanced Features

#### Node Name Shortcuts
You can use short node names (just the prefix) for convenience:
- ✅ `ir1` → `ir1.node.check-host.net`
- ✅ `de1` → `de1.node.check-host.net`
- ✅ `us3` → `us3.node.check-host.net`

#### Response Parsing
The tool automatically parses raw JSON responses into human-readable tables:
- Ping: Shows packet loss, min/avg/max RTT
- HTTP: Displays status code, response time, server IP
- TCP: Shows connection time or error details
- DNS: Lists resolved A and AAAA records

### 🔧 Configuration

No configuration needed! The tool works out of the box with the public Check-Host.net API.

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

---

## 🇮🇷 فارسی <a id="persian"></a>

### 🎯 معرفی

ابزار خط فرمان Check-Host.net یک رابط کاربری حرفه‌ای برای سرویس [Check-Host.net](https://check-host.net) است. با این ابزار می‌توانید انواع بررسی‌های شبکه را از نقاط مختلف جهان مستقیماً از ترمینال خود انجام دهید.

### ✨ ویژگی‌ها

- **🌐 انواع بررسی**
  - بررسی Ping با آمار دقیق
  - بررسی HTTP/HTTPS وب‌سایت‌ها
  - تست اتصال پورت TCP
  - بررسی رکوردهای DNS

- **🎨 خروجی زیبا**
  - جداول رنگی و مرتب
  - خلاصه قابل فهم
  - نمایش خروجی JSON خام برای اشکال‌زدایی

- **🌍 شبکه جهانی**
  - دسترسی به بیش از ۶۰ گره بررسی در سراسر جهان
  - مشاهده لیست کامل گره‌ها
  - انتخاب گره‌های دلخواه
  - پشتیبانی از نام‌های کوتاه

### 🚀 نصب

```bash
# دریافت کد
git clone https://github.com/mehdirzfx/check-host-cli.git
cd check-host-cli

# نصب پیش‌نیاز
pip install requests

# اجرای برنامه
python check_host.py
```

### 📖 راهنما

#### منوی اصلی

```
============================================================
🖥  Host Check Tool using check-host.net API
============================================================

📋 Main Menu:
   1. 🌐 Ping Check
   2. 🌐 HTTP Check
   3. 🌐 TCP Check
   4. 🌐 DNS Check
   5. 📡 View Nodes List
   6. 🚪 Exit
```

#### مثال‌ها

**بررسی HTTP با گره‌های خاص:**

```bash
🔷 Select option (1-6): 2
🔷 Enter host address: example.com
🔷 Maximum number of nodes: 3
🔷 Specify specific nodes? (y/n): y
🔷 Enter node names: ir1,de1,us1
```

---

## 🚀 درخواست‌های توسعه (Feature Requests)

### پیشنهادات برای نسخه‌های آینده:

#### 1. **حالت خودکار (Automation Mode)**
   - امکان اجرا بدون منوی تعاملی با آرگومان‌های خط فرمان
   - پشتیبانی از فایل کانفیگ
   ```bash
   python check_host.py --check http --host example.com --nodes ir1,de1 --output json
   ```

#### 2. **گزارش‌گیری پیشرفته**
   - ذخیره نتایج در فایل‌های CSV/JSON
   - مقایسه نتایج بین بررسی‌های مختلف
   - نمودارهای ساده از روند تغییرات

#### 3. **بررسی‌های زمان‌بندی شده**
   - امکان تعریف وظایف دوره‌ای
   - ارسال هشدار در صورت مشکل
   ```python
   # مثال فایل کانفیگ
   {
     "checks": [
       {"type": "http", "host": "example.com", "interval": 300, "nodes": ["ir1", "de1"]}
     ]
   }
   ```

#### 4. **پشتیبانی از پروتکل‌های بیشتر**
   - UDP port check
   - ICMP options
   - Custom port ranges
   - SSL/TLS certificate check

#### 5. **واسط کاربری گرافیکی ساده**
   - نسخه TUI با کتابخانه `rich` یا `textual`
   - نمایش لحظه‌ای پیشرفت بررسی‌ها

#### 6. **مدیریت خطا و لاگینگ**
   - سیستم لاگینگ حرفه‌ای
   - ذخیره خطاها برای تحلیل بعدی
   - قابلیت retry خودکار

#### 7. **بین‌المللی‌سازی (i18n)**
   - پشتیبانی از زبان‌های بیشتر
   - سیستم ترجمه پویا

#### 8. **ابزارهای جانبی**
   - ماشین‌حساب subnet
   - WHOIS lookup
   - Traceroute از گره‌های مختلف

### 🤝 مشارکت در توسعه

اگر مایل به پیاده‌سازی هر یک از این ویژگی‌ها هستید، لطفاً:
1. یک Issue جدید باز کنید
2. پیشنهاد خود را توضیح دهید
3. اگر امکانش هست، نمونه کد یا طرح اولیه ارائه دهید

### 📝 نکات برای توسعه‌دهندگان

```bash
# نصب برای توسعه
pip install -r requirements-dev.txt

# اجرای تست‌ها
pytest tests/

# فرمت کردن کد
black check_host.py
```

---

## 📜 License

MIT License - feel free to use this project for any purpose.

## 📧 Contact

- **Email**: semicalon@outlook.com
- **GitHub**: [mehdirzfx](https://github.com/mehdirzfx)

---

<div align="center">
**⭐ If you find this tool useful, please star it on GitHub! ⭐**
</div>