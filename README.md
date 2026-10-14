# Python-TCP-Chat-Application
Multi-User Chat System using TCP Sockets and Python - UCAS University Project
# Multi-User TCP Chat Application 💬

A real-time multi-user chat system built using Python Sockets and TCP protocol, developed as a **University Project** at the **University College of Applied Sciences (UCAS)**.

---

## 🖼️ Project Preview

![Presentation Cover](C:\Users\H.P\Pictures\Screenshots\Screenshot 2026-10-14 150214.png)

### Live Execution in VS Code
![Chat Execution](image_5ccc93.jpg)

---

## 🚀 Project Overview

The application utilizes a **Client-Server Architecture** (`SOCK_STREAM`) to ensure reliable, ordered, and error-free message delivery across clients. 
- **Server (`server.py`)**: Manages incoming connections, handles multi-threading (`threading`) to serve multiple clients simultaneously, and broadcasts messages to all active users.
- **Client (`client.py`)**: Runs dual threads—one for continuously listening for incoming messages from the server, and the main thread for user input.

---

## 🛠️ Key Technical Features

- **Reliability (TCP)**: Guarantees full data delivery and packet ordering without loss.
- **Multi-Threading**: Uses Python threads (`threading`) to handle multiple concurrent client sessions without blocking the system.
- **Broadcast Mechanism**: Automatically distributes any message sent by a client to all other connected peers instantly.
- **Safe Disconnection**: Exception handling (`try-except`) to safely clean up disconnected clients and notify others.

---

## 📂 Project Files

- `server.py` - Core server script managing client sockets and broadcasting.
- `client.py` - Client application script with background listening and input threads.
- `مشروع شبكات نظري.pptx` - Comprehensive project presentation documentation.

---

## 🏛️ Academic Context
- **Institution:** University College of Applied Sciences (UCAS)
- **Major:** Cybersecurity Engineering (1st Year Project)
- **Course:** Computer Networking Principles
- **Student:** Basher Alakklouk
- **Instructor:** Eng. Mahmoud Al-Sheikh Khalil
