#!/usr/bin/env python3
"""
Interactive CLI for AI Talent Matching Agent

Menu-driven interface for:
- Matching candidates to positions
- Adjusting matching weights
- Viewing match results
- Exporting reports
"""

import json
import logging
from datetime import datetime
from typing import List, Dict, Any

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MatchingCLI:
    """Interactive CLI for matching agent."""
    
    def __init__(self):
        """Initialize the CLI."""
        self.last_results = None
        self.weights = {
            'skill_match': 0.4,
            'experience_match': 0.3,
            'cultural_fit': 0.2,
            'other': 0.1
        }
    
    def print_header(self, title: str):
        """Print formatted section header."""
        print("\n" + "=" * 70)
        print(f"  {title}")
        print("=" * 70 + "\n")
    
    def print_menu(self):
        """Display main menu."""
        self.print_header("AI Talent Matching Agent - Main Menu")
        print("1. Match candidates to position")
        print("2. View current matching weights")
        print("3. Adjust matching weights")
        print("4. View last results")
        print("5. Export results to file")
        print("6. Batch match (multiple positions)")
        print("7. Settings")
        print("8. Exit")
        print()
    
    def get_user_input(self, prompt: str, default: str = None) -> str:
        """Get input from user with optional default."""
        if default:
            prompt = f"{prompt} [{default}]: "
        else:
            prompt = f"{prompt}: "
        
        user_input = input(prompt).strip()
        return user_input if user_input else default
    
    def get_float_input(self, prompt: str, default: float = None) -> float:
        """Get float input from user."""
        while True:
            try:
                value = self.get_user_input(prompt, str(default) if default else None)
                return float(value)
            except ValueError:
                print("❌ Invalid number. Please try again.")
    
    def match_candidate_to_position(self):
        """Match a single candidate to a position."""
        self.print_header("Match Candidate to Position")
        
        # Get candidate info
        print("CANDIDATE INFORMATION:")
        candidate = {
            'id': self.get_user_input("Candidate ID"),
            'name': self.get_user_input("Candidate name"),
            'skills': [s.strip() for s in self.get_user_input("Skills (comma-separated)").split(",")],
            'years_experience': int(self.get_float_input("Years of experience", 5)),
            'seniority_level': self.get_user_input("Seniority level (junior/mid/senior)", "mid")
        }
        
        if not candidate['name'] or not candidate['skills']:
            print("❌ Candidate name and skills required")
            return
        
        # Get position info
        print("\nPOSITION INFORMATION:")
        position = {
            'id': self.get_user_input("Position ID"),
            'title': self.get_user_input("Job title"),
            'required_skills': [s.strip() for s in self.get_user_input("Required skills (comma-separated)").split(",")],
            'required_experience': int(self.get_float_input("Required years of experience", 3)),
            'seniority_level': self.get_user_input("Position level (junior/mid/senior)", "mid")
        }
        
        if not position['title'] or not position['required_skills']:
            print("❌ Position title and skills required")
            return
        
        print("\n🔄 Calculating match score...")
        
        # Calculate scores (mock - full implementation uses Claude)
        skill_match = self._score_skills(candidate, position)
        exp_match = self._score_experience(candidate, position)
        culture_match = self._score_cultural_fit(candidate, position)
        
        overall_score = (
            skill_match * self.weights['skill_match'] +
            exp_match * self.weights['experience_match'] +
            culture_match * self.weights['cultural_fit'] +
            75 * self.weights['other']
        )
        
        if overall_score >= 85:
            recommendation = "🟢 HIGHLY RECOMMENDED"
        elif overall_score >= 70:
            recommendation = "🟡 RECOMMENDED"
        elif overall_score >= 50:
            recommendation = "🟠 MAYBE"
        else:
            recommendation = "🔴 PASS"
        
        # Display results
        print("\n" + "-" * 70)
        print("MATCH RESULTS")
        print("-" * 70)
        print(f"Candidate: {candidate['name']} → Position: {position['title']}\n")
        print(f"Overall Score: {overall_score:.1f}/100 {recommendation}\n")
        print("Dimension Scores:")
        print(f"  • Skill Match:       {skill_match:6.1f}% (weight: {self.weights['skill_match']*100:.0f}%)")
        print(f"  • Experience Match:  {exp_match:6.1f}% (weight: {self.weights['experience_match']*100:.0f}%)")
        print(f"  • Cultural Fit:      {culture_match:6.1f}% (weight: {self.weights['cultural_fit']*100:.0f}%)")
        
        matched_skills = set(candidate['skills']) & set(position['required_skills'])
        missing_skills = set(position['required_skills']) - set(candidate['skills'])
        
        print(f"\nSkill Analysis:")
        print(f"  ✓ Matched:  {', '.join(matched_skills) if matched_skills else 'None'}")
        if missing_skills:
            print(f"  ✗ Missing:  {', '.join(missing_skills)}")
        
        print(f"\nExperience:")
        print(f"  Required: {position['required_experience']} years")
        print(f"  Candidate: {candidate['years_experience']} years")
        print("-" * 70)
        
        self.last_results = {
            'type': 'single_match',
            'candidate': candidate,
            'position': position,
            'scores': {
                'overall': overall_score,
                'skill_match': skill_match,
                'experience_match': exp_match,
                'cultural_fit': culture_match
            },
            'recommendation': recommendation,
            'timestamp': datetime.now().isoformat()
        }
        
        print("\n✅ Match calculated successfully")
    
    def view_weights(self):
        """Display current matching weights."""
        self.print_header("Current Matching Weights")
        
        total = sum(self.weights.values())
        for key, weight in self.weights.items():
            pct = (weight / total) * 100
            bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
            print(f"  {key:20s} {weight:.2f} ({bar}) {pct:.1f}%")
        
        print(f"\nTotal: {total:.2f} (should be 1.0 for proper weighting)")
    
    def adjust_weights(self):
        """Adjust matching weights."""
        self.print_header("Adjust Matching Weights")
        
        print(f"Current weights: {self.weights}\n")
        print("Enter new weights (decimal form, e.g., 0.4):")
        print("Note: Weights should sum to 1.0\n")
        
        new_weights = {}
        for key in self.weights.keys():
            new_weights[key] = self.get_float_input(f"  {key}", self.weights[key])
        
        total = sum(new_weights.values())
        if abs(total - 1.0) > 0.01:
            print(f"\n⚠️  Warning: Weights sum to {total:.2f}, not 1.0")
            confirm = input("Continue anyway? (y/n): ").strip().lower()
            if confirm != 'y':
                print("❌ Weights not updated")
                return
        
        self.weights = new_weights
        print(f"\n✅ Weights updated: {self.weights}")
    
    def view_results(self):
        """Display last results."""
        self.print_header("Last Results")
        
        if not self.last_results:
            print("❌ No results available")
            return
        
        results = self.last_results
        
        if results['type'] == 'single_match':
            print(f"Candidate: {results['candidate']['name']}")
            print(f"Position: {results['position']['title']}")
            print(f"Overall Score: {results['scores']['overall']:.1f}/100")
            print(f"Recommendation: {results['recommendation']}")
        
        print(f"\nTimestamp: {results['timestamp']}")
    
    def export_results(self):
        """Export last results to file."""
        self.print_header("Export Results")
        
        if not self.last_results:
            print("❌ No results to export")
            return
        
        filename = self.get_user_input(
            "Filename to export",
            f"match_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        
        try:
            with open(filename, 'w') as f:
                json.dump(self.last_results, f, indent=2)
            print(f"✅ Results exported to {filename}")
        except Exception as e:
            print(f"❌ Export failed: {e}")
    
    def batch_match(self):
        """Match multiple candidates to a position."""
        self.print_header("Batch Match - Multiple Candidates to Position")
        
        # Get position
        print("POSITION INFORMATION:")
        position = {
            'id': self.get_user_input("Position ID"),
            'title': self.get_user_input("Job title"),
            'required_skills': [s.strip() for s in self.get_user_input("Required skills").split(",")],
            'required_experience': int(self.get_float_input("Required years", 3)),
            'seniority_level': self.get_user_input("Level (junior/mid/senior)", "mid")
        }
        
        # Get candidates
        print("\nCANDIDATES:")
        candidates = []
        num_candidates = int(self.get_float_input("Number of candidates to match", 3))
        
        for i in range(num_candidates):
            print(f"\nCandidate {i+1}:")
            candidate = {
                'id': f"cand_{i+1}",
                'name': self.get_user_input(f"  Name"),
                'skills': [s.strip() for s in self.get_user_input(f"  Skills").split(",")],
                'years_experience': int(self.get_float_input(f"  Years", 5)),
                'seniority_level': self.get_user_input(f"  Level", "mid")
            }
            candidates.append(candidate)
        
        print(f"\n🔄 Matching {len(candidates)} candidates to {position['title']}...\n")
        
        # Calculate matches
        matches = []
        for candidate in candidates:
            skill_match = self._score_skills(candidate, position)
            exp_match = self._score_experience(candidate, position)
            culture_match = self._score_cultural_fit(candidate, position)
            
            overall = (
                skill_match * self.weights['skill_match'] +
                exp_match * self.weights['experience_match'] +
                culture_match * self.weights['cultural_fit'] +
                75 * self.weights['other']
            )
            
            matches.append({
                'candidate': candidate,
                'score': overall,
                'skill_match': skill_match,
                'exp_match': exp_match,
                'culture_match': culture_match
            })
        
        # Sort by score
        matches = sorted(matches, key=lambda x: x['score'], reverse=True)
        
        # Display results
        print("RANKED RESULTS:")
        print("-" * 70)
        for i, match in enumerate(matches, 1):
            name = match['candidate']['name']
            score = match['score']
            emoji = "🟢" if score >= 85 else "🟡" if score >= 70 else "🟠" if score >= 50 else "🔴"
            print(f"{i}. {name:20s} {score:6.1f}/100 {emoji}")
        print("-" * 70)
        
        self.last_results = {
            'type': 'batch_match',
            'position': position,
            'matches': matches,
            'timestamp': datetime.now().isoformat()
        }
        
        print("\n✅ Batch matching complete")
    
    def show_settings(self):
        """Show configuration."""
        self.print_header("Settings")
        
        print("Matching Agent Configuration:")
        print(f"  Config File: config.yaml")
        print(f"  Current Weights: {self.weights}")
        print(f"  Total Weight: {sum(self.weights.values()):.2f}")
        print("\nTo adjust weights, select option 3 from main menu")
    
    def _score_skills(self, candidate: Dict, position: Dict) -> float:
        """Score skill match."""
        candidate_skills = set(candidate.get('skills', []))
        required_skills = set(position.get('required_skills', []))
        
        if not required_skills:
            return 75.0
        
        matches = len(candidate_skills & required_skills)
        return (matches / len(required_skills)) * 100
    
    def _score_experience(self, candidate: Dict, position: Dict) -> float:
        """Score experience match."""
        candidate_exp = candidate.get('years_experience', 0)
        required_exp = position.get('required_experience', 0)
        
        if candidate_exp >= required_exp:
            return min(100, 75 + (10 * (candidate_exp - required_exp)))
        else:
            return (candidate_exp / required_exp) * 75 if required_exp > 0 else 50
    
    def _score_cultural_fit(self, candidate: Dict, position: Dict) -> float:
        """Score cultural fit."""
        candidate_level = candidate.get('seniority_level', 'mid')
        position_level = position.get('seniority_level', 'mid')
        
        return 85.0 if candidate_level == position_level else 65.0
    
    def run(self):
        """Main CLI loop."""
        print("\n🚀 AI Talent Matching Agent - Interactive CLI")
        
        while True:
            self.print_menu()
            choice = input("Select option (1-8): ").strip()
            
            if choice == "1":
                self.match_candidate_to_position()
            elif choice == "2":
                self.view_weights()
            elif choice == "3":
                self.adjust_weights()
            elif choice == "4":
                self.view_results()
            elif choice == "5":
                self.export_results()
            elif choice == "6":
                self.batch_match()
            elif choice == "7":
                self.show_settings()
            elif choice == "8":
                print("\n👋 Goodbye!\n")
                break
            else:
                print("❌ Invalid option. Please try again.")


def main():
    """Entry point."""
    cli = MatchingCLI()
    cli.run()


if __name__ == "__main__":
    main()
