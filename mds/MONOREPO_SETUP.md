# Panchang Automation - Monorepo Setup

## Your Structure

```
ld-siri-automations/          (main repo)
├── .github/
│   └── workflows/
│       └── fetch-panchang.yml    (NEW - GitHub Actions)
├── panchang/                      (subdirectory)
│   ├── fetch_panchang.py          (NEW - fetch script)
│   ├── panchang.json              (AUTO - generated daily)
│   ├── panchang_voice.json        (AUTO - generated daily)
│   └── README.md                  (optional)
├── requirements.txt               (NEW - dependencies)
└── .gitignore                     (update to ignore node_modules if needed)
```

---

## Step-by-Step Setup

### **Step 1: Clone/Open Your Repo**

You already have it locally:
```bash
cd /d/LOKESH/Workspace/Repos/ld-siri-automations
```

### **Step 2: Add `fetch_panchang.py` to `panchang/` Directory**

**Option A: Copy the file**
- Copy `fetch_panchang.py` (the modified version with subdirectory support)
- Paste it into `panchang/` folder
- File location: `ld-siri-automations/panchang/fetch_panchang.py`

**Option B: Create it manually**
```bash
# From repo root
nano panchang/fetch_panchang.py
# Paste the content from fetch_panchang.py file I created
# Save (Ctrl+X, then Y, then Enter)
```

### **Step 3: Add `requirements.txt` to Repo Root**

**Location:** `ld-siri-automations/requirements.txt`

**Content:**
```
requests==2.31.0
beautifulsoup4==4.12.0
```

### **Step 4: Create GitHub Actions Workflow**

**Create directory structure:**
```bash
mkdir -p .github/workflows
```

**Create file:** `.github/workflows/fetch-panchang.yml`

**Location:** `ld-siri-automations/.github/workflows/fetch-panchang.yml`

**Content:** Copy from the workflow file I provided (`.github_workflows_panchang_monorepo.yml`)

### **Step 5: Push to GitHub**

```bash
# From repo root
git add panchang/fetch_panchang.py
git add requirements.txt
git add .github/workflows/fetch-panchang.yml
git commit -m "Add panchang automation"
git push origin main
```

### **Step 6: Test GitHub Actions**

1. Go to your GitHub repo online
2. Click **"Actions"** tab
3. Click **"Fetch Panchang Data Daily"** workflow
4. Click **"Run workflow"** (blue button)
5. Select main branch
6. Click **"Run workflow"**
7. Wait 30 seconds, then refresh

### **Step 7: Verify JSON Files**

1. Go to **"Code"** tab
2. Navigate to `panchang/` folder
3. You should see:
   - `panchang.json` ✓
   - `panchang_voice.json` ✓

### **Step 8: Get Raw URL for Siri**

1. Click on `panchang/panchang_voice.json`
2. Click **"Raw"** button (top right)
3. Copy the URL from address bar

**Format:**
```
https://raw.githubusercontent.com/YOUR-USERNAME/ld-siri-automations/main/panchang/panchang_voice.json
```

**Example:**
```
https://raw.githubusercontent.com/lokesh/ld-siri-automations/main/panchang/panchang_voice.json
```

### **Step 9: Create Siri Shortcut**

**On iPhone:**

1. Open **Shortcuts** app
2. Tap **"+"** (new shortcut)
3. Tap **"Add Action"**
4. Search: **"Get Contents of URL"**
5. Paste your JSON URL (from Step 8)
6. Tap **"Add Action"**
7. Search: **"Get Dictionary Value"**
8. Set Key: `voice_text`
9. Tap **"Add Action"**
10. Search: **"Speak Text"**

### **Step 10: Add to Siri**

1. Tap **three dots** (top right)
2. Tap **"Details"**
3. Name: `Panchang`
4. Toggle **"Show in Siri Suggestions"** ON
5. Tap **"Add to Siri"**
6. Record: **"Tell me today's panchang"**
7. Tap **"Done"**

