"""
Tests for AI Talent Matching Agent
"""

import unittest
from src.matching_agent import match_candidate_to_role

class TestMatchingAgent(unittest.TestCase):
    def setUp(self):
        self.sample_candidate = {
            "id": "cand_001",
            "name": "John Doe",
            "skills": ["Python", "PyTorch", "Computer Vision"],
            "experience_years": 5,
            "research_domain": "AI/ML"
        }
        
        self.sample_job = {
            "id": "job_001",
            "title": "AI Engineer, Computer Vision",
            "required_skills": ["Python", "PyTorch", "Deep Learning"],
            "seniority": "senior",
            "domain": "Computer Vision"
        }
    
    def test_matching_returns_expected_structure(self):
        result = match_candidate_to_role(self.sample_candidate, self.sample_job)
        self.assertIn("candidate_id", result)
        self.assertIn("job_id", result)
        self.assertIn("match_score", result)
        self.assertIn("reasoning", result)
        self.assertIn("strengths", result)
        self.assertIn("gaps", result)
    
    def test_match_score_is_valid_range(self):
        result = match_candidate_to_role(self.sample_candidate, self.sample_job)
        self.assertGreaterEqual(result["match_score"], 0.0)
        self.assertLessEqual(result["match_score"], 100.0)

if __name__ == "__main__":
    unittest.main()