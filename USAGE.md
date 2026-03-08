# Running AI Talent Matching Agent: User Guides

Guide for using the interactive CLI and web dashboard to match candidates to positions.

## ⚡ Quick Start

### Prerequisites
```bash
pip install flask python-dotenv
```

### Starting the Interfaces

**CLI (Terminal):**
```bash
python interactive_cli.py
```

**Web Dashboard (Browser):**
```bash
python app.py
# Open: http://localhost:5001
```

---

## 🎯 Interactive CLI Usage

The fastest way to match candidates from your terminal.

### Starting
```bash
python interactive_cli.py
```

### Main Menu Options

**Option 1: Match Candidate to Position**
- Enter candidate details (skills, experience, level)
- Enter position requirements
- Get detailed match score with breakdown

**Option 2: View Weights**
- See current scoring weights (skills, experience, cultural fit, other)
- Visual percentage bars

**Option 3: Adjust Weights**
- Change matching formula weights
- Customize scoring emphasis
- Real-time impact on scoring

**Option 4: View Last Results**
- Display results from last operation
- Quick review of scores

**Option 5: Export Results**
- Save match results to JSON file
- Timestamped filename
- Share with team

**Option 6: Batch Match**
- Match multiple candidates to one position
- Automatic ranking by score
- See all candidates at once

**Option 7: Settings**
- View configuration
- Check weight totals

**Option 8: Exit**

### Example: Match Senior Engineer

```bash
$ python interactive_cli.py

Select option: 1  # Match Candidate

CANDIDATE INFORMATION:
Candidate ID: cand_001
Candidate name: Jane Smith
Skills (comma-separated): Python, PyTorch, Deep Learning, Research
Years of experience: 7
Seniority level: senior

POSITION INFORMATION:
Position ID: pos_001
Job title: Senior ML Research Engineer
Required skills (comma-separated): Python, PyTorch, Deep Learning
Required years of experience: 5
Position level: senior

🔄 Calculating match score...

MATCH RESULTS
Overall Score: 92.5/100 🟢 HIGHLY RECOMMENDED
Dimension Scores:
  • Skill Match:       100% (weight: 40%)
  • Experience Match:  100% (weight: 30%)
  • Cultural Fit:       85% (weight: 20%)
```

### Example: Batch Match Multiple Candidates

```bash
$ python interactive_cli.py

Select option: 6  # Batch match

POSITION INFORMATION:
Position ID: open_001
Job title: ML Engineer
Required skills: Python,PyTorch,Transformers
Required years: 3
Position level: mid

CANDIDATES:
Number of candidates: 3

Candidate 1:
  Name: Alice Brown
  Skills: Python,PyTorch,Research
  Years: 5
  Level: mid

Candidate 2:
  Name Bob Chen
  Skills: Python,TensorFlow
  Years: 4
  Level: senior

Candidate 3:
  Name: Carol Davis
  Skills: Python,PyTorch,Transformers
  Years: 6
  Level: senior

RANKED RESULTS:
1. Carol Davis             92.5/100 🟢
2. Bob Chen                75.0/100 🟡
3. Alice Brown             65.3/100 🟠
```

---

## 🌐 Web Dashboard Usage

Beautiful interface for matching candidates to positions.

### Starting
```bash
python app.py
# Then open: http://localhost:5001
```

### Features

**Tab 1: 1:1 Match**
- Match single candidate to position
- Two-column form (left: candidate, right: position)
- Visual score display with progress bars
- Skill analysis (matched vs. missing)
- One-click export

**Tab 2: Batch Match**
- Position details
- Add multiple candidates dynamically
- + Add Candidate button
- Automatic ranking
- Export all results

**Tab 3: Help**
- Scoring methodology explanation
- Tips for using the tool
- Weight explanations

### Example: Web Dashboard Workflow

**1. Open Dashboard**
```
http://localhost:5001
```

**2. Click "1:1 Match" Tab**
- Fill candidate info (left)
- Fill position info (right)
- Click "Calculate Match Score"

**3. View Results**
- See overall score (large numbers)
- Color-coded recommendation
- Three progress bars (skills, experience, fit)
- Skill matching analysis
- Export button

**4. Try Batch Match**
- Switch to "Batch Match" tab
- Enter single position
- Add candidates with "Add Candidate" button
- Click "Run Batch Match"
- See ranked list
- Export all scores

---

## 🎨 Understanding the Scoring

### Dimensions (4 factors)

