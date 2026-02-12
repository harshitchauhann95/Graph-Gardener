# 🌿 Graph-Gardner Pro

### 🌟 Make Your GitHub Contribution Graph Vibrant and Active! 🌟

A lightweight Python utility designed to help manage and visualize Git contribution history through automated, backdated commits.

---

## ⚖️ Ethical Use & Disclaimer
**Important: Read Before Use**

> ⚠️ **This tool is a "contribution hack" intended for aesthetic visualization and educational purposes only.**  
> * **Be Honest:** This does not represent real coding work or skill. Do not use this to deceive potential employers or clients.  
> * **Be Responsible:** Overusing this script can clutter GitHub's global activity data.  
> * **Privacy First:** We strongly recommend using this only on **Private Repositories** so it doesn't interfere with your public project history.  

Use this tool ethically to improve the look of your personal profile, but let your real code speak for your talent!

---

## 📌 Overview
This script automates the process of generating a commit history. It allows you to fill in your GitHub contribution graph by creating commits for past dates, using realistic time-stamping (9 AM - 6 PM) and adjustable "intensity" levels to simulate a natural workflow.

---

## 🚀 Features

- **Backdated Commits:** Specify exactly how many days into the past you want to start.  
- **Realistic Timing:** Randomizes commits within standard business hours (9 AM - 6 PM) to avoid "bot-like" 3:00 AM timestamps.  
- **Intensity Control:** Choose the probability (0.1 to 1.0) of commits occurring on any given day.  
- **Natural Variety:** Randomly generates 1–3 commits on active days for a varied, organic-looking heatmap.  
- **Safe Commit Checks:** Only commits when changes exist to avoid unnecessary empty commits.  
- **Optional Push:** Ask before pushing all commits to the remote repository.

---

## 🛠️ Installation & Usage

1. **Clone your target repository** (or create a new empty one on GitHub and clone it locally).  
2. **Place the script** (`main.py`) in your repository folder.  
3. **Run the script:** python main.py
4.	Follow prompts:
	•	Repository path (default: current folder .)
	•	Days back (default: 365)
	•	Commit intensity (0.1 – 1.0, default: 0.5)
	•	Filename to modify (default: contributions.log)
5.	Push to remote (optional) after commits are created

## ⚠️ Recommended Best Practices

- Use **private repositories** to avoid interfering with public project history.  
- Do **not overuse** the script; keep intensity moderate.  
- Remember, this is **for aesthetic purposes only**, not for resume or job deception.  

## 💡 Suggestions for Improvement

- Add **branch-specific commit safety**.  
- Wrap git commands in **try/except** for safer execution.  
- Create a **real analytics version** that visualizes contribution history without faking commits.  

## 📄 License

This project is **open-source** and free to use for educational purposes. Use responsibly.
