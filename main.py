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

    # Ensure file exists
    if not os.path.exists(filepath):
        open(filepath, "w").close()

    # Modify file
    with open(filepath, "a") as f:
        f.write(f"Contribution update: {date_str}\n")

    # Set fake commit dates
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    # Stage file
    subprocess.run(["git", "add", filename], cwd=repo_path, check=True)

    # Commit only if there are changes
    diff_check = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=repo_path
    )

    if diff_check.returncode != 0:
        subprocess.run(
            ["git", "commit", "-m", "refactor: update data logs"],
            cwd=repo_path,
            env=env,
            check=True
        )


def main():
    print("🌱 Graph-Greener: Professional Edition 🌱\n")

    repo_path = get_input("Repository path", ".")
    if not is_git_repo(repo_path):
        print("❌ Error: Not a Git repository.")
        return

    days_back = int(get_input("How many days back?", "365"))
    intensity = float(get_input("Commit intensity (0.1–1.0)", "0.5"))
    filename = get_input("Filename to modify", "contributions.log")

    start_date = datetime.now() - timedelta(days=days_back)
    total_commits = 0

    for i in range(days_back + 1):
        current_day = start_date + timedelta(days=i)

        if random.random() < intensity:
            commits_today = random.randint(1, 3)

            for _ in range(commits_today):
                commit_time = current_day.replace(
                    hour=random.randint(9, 18),
                    minute=random.randint(0, 59),
                    second=random.randint(0, 59)
                )

                make_commit(commit_time, repo_path, filename)
                total_commits += 1

    print(f"\n✅ Created {total_commits} commits.")

    if input("Push to remote? (y/n): ").lower() == "y":
        subprocess.run(["git", "push"], cwd=repo_path)
        print("🚀 Pushed successfully!")


if __name__ == "__main__":
    main()
