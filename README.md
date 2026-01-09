# Multiplayer Raycaster Engine  
### Flask • HTML Canvas • Online Multiplayer

A **Flask-based web application** hosting an **optimised online multiplayer 3D raycaster engine** built entirely on an **HTML Canvas** renderer.

The project combines a **high-performance client-side engine**, real-time multiplayer networking, and a **secure, API-driven backend**, designed for responsiveness, scalability, and low memory overhead.

---

## 🎮 Overview

This platform delivers a classic raycasting-style 3D engine with modern features:

- Smooth 60 FPS client tick
- Multiplayer world replication
- Modular engine architecture
- Secure, production-ready backend
- REST-driven services and asset pipelines

The system is designed to run efficiently in-browser while supporting multiple concurrent players.

**DEMO VIDEO:** https://github.com/user-attachments/assets/59f46060-d52b-4906-bff6-014e86002822

---

## 🧩 Tech Stack

### Backend
- **Framework:** Flask + Flask Dependencies
- **Database:** MongoDB
- **Auth & Security:** Werkzeug, CSRF protection, Google reCAPTCHA
- **Networking:** UDP-style WebSocket replication
- **Templating:** Jinja2

### Frontend
- **Rendering:** P5.js + HTML Canvas (Raycasting)
- **UI:** JINJA2 + Bootstrap + layered custom CSS
- **Audio:** Web Audio API
- **Input:** Keyboard + Mouse

---

## 🧠 Engine Design

### Core Principles
- Modular architecture
- Memory-efficient data structures
- Minimal shared resources between client and server
- Explicit update and render pipelines

---

### ⏱️ Order of Operations

1. **Client Tick (Target: 60 FPS)**
2. Input Processing
3. Physics & Collision Resolution
4. Camera Update
5. Raycasting & Wall Projection
6. Lighting & Shader Application
7. UI Rendering
8. Network Sync

Some effects are intentionally capped at **30 FPS** to reduce processing cost.

---

## 🎮 Controls

| Action | Input |
|------|------|
| Move | WASD |
| Sprint | Hold Shift |
| Look | Mouse movement |
| Toggle FOV | X |
| Toggle Resolution | C |

---

## 🧍 Character Controller

- Adjustable base movement speed
- Sprint speed multiplier
- Collision-aware physics
- Head-bob effect for movement feedback

---

## 🎥 Camera System

- Dynamic **FOV control**
- Resolution scaling
- Height projection (Y-axis relative to canvas height)
- Head bobbing synced to movement
- Optimised projection math with rounded precision

---

## 🔊 Sound System

- Responsive footsteps
- Collision-based sound triggers
- Distance-aware volume scaling
- Lightweight audio pooling

---

## 💡 Lighting & Shading

- Shader cache system for brightness maps
- Pixel-based lighting interpolation
- Accuracy rounding for performance
- Floor & sky gradient rendering to contrast world geometry

---

## 🗺️ UI Systems

- **Minimap**
  - Displays world layout
  - Shows active raycasts from player
- **FPS Counter**
  - Live performance monitoring

---

## 🌐 Multiplayer Networking

- UDP-style WebSocket client/server replication
- Character state replication
- Real-time world synchronisation
- Live side-chat for players
- Browser idle timeout & auto-disconnect

### Logging & Events
- Join / leave logging
- Chat logging
- Webhook to Discord Channels

---

## 🧵 Server Architecture

- Each game **world/server runs on its own thread**
- Isolated state per world
- Scalable multi-instance hosting
- Low shared memory overhead

---

## 🔌 REST API

### API Design
- Version-controlled (`/api/v1`)
- Blueprint-based (modular & stackable)
- Resource & sub-resource structure
- JSON request / response format

### Features
- Global TTL caches for fast data serving
- Token-based authentication
- Role-based access control
- Requests denied without valid tokens
- Hidden stack traces on errors
- Sanitised error responses

---

## ⚡ Optimisations

- Shader brightness caches
- Rounded numeric calculations
- FPS-bound update methods
- Adjacent wall removal on map generation
- 16×16 textures with pixel skipping based on LOD
- Max render distance to skip far walls
- Browser idle disconnects to save bandwidth and CPU
- Texture RGB pixel data fetched via API

---

## 🔐 Website Security

Security is implemented at every layer:

- Session tokens stored in secure cookies
- Secure server-side forms
- Cryptographic hashing via Werkzeug
- Google reCAPTCHA protection
- CSRF prevention
- Input sanitisation
- User access levels
- Multi-factor authentication via email (Gmail bot)
- Environment variable loading for sensitive data
- NoSQL storage via MongoDB DQL to eliminate SQL injection vectors

---

## 👤 Account Management

- Register accounts
- Login / Logout
- Edit / Update profiles
- Delete accounts
- Role-based access enforcement

---

## 🎨 Frontend Architecture

- Responsive layouts via Bootstrap
- Layered CSS structure
- Jinja2 layered templating
- Reactive UI updates without full reloads

---

## 🛠️ Configuration

- Sensitive data loaded via environment variables
- API keys and secrets never hardcoded
- Configurable per-environment settings

---

## ✨ Notes

This project demonstrates:

- Advanced browser-based rendering
- Real-time multiplayer networking
- Secure Flask backend design
- Performance-driven engine optimisation
- Clean separation between engine, network, and API layers

A strong foundation for **browser-based multiplayer engines, experiments, or game tech portfolios**.
