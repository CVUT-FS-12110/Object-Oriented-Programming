# Git & GitHub — Intro Course

> **Format:** Live demo + hands-on. Every command is run together. Ask questions any time.

---

## Part 1 — Local Git

### 1. `git init` — Start a repository

```bash
mkdir my-project
cd my-project
git init
```

- Creates a hidden `.git/` folder — this is where Git stores everything
- The working directory is now a **repository**

> 💡 You only run `git init` once per project

---

### 2. `git status` — What's going on right now?

```bash
git status
```

- Shows which files are **untracked**, **modified**, or **staged**
- Run this constantly — it's your compass

Create a file and check status:

```bash
echo "# My Project" > README.md
git status
# → README.md appears as "untracked"
```

---

### 3. `git add` — Stage changes

```bash
git add README.md        # stage one file
git add .               # stage everything in current directory
```

- Staging = telling Git "include this in the next snapshot"
- Nothing is saved permanently yet

```bash
git status
# → README.md is now "Changes to be committed"
```

> 💡 Think of staging as packing a box before you seal and ship it

---

### 4. `git commit` — Save a snapshot

```bash
git commit -m "Initial commit: add README"
```

- Creates a permanent snapshot with a message
- Every commit gets a unique ID (SHA hash)
- Good commit messages: short, imperative ("Add feature", not "Added feature")

```bash
git status
# → "nothing to commit, working tree clean"
```

---

### 5. `git log` — Browse history

```bash
git log               # full log
git log --oneline     # compact view (recommended)
```

- Shows all commits: author, date, message, hash
- `q` to exit the log viewer

Make another commit to see history grow:

```bash
echo "Some content" >> README.md
git add .
git commit -m "Add content to README"
git log --oneline
```

---

### 6. `git merge` — Combine branches (no conflict)

First, understand branches:

```bash
git branch             # list branches
git branch feature     # create a branch called "feature"
git switch feature     # switch to it
```

Make a change on the feature branch:

```bash
echo "New feature" > feature.txt
git add .
git commit -m "Add feature.txt"
```

Merge back to main:

```bash
git switch main
git merge feature
git log --oneline
```

- Git combines the histories automatically (fast-forward merge)
- The feature branch still exists — delete it if done: `git branch -d feature`

> 💡 `main` is just a branch — the default one

---

## Part 2 — Remote Git (GitHub)

### 7. `git remote add` — Connect to GitHub

After creating a new repo on GitHub (empty, no README):

```bash
git remote add origin https://github.com/yourname/my-project.git
git remote -v         # verify the connection
```

- `origin` is just an alias for the remote URL — it's the convention
- You can have multiple remotes

---

### 8. `git push` — Send to GitHub

```bash
git push -u origin main
```

- `-u` sets the upstream (only needed the first time)
- After that, just `git push`

Refresh GitHub — your files are there. ✅

---

## Part 3 — GitHub Workflow

> Now we switch to the GitHub UI

### Step 1: Create an Issue

1. Go to your repo → **Issues** tab → **New issue**
2. Title: `Fix typo in README`
3. Add a comment describing the problem (e.g., "The word 'recieve' should be 'receive'")
4. Submit the issue — it gets a number, e.g. `#1`

> Issues track bugs, ideas, and tasks. Comments = discussion thread.

---

### Step 2: Create a Branch for the Issue

On GitHub, from the issue page:
- Click **"Create a branch"** → names it something like `1-fix-typo-in-readme`

Or locally:

```bash
git fetch origin
git switch -c fix/typo-in-readme
```

Make the fix:

```bash
# Fix the typo in README.md (edit it)
git add README.md
git commit -m "Fix typo: recieve → receive (closes #1)"
git push origin fix/typo-in-readme
```

> 💡 Writing `closes #1` in the commit message will auto-close the issue when merged

---

### Step 3: Open a Pull Request (PR)

On GitHub:
1. You'll see a **"Compare & pull request"** banner — click it
2. Add a title and description
3. Assign reviewers if needed
4. Submit the PR

The PR shows: what changed, diff, commit history, linked issue.

---

### Step 4: Code Review

Reviewers can:
- **Comment** on specific lines
- **Request changes** — author must update the branch
- **Approve** — signals it's ready to merge

```bash
# If changes are requested, just push more commits to the same branch
git add .
git commit -m "Address review feedback"
git push
```

The PR updates automatically.

---

### Step 5: Merge the PR

Once approved:
1. Click **"Merge pull request"** on GitHub
2. Choose merge strategy (usually **"Create a merge commit"** or **"Squash and merge"**)
3. Delete the branch (GitHub offers this after merge)

Pull the merged result locally:

```bash
git switch main
git pull
```

---

### ⚡ Merge Conflict

Conflicts happen when two branches change the **same line** of the same file.

**Simulate it:**

```bash
# On main
echo "Hello from main" > hello.txt
git add . && git commit -m "Add hello.txt on main"

# On a feature branch (from earlier point)
git switch -c conflict-demo main~1
echo "Hello from feature" > hello.txt
git add . && git commit -m "Add hello.txt on feature"

# Merge → conflict!
git switch main
git merge conflict-demo
```

Git marks the conflict in the file:

```
<<<<<<< HEAD
Hello from main
=======
Hello from feature
>>>>>>> conflict-demo
```

**Resolve it:**
1. Edit the file — keep what you want, remove the markers
2. `git add hello.txt`
3. `git commit -m "Resolve merge conflict in hello.txt"`

> On GitHub, conflicts in a PR can be resolved directly in the browser via **"Resolve conflicts"**

---

## Quick Reference

| Command | What it does |
|---|---|
| `git init` | Start a new repo |
| `git status` | Show current state |
| `git add <file>` | Stage a file |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Save a snapshot |
| `git log --oneline` | Compact history |
| `git branch <name>` | Create a branch |
| `git switch <name>` | Switch branch |
| `git merge <branch>` | Merge into current |
| `git remote add origin <url>` | Connect to remote |
| `git push -u origin main` | Push (first time) |
| `git push` | Push (subsequent) |
| `git pull` | Fetch + merge from remote |
| `git fetch` | Fetch without merging |

---

## GitHub Workflow Summary

```
Issue → Branch → Commits → Push → PR → Review → Merge
```

---

*Git version: 2.x+ recommended. GitHub account required for Part 3.*
