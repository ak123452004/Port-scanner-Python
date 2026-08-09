# 🔐 Port Scanner (Python)

A beginner-friendly **TCP Port Scanner** developed using Python. This project demonstrates basic networking and cybersecurity concepts by checking whether TCP ports are open on a target system.

> ⚠️ **Ethical Use Only:** Use this tool only on systems, networks, and devices that you own or have explicit permission to test.

---

## 📌 Internship Details

| Field             | Details                          |
| ----------------- | -------------------------------- |
| **Intern ID**     | CMQ7VDB7B0                       |
| **Full Name**     | Ankit Kumar                      |
| **No. of Weeks**  | 8                                |
| **Project Name**  | Port Scanner (Python)            |
| **Project Scope** | Cyber Security & Ethical Hacking |

---

## 📖 About the Project

A port scanner is a cybersecurity tool used to identify open TCP ports on a target system.

Open ports can indicate services that are running and accepting network connections.

This project uses Python's built-in `socket` library to:

* Resolve a hostname to an IP address
* Scan a specified range of TCP ports
* Detect open ports
* Identify common TCP services
* Display scan results in the terminal
* Handle invalid hostnames and port ranges

---

## 🎯 Objectives

The main objectives of this project are:

1. Learn basic network programming in Python.
2. Understand TCP ports and network services.
3. Practice Python functions and loops.
4. Learn how the `socket` module works.
5. Understand basic concepts of network reconnaissance.
6. Build a simple cybersecurity tool for educational purposes.

---

## 🛠️ Technologies Used

* **Python 3**
* **Socket Programming**
* **TCP/IP**
* **Command Line Interface**
* **Git & GitHub**

### Python Modules

The project uses only Python's standard library:

```text
socket
argparse
datetime
```

No external Python packages are required.

---

## 📂 Project Structure

```text
Port-Scanner-Python/
│
├── port_scanner.py
├── README.md
└── requirements.txt
```

---

## ⚙️ How It Works

The scanner follows these basic steps:

```text
Start
  ↓
Take Target IP/Hostname
  ↓
Resolve Hostname
  ↓
Take Port Range
  ↓
Create TCP Socket
  ↓
Attempt Connection
  ↓
Is Port Open?
  ├── Yes → Display Port
  └── No  → Continue
  ↓
Finish Scan
```

---

## 💻 Installation

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the installation:

```bash
python --version
```

or:

```bash
python3 --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Port-Scanner-Python.git
```

### 3. Open the Project Directory

```bash
cd Port-Scanner-Python
```

No additional packages are required.

---

## 🚀 How to Run

### Scan localhost

```bash
python port_scanner.py 127.0.0.1
```

The default scan checks ports:

```text
1 - 1024
```

### Scan a specific port range

```bash
python port_scanner.py 127.0.0.1 -s 1 -e 100
```

### Scan a hostname

```bash
python port_scanner.py example.com -s 1 -e 100
```

Only scan systems for which you have permission.

---

## 🖥️ Example Output

```text
==================================================
        PYTHON PORT SCANNER
==================================================

Target   : 127.0.0.1
IP       : 127.0.0.1
Port     : 1 - 100
Started  : 2026-08-09 13:00:00
--------------------------------------------------

Open Ports:
  Port 22    -> ssh
  Port 80    -> http

--------------------------------------------------
Scan completed: 2026-08-09 13:00:05
==================================================
```

The actual results will depend on the services running on the target system.

---

## 🔍 Features

### 1. Hostname Resolution

The program can accept either:

```text
127.0.0.1
```

or:

```text
localhost
```

or a hostname.

### 2. Custom Port Range

Users can choose the starting and ending ports.

Example:

```bash
python port_scanner.py 127.0.0.1 -s 20 -e 100
```

### 3. Open Port Detection

The scanner attempts a TCP connection to each port.

If the connection succeeds, the port is reported as open.

### 4. Service Identification

For recognized TCP ports, the program attempts to display the associated service name.

Example:

```text
Port 22 -> ssh
Port 80 -> http
```

### 5. Error Handling

The program handles:

* Invalid hostnames
* Invalid port numbers
* Incorrect port ranges
* Socket connection errors

---

## 🧠 Cybersecurity Concepts Learned

Through this project, the following concepts can be understood:

* Network reconnaissance
* TCP/IP basics
* TCP ports
* Network services
* Client-server communication
* Socket programming
* Port scanning
* Basic ethical hacking methodology

---

## 🔐 Ethical and Legal Disclaimer

This project is created for **educational purposes and authorized security testing**.

Do not scan systems, websites, servers, or networks without proper authorization.

Unauthorized port scanning may violate organizational policies or applicable laws.

Recommended practice targets include:

```text
127.0.0.1
localhost
Your own virtual machine
Your own lab network
Authorized cybersecurity labs
```

---

## 🔮 Future Improvements

Possible improvements for future versions include:

* Multi-threaded scanning
* Faster scanning
* Service/version detection
* Banner grabbing
* TCP and UDP scanning
* Export results to CSV
* Save scan results to a file
* Simple graphical user interface
* Logging functionality
* Scan progress indicator

---

## 📚 Learning Outcome

After completing this project, a beginner should have a better understanding of:

* Python socket programming
* TCP connections
* Network ports
* Basic reconnaissance
* Command-line arguments
* Exception handling
* GitHub project organization
* Ethical cybersecurity practices

---

## 👨‍💻 Author

**Ankit Kumar**

**Intern ID:** CMQ7VDB7B0

**Project:** Port Scanner (Python)

**Duration:** 8 Weeks

**Scope:** Cyber Security & Ethical Hacking

---

## ⭐ Conclusion

The **Port Scanner (Python)** project is a simple introduction to network security and ethical hacking. It demonstrates how Python can be used to establish TCP connections and identify open ports on an authorized target.

This project can serve as a foundation for learning more advanced cybersecurity concepts such as network reconnaissance, vulnerability assessment, and security testing.