### **Step 11: Test**

Say: **"Hey Siri, tell me today's panchang"**

Done! 🎉

---

## Local Testing (Optional)

You can test the fetch script locally:

```bash
# From repo root
cd panchang
python fetch_panchang.py
cd ..
```

Then check:
```bash
cat panchang/panchang_voice.json
```

---

## Directory Structure After Setup

```
ld-siri-automations/
├── .github/
│   └── workflows/
│       └── fetch-panchang.yml
├── panchang/
│   ├── fetch_panchang.py
│   ├── panchang.json
│   ├── panchang_voice.json
│   └── README.md (optional)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Files to Add/Modify

| File | Action | Location |
|------|--------|----------|
| `fetch_panchang.py` | Create | `panchang/fetch_panchang.py` |
| `requirements.txt` | Create | `requirements.txt` (root) |
| `fetch-panchang.yml` | Create | `.github/workflows/fetch-panchang.yml` |
| `panchang.json` | Auto-generated | `panchang/panchang.json` |
| `panchang_voice.json` | Auto-generated | `panchang/panchang_voice.json` |

---

## Important Notes

⚠️ **Keep repo public** (for Siri to access JSON without auth token)

⚠️ **Workflow runs at 6 AM IST** (adjust in `.yml` if needed)

⚠️ **Files auto-generated** (don't manually create `panchang.json`)

---

## Advantages of Monorepo

✅ One repo for all Siri automations
✅ Easy to add more automations later (e.g., `weather/`, `news/`)
✅ Central place to manage workflows
✅ Simple to share with family (one GitHub URL)
✅ Organized structure

---

## Future: Add More Automations

Once this works, you can add more to the same repo:

```
ld-siri-automations/
├── panchang/
│   ├── fetch_panchang.py
│   ├── panchang.json
│   └── panchang_voice.json
├── weather/              (future)
│   ├── fetch_weather.py
│   └── weather.json
├── news/                 (future)
│   ├── fetch_news.py
│   └── news.json
├── .github/workflows/
│   ├── fetch-panchang.yml
│   ├── fetch-weather.yml (future)
│   └── fetch-news.yml    (future)
└── requirements.txt
```

Each automation can have its own:
- Fetch script
- JSON output
- GitHub Actions workflow
- Siri shortcut

---

## Git Commands Reference

```bash
# Check status
git status

# Add files
git add panchang/fetch_panchang.py
git add requirements.txt
git add .github/workflows/fetch-panchang.yml

# Commit
git commit -m "Add panchang automation"

# Push
git push origin main

# Check logs
git log --oneline
```

---

## Troubleshooting

### Workflow Not Running
- Check `.github/workflows/fetch-panchang.yml` syntax (YAML is strict)
- Make sure file path is exactly: `.github/workflows/fetch-panchang.yml`
- Run manually from Actions tab to debug

### JSON Files Not Generated
- Check Actions tab for error logs
- Look for Python or network errors
- Manually trigger workflow again

### Siri URL Doesn't Work
- Test URL in Safari first
- Make sure repo is **public**
- Check username in URL is correct
- Check path includes `panchang/` folder

---

## Cost

| Item | Cost |
|------|------|
| GitHub (public repo) | $0 |
| GitHub Actions | $0 (free tier covers this) |
| Siri | $0 |
| **Total** | **$0** |

---

## Next Steps

1. Add `fetch_panchang.py` to `panchang/` folder
2. Add `requirements.txt` to root
3. Create `.github/workflows/fetch-panchang.yml`
4. Push to GitHub
5. Test workflow manually
6. Create Siri shortcut
7. Done! 🎉

---

## File Contents Quick Reference

**`panchang/fetch_panchang.py`** - Uses modified version that saves to `panchang/` subdirectory
**`requirements.txt`** - Same as before
**`.github/workflows/fetch-panchang.yml`** - Updated to work with monorepo structure

All files are in the outputs folder!
