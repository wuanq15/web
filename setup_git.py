import subprocess
import os

repo_dir = "/Users/phambaquang/Downloads/flower_shop_6889464"
os.chdir(repo_dir)

def run(cmd, check=True):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=check)

with open("index.html", "r") as f:
    original_lines = f.readlines()

def get_base_lines():
    return original_lines.copy()

# Initialize Git
run("git init")
# remove any existing remote origin if it exists
subprocess.run("git remote remove origin", shell=True, stderr=subprocess.DEVNULL)
run("git remote add origin https://github.com/wuanq15/web.git")
run("git add .")
# Initial commit
subprocess.run("git commit -m 'Initial commit'", shell=True)

try:
    run("git branch A")
    run("git branch B")
except:
    pass

# --- BRANCH A ---
run("git checkout -f A")
# reset to the exact initial commit to be safe, just in case branch A already existed
run("git reset --hard main", check=False) 
run("git reset --hard master", check=False)
subprocess.run("git reset --hard $(git branch --show-current)", shell=True)
# The above ensures we start clean, though newly created branch will be at current HEAD

lines = get_base_lines()

# A1: Modify footer (5 lines)
for i in range(120, 125):
    lines[i] = f"<!-- Branch A: Update footer line {i} -->\n" + lines[i]
with open("index.html", "w") as f: f.writelines(lines)
run("git commit -am 'Commit 1 on Branch A: Update footer'")

# A2: Conflict 1 target (5 lines)
for i in range(12, 17):
    lines[i] = f"<!-- Branch A: Conflict 1 at line {i} -->\n" + lines[i]
with open("index.html", "w") as f: f.writelines(lines)
run("git commit -am 'Commit 2 on Branch A: Conflict 1 prep'")

# A3: Header mod (5 lines)
for i in range(25, 30):
    lines[i] = f"<!-- Branch A: Header mod {i} -->\n" + lines[i]
with open("index.html", "w") as f: f.writelines(lines)
run("git commit -am 'Commit 3 on Branch A: Header mod'")

# A4: Conflict 2 target (5 lines)
for i in range(46, 51):
    lines[i] = f"<!-- Branch A: Conflict 2 at line {i} -->\n" + lines[i]
with open("index.html", "w") as f: f.writelines(lines)
run("git commit -am 'Commit 4 on Branch A: Conflict 2 prep'")

# A5: Footer mod 2 (5 lines)
for i in range(112, 117):
    lines[i] = f"<!-- Branch A: Footer mod 2 line {i} -->\n" + lines[i]
with open("index.html", "w") as f: f.writelines(lines)
run("git commit -am 'Commit 5 on Branch A: Footer mod 2'")


# --- BRANCH B ---
run("git checkout -f B")
# Return lines to original state for B
lines = get_base_lines()
with open("index.html", "w") as f: f.writelines(lines)
run("git reset --hard", check=False) # make sure working tree is clean to match original baseline
# Try to reset B to the initial commit, whether it is main or master
subprocess.run("git reset --hard main || git reset --hard master", shell=True)

lines = get_base_lines()

# B1: Modify top of file (5 lines)
for i in range(5, 10):
    lines[i] = f"<!-- Branch B: Top mod {i} -->\n" + lines[i]
with open("index.html", "w") as f: f.writelines(lines)
run("git commit -am 'Commit 1 on Branch B: Top mod'")

# B2: Conflict 1 target (5 lines) -> CONFLICT WITH A2
for i in range(12, 17):
    lines[i] = f"<!-- Branch B: Conflict 1 at line {i} -->\n" + lines[i]
with open("index.html", "w") as f: f.writelines(lines)
run("git commit -am 'Commit 2 on Branch B: Conflict 1 prep'")

# B3: Banner mod (5 lines)
for i in range(32, 37):
    lines[i] = f"<!-- Branch B: Banner mod {i} -->\n" + lines[i]
with open("index.html", "w") as f: f.writelines(lines)
run("git commit -am 'Commit 3 on Branch B: Banner mod'")

# B4: Conflict 2 target (5 lines) -> CONFLICT WITH A4
for i in range(46, 51):
    lines[i] = f"<!-- Branch B: Conflict 2 at line {i} -->\n" + lines[i]
with open("index.html", "w") as f: f.writelines(lines)
run("git commit -am 'Commit 4 on Branch B: Conflict 2 prep'")

# B5: Right section mod (5 lines)
for i in range(80, 85):
    lines[i] = f"<!-- Branch B: Right section mod {i} -->\n" + lines[i]
with open("index.html", "w") as f: f.writelines(lines)
run("git commit -am 'Commit 5 on Branch B: Right section mod'")

# attempt to push branches, if it fails because of authentication, print a message
print("Attempting to push to remote...")
try:
    subprocess.run("git push -u origin A", shell=True, check=True)
    subprocess.run("git push -u origin B", shell=True, check=True)
    print("Successfully pushed to remote.")
except subprocess.CalledProcessError:
    print("Could not push to remote automatically (likely needs credentials).")
