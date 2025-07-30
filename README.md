# 🔒 Spotlight Privacy Filter

A lightweight Python desktop utility that creates a movable spotlight around your mouse cursor, dimming the rest of the screen. Perfect for screen sharing, focused presentations, or maintaining on-screen privacy during demos.

---

## ✨ Features

- 🔆 Spotlight follows your mouse pointer
- 🧠 Minimal and efficient design using `tkinter`
- 🎯 Hotkey toggle: `Ctrl + Alt + S`
- 🛑 Exit via red button or system tray
- 🎈 Cross-platform support (Windows/Linux)

---

## 🛠️ Built With

- `tkinter` – UI framework
- `pystray` – System tray icon
- `keyboard` – Hotkey listener
- `pyautogui` – Mouse position tracking
- `Pillow` – Icon drawing
- `screeninfo` – Multi-monitor support

---

## 📦 Installation

### 1. Clone the repository

git clone https://github.com/gurmeet289/spotlight-privacy-filter.git
cd privacy-spotlight

---

### 2. Install dependencies

It’s recommended to use a virtual environment.

    pip install -r requirements.txt

Or install manually:

    pip install pystray keyboard pillow pyautogui screeninfo

---

## 🚀 Usage:

### Run the script:

    python privacy_spotlight.py

## Controls:

    Toggle spotlight on/off: Ctrl + Alt + S

    Exit: Press Esc, click the red circle, or right-click the system tray icon and select "Exit"

### 📁 File Structure:

    spotlight_privacy/
      │
      ├── spotlight_privacy_filter.py   # Main Python script
      ├── requirements.txt       # Dependency list

## UseCases:

  ### 🧩 Real-Time Use Cases for Privacy Spotlight

      Privacy Spotlight isn’t just a neat visual trick—it solves real-world problems for developers, professionals, educators, and creators. Here are practical use cases where this tool can be genuinely useful:
    
  ---
    
  ### 1. 🎥 Live Presentations & Demos
    
    Scenario: You're presenting your screen during a Zoom or Microsoft Teams meeting and want to keep the audience focused only on the area you're explaining.
    
    Benefit: Keeps attention on what's important and avoids accidental exposure of other tabs, folders, or apps.
    
  ---
    
  ### 2. 🧑‍🏫 Classroom or Online Teaching
    
    Scenario: Teachers using digital whiteboards or walkthroughs want students to follow along with their cursor.
    
    Benefit: Replaces the need for laser pointers or annotations. Helps students follow instructions better during online or hybrid sessions.
    
  ---
    
  ### 3. 📷 Content Recording & Tutorials
    
    Scenario: You're recording a video tutorial or walkthrough for YouTube or internal documentation.
    
    Benefit: The spotlight guides the viewer’s eyes to the correct part of the screen, improving video clarity and user experience—no editing required.
    
  ---
    
  ### 4. 🔐 Working in Public or Shared Spaces
    
    Scenario: You're working at a café, co-working space, or airport and want to reduce what's visible on your laptop screen.
    
    Benefit: Acts as a visual privacy screen. Keeps peeping eyes away from sensitive information and prevents shoulder surfing.
    
  ---
    
  ### 5. 🛡️ Client Screen Sharing with Sensitive Info
    
    Scenario: Consultants or developers working on multiple projects need to screen share with clients without showing unrelated files or messages.
    
    Benefit: Reduces the risk of data leakage and enhances client trust.
    
  ---
    
  ### 6. 🧠 Focus Aid for Neurodivergent Users
    
    Scenario: Users with ADHD or attention challenges find it hard to stay focused with a full screen of content.
    
    Benefit: The spotlight reduces visual noise and helps the user stay focused only on what’s under the cursor.
    
  ---
    
  ### 7. 🧪 Usability Testing & User Research
    
    Scenario: During moderated usability tests, you want to guide user attention subtly without intrusive highlights.
    
    Benefit: Helps guide testers without leading them, improving the quality of user insights.
    
  ---
    
  ### 8. ⚙️ IT Support or Remote Help
    
    Scenario: You're walking a user through steps remotely and want them to look at exactly what you're clicking.
    
    Benefit: No need for arrows or annotations—users visually follow the spotlight around the screen.
    
  ---
    
  ### 9. 🧑‍💼 Privacy Compliance in Regulated Environments
    
    Scenario: You're in banking, insurance, or healthcare and must ensure only certain parts of the screen are visible during demos.
    
    Benefit: Adds a lightweight privacy layer when sharing screens in high-stakes environments.
    
  ---
    
  ### 10. 🛑 Prevent Peeping Over Your Shoulder 
    
    Scenario: You're working on sensitive emails, documents, or code while commuting or in a shared office.
    
    Benefit: The spotlight masks the rest of the screen, making it difficult for nearby people to casually view or read your content.
    
  ---
    
  ## Summary
    
    Whether you’re teaching, presenting, protecting sensitive data, or just staying focused, **Spotlight Privacy Filter** is a lightweight tool that gives you control over what stays visible on your screen.
    
  ##Laptop/Desktop Utilty;

  You can download the utility(.exe) file into you local space and execute it by double click on it.
