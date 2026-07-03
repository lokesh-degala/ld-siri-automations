# Monorepo Setup Checklist - ld-siri-automations

## ✅ Pre-Setup
- [ ] Existing repo: `/d/LOKESH/Workspace/Repos/ld-siri-automations`
- [ ] Local `panchang/` folder exists
- [ ] Repo is on GitHub (public)
- [ ] Git is configured locally

---

## 📄 Step 1: Add Files Locally (5 min)

### Add `panchang/fetch_panchang.py`
- [ ] Copy `fetch_panchang.py` to `panchang/` folder
- [ ] File path: `ld-siri-automations/panchang/fetch_panchang.py`
- [ ] Verify it exists: `ls panchang/fetch_panchang.py`

### Add `requirements.txt` to Root
- [ ] Create `requirements.txt` in repo root
- [ ] Content:
  ```
  requests==2.31.0
  beautifulsoup4==4.12.0
  ```
- [ ] Verify: `ls requirements.txt`

### Add `.github/workflows/fetch-panchang.yml`
- [ ] Create directory: `mkdir -p .github/workflows`
- [ ] Create file: `.github/workflows/fetch-panchang.yml`
- [ ] Paste workflow content (monorepo version)
- [ ] Verify: `ls .github/workflows/fetch-panchang.yml`

---

## 🔧 Step 2: Commit & Push (3 min)

```bash
# From repo root
git status
git add panchang/fetch_panchang.py
git add requirements.txt
git add .github/workflows/fetch-panchang.yml
git commit -m "Add panchang automation"
git push origin main
```

- [ ] `git add` successful
- [ ] `git commit` successful
- [ ] `git push` successful
- [ ] No errors in terminal

---

## 🌐 Step 3: Verify on GitHub (2 min)

1. Go to your repo on GitHub: `https://github.com/YOUR-USERNAME/ld-siri-automations`
2. Check these files exist:
   - [ ] `panchang/fetch_panchang.py` (visible in Code tab)
   - [ ] `requirements.txt` (visible in Code tab)
   - [ ] `.github/workflows/fetch-panchang.yml` (visible in Actions tab)

---

## ▶️ Step 4: Run Workflow Manually (2 min)

1. Go to **"Actions"** tab on GitHub
2. Click **"Fetch Panchang Data Daily"** workflow
3. Click **"Run workflow"** (blue button)
4. Select **main** branch
5. Click **"Run workflow"**
6. Wait 30-60 seconds
7. Refresh page

- [ ] Workflow started
- [ ] Workflow completed successfully (green checkmark)

---

## ✔️ Step 5: Verify JSON Files Created (1 min)

1. Go to **"Code"** tab
2. Open **`panchang/`** folder
3. Check these files exist:
   - [ ] `panchang.json` (should show data)
   - [ ] `panchang_voice.json` (should show data)

---

## 🔗 Step 6: Get Raw URL (1 min)

1. Click on `panchang/panchang_voice.json`
2. Click **"Raw"** button (top right)
3. Copy URL from browser address bar
4. Format: `https://raw.githubusercontent.com/YOUR-USERNAME/ld-siri-automations/main/panchang/panchang_voice.json`

- [ ] URL copied
- [ ] URL saved for next step

---

## 📱 Step 7: Create Siri Shortcut (3 min)

**On iPhone:**

- [ ] Open **Shortcuts** app
- [ ] Tap **"+"** (new shortcut)
- [ ] Add action: **Get Contents of URL**
  - [ ] Paste your raw GitHub URL
- [ ] Add action: **Get Dictionary Value**
  - [ ] Key: `voice_text`
- [ ] Add action: **Speak Text**
  - [ ] (Auto-populated)

---

## 🎤 Step 8: Add to Siri (2 min)

- [ ] Tap **three dots** (top right)
- [ ] Tap **"Details"**
- [ ] Name: `Panchang`
- [ ] Toggle **"Show in Siri Suggestions"** ON
- [ ] Tap **"Add to Siri"**
- [ ] Record voice command: **"Tell me today's panchang"**
- [ ] Tap **"Done"**

---

## 🎉 Step 9: Test (30 sec)

- [ ] Say: **"Hey Siri, tell me today's panchang"**
- [ ] iPhone should speak panchang data
- [ ] If works: ✅ You're done!

---

## 📊 Timeline

| Step | Time | Status |
|------|------|--------|
| Add files locally | 5 min | ⏱️ |
| Commit & push | 3 min | ⏱️ |
| Verify on GitHub | 2 min | ⏱️ |
| Run workflow | 2 min | ⏱️ |
| Verify JSON files | 1 min | ⏱️ |
| Get raw URL | 1 min | ⏱️ |
| Create shortcut | 3 min | ⏱️ |
| Add to Siri | 2 min | ⏱️ |
| Test | 1 min | ⏱️ |
| **TOTAL** | **20 min** | ✅ |

---

## 🛠️ File Locations Reference

| File | Location | Purpose |
|------|----------|---------|
| `fetch_panchang.py` | `panchang/fetch_panchang.py` | Fetch script |
| `requirements.txt` | `requirements.txt` (root) | Python dependencies |
| `fetch-panchang.yml` | `.github/workflows/fetch-panchang.yml` | GitHub Actions workflow |
| `panchang.json` | `panchang/panchang.json` | Auto-generated daily |
| `panchang_voice.json` | `panchang/panchang_voice.json` | Auto-generated daily |

---

## 🐛 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Workflow won't start | Check `.github/workflows/fetch-panchang.yml` syntax |
| JSON files not created | Check Actions tab for error logs |
| Siri says 404 | Make sure repo is **PUBLIC** |
| No data in JSON | drikpanchang.com might be down, retry later |
| Git push fails | Make sure you're on `main` branch (`git status`) |

---

## ✨ After This Works

You can add more automations to the same repo:

```
ld-siri-automations/
├── panchang/          ✅ Done
├── weather/           (future)
├── news/              (future)
├── stocks/            (future)
└── .github/workflows/ (add more workflows here)
```

Each follows the same pattern!

---

## 🎯 You're All Set!

Follow the checklist in order and you should be done in ~20 minutes.

If stuck anywhere, check **MONOREPO_SETUP.md** for detailed explanations.

Good luck! 🚀
