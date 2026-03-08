# AI Talent Matching Agent

Intelligent candidate-to-position matching with multi-dimensional scoring. Match candidates to jobs using skills analysis, experience alignment, and cultural fit scoring.

**🌟 Choose Your Interface:** CLI for terminal users, web dashboard for visual insights.

## ⚡ Quick Start

### Interactive CLI (Terminal)
```bash
python interactive_cli.py
# Menu-driven interface for matching candidates
```

### Web Dashboard (Browser)
```bash
python app.py
# Open: http://localhost:5001
# Single match and batch matching interface
```

## Features

- ✅ **1:1 Candidate Matching** - Score individual candidates against positions
- ✅ **Batch Matching** - Compare multiple candidates to one job
- ✅ **Multi-Dimensional Scoring** - Skills (40%), Experience (30%), Cultural Fit (20%), Other (10%)
- ✅ **Adjustable Weights** - Customize scoring emphasis for your hiring needs
- ✅ **Visual Results** - Progress bars, color-coded recommendations, detailed analysis
- ✅ **Skill Gap Analysis** - See matched vs. missing skills
- ✅ **JSON Export** - Share results with stakeholders
- ✅ **Interactive & Web** - Terminal and browser interfaces included

## Installation

1. Clone:
```bash
git clone https://github.com/shashanksangar/ai-talent-matching-agent.git
cd ai-talent-matching-agent
```

2. Install dependencies:
```bash
pip install flask python-dotenv
```

3. (Optional) Configure environment:
```bash
cp .env.example .env
# Add API keys if using Claude integration
```

## Usage Examples

### 📖 Complete Guide
See [USAGE.md](USAGE.md) for detailed tutorials:
- CLI menu-driven interface
- Web dashboard walkthrough
- Batch matching workflow
- Weight customization
- Exporting results

### CLI: Quick Match

**Start the CLI:**
```bash
python interactive_cli.py
```

**Menu Options:**
```
1. Match candidate to position
2. View current matching weights
3. Adjust matching weights
4. View last results
5. Export results to file
6. Batch match (multiple candidates)
7. Settings
8. Exit
```

**Example: Match One Candidate**
```
Select option: 1
Candidate name: Jane Smith
Skills: Python, PyTorch, Deep Learning
Years of experience: 5
Seniority level: senior

Job title: Senior ML Engineer
Required skills: Python, PyTorch
Required years: 3
Position level: senior

Overall Score: 92.5/100 🟢 HIGHLY RECOMMENDED
Skill Match: 100% | Experience: 95% | Cultural Fit: 85%
```

### CLI: Batch Matching

**Start CLI:**
```bash
python interactive_cli.py
```

**Select Option 6:**
- Enter position once
- Add multiple candidates
- See ranked results
- Export all scores

### 🌐 Web Dashboard

**Start Server:**
```bash
python app.py
# Open: http://localhost:5001
```

**Tabs Available:**
- **1:1 Match** - Single candidate to position
- **Batch Match** - Multiple candidates to one job
- **Help** - Scoring methodology explained

**Workflow:**
1. Fill candidate info (left column)
2. Fill position info (right column)
3. Click "Calculate Match Score"
4. See visual score breakdown
5. Click "📥 Export" to download JSON

## Configuration

### Scoring Dimensions

The matching algorithm scores across 4 dimensions:

1. **Skill Match (40%)**
   - What % of required skills does candidate have?
   - Example: Need [Python, PyTorch, TensorFlow], have [Python, PyTorch] = 67%

2. **Experience Match (30%)**
   - Does experience level meet requirement?
   - Example: Need 5 years, have 7 years = 100%
   - Example: Need 5 years, have 3 years = 60%

3. **Cultural Fit (20%)**
   - Do seniority levels align?
   - Examples: junior→junior, mid→mid, senior→senior

4. **Other Factors (10%)**
   - Baseline default score

### Adjust Weights

In CLI, select option 3 to adjust weights:
```
Current weights: {skill: 0.4, exp: 0.3, culture: 0.2, other: 0.1}

Enter new weights...
skill_match: 0.5
experience_match: 0.25
cultural_fit: 0.15
other: 0.1
```

## Project Structure

```
ai-talent-matching-agent/
├── interactive_cli.py      # CLI interface
├── app.py                  # Web server
├── templates/
│   └── index.html          # Web UI
├── src/
│   ├── matching_agent.py   # Core matching logic
│   ├── models/
│   └── utils/
├── config.yaml             # Configuration
├── .env.example            # Environment template
├── USAGE.md                # Detailed guide
└── README.md               # This file
```

## Development

### Run Tests
```bash
cd /Users/ssangar/ai-talent-matching-agent
python -m pytest tests/
```

## Contributing

Part of the **AI Talent Copilot** ecosystem.