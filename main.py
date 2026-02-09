import os
import random
import subprocess
from datetime import datetime, timedelta

def is_git_repo(path):
    return os.path.isdir(os.path.join(path, ".git"))

def get_input(prompt, default):
    user_input = input(f"{prompt} (default {default}): ").strip()
    return user_input if user_input else default

def make_commit(date, repo_path, filename):
    filepath = os.path.join(repo_path, filename)
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    
    # Update the file
    with open(filepath, "a") as f:
        f.write(f"Contribution update: {date_str}\n")
    
    # Stage and Commit with backdated environment variables
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    
    subprocess.run(["git", "add", filename], cwd=repo_path, capture_output=True)
    subprocess.run(["git", "commit", "-m", "refactor: update data logs"], cwd=repo_path, env=env, capture_output=True)

def main():
    print("🌱 Graph-Greener: Professional Edition 🌱\n")

    repo_path = get_input("Repository path", ".")
    if not is_git_repo(repo_path):
        print("❌ Error: That directory isn't a Git repository.")
        return

    days_back = int(get_input("How many days back should we start?", "365"))
    intensity = float(get_input("Commit intensity (0.1 to 1.0)", "0.5"))
    filename = get_input("Filename to modify", "contributions.log")

    start_date = datetime.now() - timedelta(days=days_back)
    total_commits = 0

    print(f"\n🚀 Generating history for the last {days_back} days...")

    for i in range(days_back + 1):
        current_day = start_date + timedelta(days=i)
        
        # This creates a more natural "patchy" look
        if random.random() < intensity:
            # Randomize number of commits per day (1 to 3)
            for _ in range(random.randint(1, 3)):
                # Randomize time of day
                commit_time = current_day.replace(
                    hour=random.randint(9, 18), 
                    minute=random.randint(0, 59)
                )
                make_commit(commit_time, repo_path, filename)
                total_commits += 1

    print(f"✅ Created {total_commits} commits.")
    
    push = input("Push to remote now? (y/n): ").lower()
    if push == 'y':
        subprocess.run(["git", "push"], cwd=repo_path)
        print("Done! Check your profile shortly.")

if __name__ == "__main__":
    main()