# 🎮 SA-MP Server Watchdog

> Hi, my name is **Benyamin**. This `server_always_run` program works in such a way that after your server executable is shut down, it automatically restarts it and does not let it remain offline.
>
> It took approximately **2 hours** to make. This version is complete and has no issues.

A lightweight Python script that automatically restarts your **SA-MP** (`samp-server.exe`) server if it crashes or stops running.

---

## 📋 Features

- Monitors `samp-server.exe` continuously
- Automatically restarts the server when it goes offline
- Minimal resource usage with sleep intervals
- Simple, no-dependency setup

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- Windows OS
- `samp-server.exe` present in the same directory as the script

### Installation

1. Clone this repository or download `server_always_run.py`
2. Place `server_always_run.py` in the **same folder** as your `samp-server.exe`

```
your-server-folder/
├── samp-server.exe
├── server_always_run.py
└── ...
```

3. Run the script:

```bash
python server_always_run.py
```

---

## ⚙️ How It Works

1. On launch, the script checks if `samp-server.exe` exists in the current directory
2. It then enters a loop, checking the Windows task list every second
3. If `samp-server.exe` is **not** found in the running processes, it starts it automatically
4. If it **is** running, the script waits and checks again

---

## 🔧 SA-MP vs open.mp

| Server Type | Executable to use |
|-------------|------------------|
| **SA-MP** | `samp-server.exe` (default) |
| **open.mp** | Change the executable name in the script to your open.mp binary |

> If you want to run it for **open.mp**, you must change the `samp-server.exe` reference in the source code to your open.mp server executable name.

---

## 📌 Notes

- This script is **Windows only** (uses `tasklist` and `start` commands)
- Keep the terminal/console open while the watchdog is running
- Make sure Python is added to your system PATH

---

## 👤 Author

**BenyVK**
- Discord: `BenyVK#0000`
- Telegram: [@i36vk](https://t.me/i36vk)
