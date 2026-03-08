# AI Talent Matching Agent

An agentic AI-powered tool for matching candidates to specific job roles. Uses multi-dimensional analysis to ensure optimal fit based on skills, experience, and domain expertise.

## Features

- **Multi-Dimensional Matching**: Evaluates skills, experience level, research fit, and career trajectory
- **AI-Powered Analysis**: Uses Claude to provide intelligent matching reasoning
- **Candidate-Role Alignment**: Identifies strengths and potential gaps
- **Match Scoring**: Provides quantified compatibility score (0-100)
- **Batch Processing**: Process multiple candidates against target roles

## Installation

1. Clone the repository:
```bash
git clone https://github.com/shashanksangar/ai-talent-matching-agent.git
cd ai-talent-matching-agent
```

2. Install dependencies:
```bash
pip install -e .
```

3. Configure environment:
```bash
cp .env.example .env
# Add your API keys and configurations
```

## Usage

Match a candidate to a specific job:
```bash
matching-agent --candidate candidate.json --job job_requirements.json
```

Or match candidates in batch mode:
```bash
matching-agent --batch candidates.csv --jobs jobs.csv
```

## Configuration

See `config.yaml` for matching parameters and weighting.

## Data Format

### Candidate Profile (JSON)
```json
{
  "id": "cand_001",
  "name": "Jane Smith",
  "skills": ["Python", "PyTorch", "Computer Vision"],
  "experience_years": 5,
  "research_domain": "AI/ML",
  "publications": 12,
  "previous_roles": ["ML Engineer", "Research Scientist"]
}
```

### Job Requirements (JSON)
```json
{
  "id": "job_001",
  "title": "AI Engineer, Computer Vision",
  "required_skills": ["Python", "PyTorch", "Deep Learning"],
  "seniority": "senior",
  "domain": "Computer Vision",
  "min_experience_years": 4,
  "preferred_background": "Academic or Research"
}
```

## Contributing

Part of the AI Talent Copilot ecosystem. See main project for guidelines.