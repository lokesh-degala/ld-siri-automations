# GitHub + Siri: Panchang Data Automation (Zero Cost Forever!)

## Overview

This setup uses **GitHub Actions** to:
1. ✅ Fetch panchang data **automatically every day at 6 AM IST**
2. ✅ Save to JSON files in your GitHub repo
3. ✅ iPhone Siri shortcut reads the JSON from GitHub
4. ✅ **Cost: $0 forever** (GitHub free tier)

---

## Architecture

```
GitHub Actions (Daily, 6 AM)
         ↓
    fetch_panchang.py
         ↓
   panchang.json (in repo)
    panchang_voice.json
         ↓
   GitHub Raw URL
         ↓
  iPhone Shortcut (Siri)
         ↓
   Speak to User
```

---

## Step-by-Step Setup

### **Step 1: Create GitHub Repository** (2 minutes)

1. Go to **https://github.com/new**
2. Name it: `panchang-data` (or any name you like)
3. Choose **"Public"** (so iPhone can read the JSON)
4. Click **"Create repository"**

### **Step 2: Add Files to Repo** (3 minutes)

1. In your new repo, create these files:

   **File 1: `fetch_panchang.py`**
   - Click "Add file" → "Create new file"
   - Name: `fetch_panchang.py`
   - Paste the content from `fetch_panchang.py` (the file I created)
   - Click "Commit changes"

   **File 2: `.github/workflows/fetch-panchang.yml`**
   - Click "Add file" → "Create new file"
   - Name: `.github/workflows/fetch-panchang.yml`
   - Paste the content from the workflow file
   - Click "Commit changes"

   **File 3: `requirements.txt`**
   - Click "Add file" → "Create new file"
   - Name: `requirements.txt`
   - Paste:
     ```
     requests==2.31.0
     beautifulsoup4==4.12.0
     ```
   - Click "Commit changes"

### **Step 3: Enable GitHub Actions** (1 minute)

1. Go to your repo's **"Actions"** tab
2. You should see "Fetch Panchang Data Daily" workflow
3. Click on it
4. Click **"Run workflow"** (blue button, right side)
5. Select **"Run workflow"** in the dropdown

This will run immediately. Wait 30 seconds, then refresh.

### **Step 4: Verify It Works** (1 minute)

1. Go to **"Code"** tab in your repo
2. You should see **`panchang.json`** and **`panchang_voice.json`** files
3. Click on `panchang_voice.json`
4. Click **"Raw"** button (top right)
5. **Copy this URL** - you'll need it for Siri!

Example: `https://raw.githubusercontent.com/YOUR-USERNAME/panchang-data/main/panchang_voice.json`

### **Step 5: Set Up Siri Shortcut** (3 minutes)

**On your iPhone:**

1. Open **"Shortcuts"** app
2. Tap **"+"** to create new shortcut
3. Tap **"Add Action"**
4. Search for: **"Get Contents of URL"**
5. Paste your JSON URL from Step 4
6. Tap **"Add Action"**
7. Search for: **"Get Dictionary Value"**
8. Set Key: `voice_text`
9. Tap **"Add Action"**
10. Search for: **"Speak Text"**
11. Text should auto-populate with the dictionary value

### **Step 6: Add to Siri** (2 minutes)

1. Tap the **three dots** (top right)
2. Tap **"Details"**
3. Name: `Panchang`
4. Toggle **"Show in Siri Suggestions"** ON
5. Tap **"Add to Siri"**
6. Record your voice command: **"Tell me today's panchang"**
7. Tap **"Done"**

### **Step 7: Test It!** (30 seconds)

Say: **"Hey Siri, tell me today's panchang"**

iPhone should speak: **"Today's Panchang: Tithi is Purnima upto 05:26 AM, Nakshatra is Mula upto 04:03 AM..."**

---

## How It Works

### Daily Automation
- **Time:** 6 AM IST every day (automatically)
- **Action:** GitHub Actions runs `fetch_panchang.py`
- **Result:** New JSON file is saved to your repo
- **iPhone:** Reads the latest JSON whenever you ask Siri

### No Server Running
- ✅ No Replit server needed
- ✅ No costs
- ✅ No manual updates
- ✅ Data updates automatically overnight

### Always Available
- ✅ Works offline (data cached on iPhone)
- ✅ Works with WiFi or cellular
- ✅ Instant response (just reads local data)

---

## Raw JSON URLs

After setup, you'll have these public URLs:

**Full Panchang Data (JSON):**
```
https://raw.githubusercontent.com/YOUR-USERNAME/panchang-data/main/panchang.json
```

**Voice-Friendly Version (Recommended for Siri):**
```
https://raw.githubusercontent.com/YOUR-USERNAME/panchang-data/main/panchang_voice.json
```

You can also view these in your browser anytime to see the raw data.

---

## Example JSON Files

### `panchang.json`
```json
{
  "status": "success",
  "last_updated": "2026-06-29T06:00:00.123456",
  "data": {
    "Tithi": "Purnima upto 05:26 AM, Jun 30",
    "Nakshatra": "Mula upto 04:03 AM, Jun 30",
    "Yoga": "Shukla upto 02:26 PM",
    "Sunrise": "05:26 AM",
    "Sunset": "07:23 PM",
    "Moonrise": "07:16 PM",
    "Moonset": "05:15 AM, Jun 30",
    ...
  },
  "count": 30
}
```

