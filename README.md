# 🌱 Graph Gardener

A lightweight Python utility designed to help manage and visualize Git contribution history through automated, backdated commits.

## 📌 Overview
This script automates the process of generating a commit history. It allows you to fill in your GitHub contribution graph by creating commits for past dates, using realistic time-stamping (9 AM - 6 PM) and adjustable "intensity" levels to simulate a natural workflow.

## 🚀 Features
* **Backdated Commits:** Specify exactly how many days into the past you want to start.
* **Realistic Timing:** Randomizes commits within standard business hours to avoid "bot-like" 3:00 AM timestamps.
* **Intensity Control:** Choose the probability of commits occurring on any given day.
* **Multiple Commits per Day:** Randomly generates 1–3 commits on active days for a varied heatmap appearance.

## 🛠️ Installation & Usage

1. **Clone your target repository** (or create a new empty one on GitHub and clone it locally).
2. **Place the script** in a directory of your choice.
3. **Run the script:**
   ```bash
   python main.py