**1. Skill Match (40%)**
- Percentage of required skills the candidate has
- Example: Need [Python, PyTorch, TensorFlow], Candidate has [Python, PyTorch] = 67%

**2. Experience Match (30%)**
- How well current experience matches requirement
- Example: Need 5 years, Candidate has 7 years = 100% +bonus
- Example: Need 5 years, Candidate has 3 years = 60%

**3. Cultural Fit (20%)**
- Seniority level alignment
- junior→junior, mid→mid, senior→senior = Highest score

**4. Other Factors (10%)**
- Default baseline

### Overall Score Calculation
```
Overall = (Skills × 0.4) + (Experience × 0.3) + (Culture × 0.2) + (Other × 0.1)
```

### Recommendations
- **🟢 85-100:** Highly Recommended
- **🟡 70-84:** Recommended
- **🟠 50-69:** Maybe
- **🔴 <50:** Pass

---

## 📊 Usage Scenarios

### Scenario 1: Quick Single Match
```bash
python interactive_cli.py
# Option 1
# Enter candidate and position details
# See instant match score
```

### Scenario 2: Team Hiring Review
```bash
python app.py
# Open in browser at localhost:5001
# Use Batch Match tab
# Add candidates from your pool
# See ranked leaderboard
# Export as JSON report
```

### Scenario 3: Adjust Scoring for Your Needs
```bash
python interactive_cli.py
# Option 3: Adjust Weights
# Increase skill weight if skills most important
# Increase experience if seniority critical
# Option 1: Run match with new weights
```

### Scenario 4: Compare Multiple Candidates
```bash
python app.py
# Batch Match tab
# Add 5-10 candidates
# See automatically ranked list
# Click Export for sharing
```

---

## 💾 Exporting Results

### CLI Export
```
Select option: 5
Filename: team_matches_march.json
✅ Results exported to team_matches_march.json
```

### Web Export
- Click "📥 Export" button on results
- Browser downloads JSON file
- Includes all match details

### JSON Format
```json
{
  "type": "batch",
  "position": {
    "title": "ML Engineer",
    "required_skills": ["Python", "PyTorch"],
    "required_experience": 3,
    "seniority_level": "mid"
  },
  "matches": [
    {
      "candidate_name": "Jane Smith",
      "overall_score": 92.5,
      "skill_match": 100,
      "experience_match": 95,
      "cultural_fit": 85
    }
  ]
}
```

---

## ⚙️ Configuration

### Weights (config.yaml)
```yaml
matching:
  weights:
    skill_match: 0.4
    experience_match: 0.3
    cultural_fit: 0.2
    other: 0.1
```

### Adjust in CLI
- Option 3 allows real-time weight adjustment
- Changes persist for current session
- Or edit config.yaml before running

---

## 🔧 Troubleshooting

**Port 5001 already in use?**
```bash
# Edit app.py, change port=5001 to another number
python app.py --port 5002
```

**No results displayed?**
- Make sure all required fields are filled
- Check that skills/experience are entered
- Try with test data

**Export not working?**
- Check download folder
- Try different filename
- Ensure write permissions

---

## 📈 Tips & Best Practices

1. **Be Specific with Skills**
   - Use exact skill names (Python, not coding)
   - Comma-separated format

2. **Adjust Weights for Your Needs**
   - Skills-heavy role? Increase skill_match weight
   - Experience critical? Bump experience_match
   - Cultural fit important? Adjust cultural_fit

3. **Use Batch Matching**
   - Compare multiple candidates at once
   - Get automatic ranking
   - Save time vs. 1:1 matching

4. **Export for Stakeholders**
   - Share JSON reports with hiring team
   - Show objective scoring
   - Use rankings to decide interviews

5. **Iterate on Parameters**
   - Try different weight combinations
   - See how scores change
   - Find the right formula for your org

---

## 📱 Both Interfaces

|  | CLI | Web |
|---|-----|-----|
| Speed | ⚡ Fast | 📊 Visual |
| 1:1 Match | ✅ Yes | ✅ Yes |
| Batch Match | ✅ Yes | ✅ Yes |
| Weight Adjustment | ✅ Interactive | ❌ Manual edit |
| Export | ✅ JSON | ✅ JSON |
| Sharing | 📄 File | 🌐 Link |
| Batch Size | Limited | Limited |

---

## 🚀 Next Steps

1. Try the CLI: `python interactive_cli.py`
2. Try the web: `python app.py` → http://localhost:5001
3. Match your first candidate
4. Adjust weights for your use case
5. Batch match your candidate pool
6. Export and share results

Happy matching! 👥
