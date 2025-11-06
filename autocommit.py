import os
import subprocess
from datetime import datetime

# --- SETTINGS ---
REPO_PATH = r"C:\Users\Ezatullah Farazi\Documents\Codewars_solutions"
BRANCH = "main"
LOG_FILE = os.path.join(REPO_PATH, "auto_commit_log.txt")
# ----------------

def log(message: str):
    """Write a timestamped message to the log file."""
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {message}\n")

def run_command(command: list) -> subprocess.CompletedProcess:
    """Run a shell command and return its result."""
    return subprocess.run(command, capture_output=True, text=True)

def main():
    os.chdir(REPO_PATH)

    # Get the current git status (porcelain format = easy to parse)
    result = run_command(["git", "status", "--porcelain"])
    lines = result.stdout.strip().splitlines()

    if not lines:
        log("No changes found.")
        return

    for line in lines:
        status, filename = line[:2].strip(), line[3:].strip()

        # Only handle .py files, ignore others just in case
        if not filename.endswith(".py"):
            continue

        # Determine message based on status type
        if status == "??":
            action = "Add"
        elif status == "M":
            action = "Update"
        else:
            continue

        # Stage, commit, push
        run_command(["git", "add", filename])
        commit_msg = f"{action}: {os.path.basename(filename)}"
        commit_result = run_command(["git", "commit", "-m", commit_msg])

        if "nothing to commit" in commit_result.stdout.lower():
            log(f"Skipped: {filename} (no changes).")
            continue

        push_result = run_command(["git", "push", "origin", BRANCH])

        if push_result.returncode == 0:
            log(f"{action}: {filename} ✅ pushed successfully.")
        else:
            log(f"{action}: {filename} ❌ push failed.\n{push_result.stderr}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log(f"Error: {e}")