### `panchang_voice.json`
```json
{
  "status": "success",
  "last_updated": "2026-06-29T06:00:00.123456",
  "voice_text": "Today's Panchang: Tithi is Purnima upto 05:26 AM Jun 30, Nakshatra is Mula upto 04:03 AM Jun 30, Yoga is Shukla upto 02:26 PM, Sunrise is 05:26 AM, Sunset is 07:23 PM",
  "data": { ... }
}
```

---

## Customizing the Schedule

### Change Daily Fetch Time

Edit `.github/workflows/fetch-panchang.yml`:

**Current (6 AM IST):**
```yaml
- cron: '30 0 * * *'  # 6 AM IST
```

**Other times:**
```yaml
- cron: '0 0 * * *'   # 12:30 AM IST (midnight + 30 min)
- cron: '0 4 * * *'   # 9:30 AM IST
- cron: '0 12 * * *'  # 5:30 PM IST
- cron: '0 18 * * *'  # 11:30 PM IST
```

(The format is: minute hour * * *, in UTC. IST = UTC + 5:30)

---

## Advanced: Multiple Siri Shortcuts

Create shortcuts for specific elements:

**"What's Today's Tithi?"**
- URL: `https://raw.githubusercontent.com/YOUR-USERNAME/panchang-data/main/panchang.json`
- Get Dictionary Value Key: `data` → then `Tithi`

**"Show All Panchang"**
- URL: `https://raw.githubusercontent.com/YOUR-USERNAME/panchang-data/main/panchang.json`
- Show Result with all data

**"Search Nakshatra"**
- Same JSON, different key extraction

---

## Troubleshooting

### GitHub Actions Not Running

1. Go to **"Actions"** tab
2. Check if workflow is enabled (green checkmark)
3. Click on a failed workflow to see the error
4. Most likely: typo in `requirements.txt` or Python path

**Fix:** Re-run the workflow manually:
- Click on "Fetch Panchang Data Daily" workflow
- Click "Run workflow" button
- Check logs

### Siri Shortcut Won't Work

1. **Test the URL first:** Open it in Safari
   - `https://raw.githubusercontent.com/YOUR-USERNAME/panchang-data/main/panchang_voice.json`
   - Should show JSON data
2. **If it shows JSON:** Shortcut is correct, test again
3. **If 404 error:** 
   - Check repo is **Public** (not Private)
   - Check filename spelling exactly
   - Check GitHub username in URL

### "No panchang.json file in repo"

1. Go to **"Actions"** tab
2. Click the latest workflow run
3. Check if it succeeded (green checkmark)
4. If red X: Click on it to see error
5. Most likely: Internet error when fetching drikpanchang.com

**Fix:** Run workflow manually again

### Data Not Updating

1. Check the **last_updated** timestamp in the JSON
2. If it's old: Workflow hasn't run yet
3. Manually trigger: Go to Actions → Run workflow → Run workflow

---

## Cost Breakdown

| Service | Cost | Notes |
|---------|------|-------|
| GitHub (public repo) | **$0** | Free forever |
| GitHub Actions | **$0** | 2000 min/month free, uses ~1 min/day |
| Siri Shortcut | **$0** | Built-in to iOS |
| **Total** | **$0** | Zero cost forever! |

---

## Tips & Tricks

✅ **Always use raw.githubusercontent.com URL** (not github.com)

✅ **Make repo Public** (private repos can't be accessed by Siri)

✅ **Test JSON in browser first** before adding to Siri

✅ **Use panchang_voice.json for Siri** (cleaner voice output)

✅ **Use panchang.json for detailed data** (all elements in dict)

✅ **Can share the JSON URL with family** (they can create their own shortcuts)

---

## Example Full Siri Flow

```
User: "Hey Siri, tell me today's panchang"
         ↓
Siri runs shortcut
         ↓
Fetches: https://raw.githubusercontent.com/username/panchang-data/main/panchang_voice.json
         ↓
Parses JSON → Gets "voice_text" field
         ↓
Speaks: "Today's Panchang: Tithi is Purnima upto 05:26 AM..."
         ↓
Done! 🎉
```

---

## Next Steps

1. ✅ Create GitHub repo
2. ✅ Add the 3 files
3. ✅ Run workflow manually to test
4. ✅ Verify JSON files exist
5. ✅ Create Siri shortcut
6. ✅ Test with Siri
7. ✅ Enjoy automatic panchang data!

---

## Support

**Something broken?**
1. Check GitHub Actions logs (Actions tab → latest run)
2. Verify JSON files exist in repo
3. Test JSON URL in Safari browser
4. Make sure repo is Public

**Questions?**
- GitHub Actions docs: https://docs.github.com/actions
- Siri Shortcuts help: https://support.apple.com/shortcuts

---

## Why This Approach is Best

✨ **Truly Free:** Never costs a penny
✨ **Always Works:** GitHub won't shut down your free tier
✨ **Maintenance-Free:** Set it and forget it
✨ **Fast:** JSON loads instantly from GitHub
✨ **Shareable:** Give URL to family, they get same data
✨ **Transparent:** See all data in repo anytime
✨ **Safe:** No credit cards, no surprise charges

Enjoy your automated panchang! 🙏
