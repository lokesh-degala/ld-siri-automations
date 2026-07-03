# GitHub Panchang + Siri Setup Checklist

## ✅ Pre-Setup
- [ ] Have a GitHub account (free at https://github.com)
- [ ] iPhone with Shortcuts app installed
- [ ] 15 minutes of free time

---

## 📦 Step 1: Create GitHub Repository (2 min)

- [ ] Go to https://github.com/new
- [ ] Name repo: `panchang-data`
- [ ] Select **"Public"** (important!)
- [ ] Click **"Create repository"**
- [ ] Copy your repo URL for reference

---

## 📄 Step 2: Add Files to Repo (3 min)

### File 1: `fetch_panchang.py`
- [ ] Click "Add file" → "Create new file"
- [ ] Filename: `fetch_panchang.py`
- [ ] Copy content from the file I provided
- [ ] Click "Commit changes"

### File 2: `.github/workflows/fetch-panchang.yml`
- [ ] Click "Add file" → "Create new file"
- [ ] Filename: `.github/workflows/fetch-panchang.yml`
- [ ] Copy content from the workflow file
- [ ] Click "Commit changes"

### File 3: `requirements.txt`
- [ ] Click "Add file" → "Create new file"
- [ ] Filename: `requirements.txt`
- [ ] Paste:
  ```
  requests==2.31.0
  beautifulsoup4==4.12.0
  ```
- [ ] Click "Commit changes"

---

## ⚙️ Step 3: Run GitHub Actions (2 min)

- [ ] Go to **"Actions"** tab in your repo
- [ ] Click **"Fetch Panchang Data Daily"** workflow
- [ ] Click **"Run workflow"** (blue button)
- [ ] Select **"Run workflow"** in dropdown
- [ ] Wait 30 seconds
- [ ] Refresh the page

---

## ✔️ Step 4: Verify Files Created (1 min)

- [ ] Go to **"Code"** tab
- [ ] Check for `panchang.json` file ✓
- [ ] Check for `panchang_voice.json` file ✓

---

## 🔗 Step 5: Get Raw URL (1 min)

- [ ] Click on `panchang_voice.json`
- [ ] Click **"Raw"** button (top right)
- [ ] Copy the URL from browser address bar
- [ ] **Save this URL!** You'll need it for Siri

Example format:
```
https://raw.githubusercontent.com/YOUR-USERNAME/panchang-data/main/panchang_voice.json
```

---

## 📱 Step 6: Create Siri Shortcut (3 min)

**On iPhone:**

- [ ] Open **Shortcuts** app
- [ ] Tap **"+"** (new shortcut)
- [ ] Tap **"Add Action"**
- [ ] Search for: `Get Contents of URL`
- [ ] Paste your JSON URL (from Step 5)
- [ ] Tap **"Add Action"**
- [ ] Search for: `Get Dictionary Value`
- [ ] Set Key: `voice_text`
- [ ] Tap **"Add Action"**
- [ ] Search for: `Speak Text`
- [ ] (Text should auto-populate)

---

## 🎤 Step 7: Add to Siri (2 min)

- [ ] Tap **three dots** (top right)
- [ ] Tap **"Details"**
- [ ] Name: `Panchang`
- [ ] Toggle **"Show in Siri Suggestions"** ON
- [ ] Tap **"Add to Siri"**
- [ ] Record voice command: **"Tell me today's panchang"**
- [ ] Tap **"Done"**

---

## 🎉 Step 8: Test It! (30 sec)

- [ ] Say: **"Hey Siri, tell me today's panchang"**
- [ ] iPhone should speak panchang data
- [ ] If works: You're done! 🎉
- [ ] If not: See troubleshooting below

---

## 🐛 Troubleshooting

### Workflow Won't Run
- [ ] Go to Actions tab
- [ ] Check if workflow has green checkmark
- [ ] If red X: Click it to see error logs
- [ ] Most common: Syntax error in YAML file
- [ ] **Fix:** Manually re-create the workflow file carefully

### JSON Files Don't Appear
- [ ] Click "Run workflow" again manually
- [ ] Wait 1-2 minutes
- [ ] Refresh page
- [ ] Check Actions tab for errors

### URL Returns 404 in Siri Shortcut
- [ ] Test URL in Safari browser
- [ ] If 404: Check repo is **Public** (not Private)
- [ ] Check filename spelling exactly
- [ ] Check GitHub username in URL is correct
- [ ] **Fix:** Update shortcut with correct URL

### Siri Says "Can't Connect"
- [ ] Make sure iPhone is on WiFi or cellular
- [ ] Test URL in Safari first
- [ ] Wait 5 seconds and try again
- [ ] Restart Shortcuts app and retry

### No Data in JSON
- [ ] Check GitHub Actions logs
- [ ] Website drikpanchang.com might be down
- [ ] Run workflow again manually

---

## ✨ What You Get

✅ Automatic daily panchang fetch (no manual work)
✅ Always free (GitHub free tier)
✅ Works instantly (cached data)
✅ Works offline (data stored locally on iPhone)
✅ Voice control via Siri
✅ Can share with family (give them the JSON URL)

---

## Cost: $0 Forever

| Item | Cost |
|------|------|
| GitHub public repo | Free |
| GitHub Actions (2000 min/month, uses ~30) | Free |
| Siri Shortcuts | Free |
| **Total** | **$0** |

---

## Pro Tips

💡 **Create more shortcuts:**
- "What's today's Tithi?" → Use `/panchang.json` with Key: `data` → `Tithi`
- "When is sunrise?" → Key: `data` → `Sunrise`
- "Show all panchang" → Show entire JSON result

💡 **Share with family:**
- Give them your raw JSON URL
- They create the same Siri shortcut
- Everyone gets same data!

💡 **Change fetch time:**
- Edit `.github/workflows/fetch-panchang.yml`
- Change `cron: '30 0 * * *'` to different time
- Current: 6 AM IST (adjust if needed)

---

## Timeline

| Step | Time | Status |
|------|------|--------|
| Create repo | 2 min | ⏱️ |
| Add files | 3 min | ⏱️ |
| Run workflow | 2 min | ⏱️ |
| Create shortcut | 3 min | ⏱️ |
| Add to Siri | 2 min | ⏱️ |
| Test | 1 min | ⏱️ |
| **Total** | **13 min** | ✅ |

---

## Next Steps

1. ✅ Start with Step 1 (Create repo)
2. ✅ Follow each step in order
3. ✅ Test at Step 8
4. ✅ Enjoy automated panchang data!

**Questions?** Check GITHUB_SIRI_SETUP.md for detailed help.
