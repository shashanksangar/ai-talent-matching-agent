#!/usr/bin/env python3
"""
Web Interface for AI Talent Matching Agent

Flask-based application for intelligent candidate-to-position matching.
"""

from flask import Flask, render_template, request, jsonify, send_file
import json
import logging
from datetime import datetime
import io

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Store results in session
results_cache = {}


@app.route('/')
def index():
    """Home page."""
    return render_template('index.html')


@app.route('/api/match', methods=['POST'])
def api_match():
    """Match a candidate to a position."""
    try:
        data = request.json
        
        candidate = data.get('candidate', {})
        position = data.get('position', {})
        
        if not candidate.get('name') or not position.get('title'):
            return jsonify({'error': 'Candidate name and position title required'}), 400
        
        # Calculate scores
        skill_score = _score_skills(candidate, position)
        exp_score = _score_experience(candidate, position)
        culture_score = _score_cultural_fit(candidate, position)
        
        weights = {
            'skill_match': 0.4,
            'experience_match': 0.3,
            'cultural_fit': 0.2,
            'other': 0.1
        }
        
        overall_score = (
            skill_score * weights['skill_match'] +
            exp_score * weights['experience_match'] +
            culture_score * weights['cultural_fit'] +
            75 * weights['other']
        )
        
        if overall_score >= 85:
            recommendation = "Highly Recommended"
        elif overall_score >= 70:
            recommendation = "Recommended"
        elif overall_score >= 50:
            recommendation = "Maybe"
        else:
            recommendation = "Pass"
        
        result = {
            'candidate_name': candidate.get('name'),
            'position_title': position.get('title'),
            'overall_score': round(overall_score, 1),
            'skill_match': round(skill_score, 1),
            'experience_match': round(exp_score, 1),
            'cultural_fit': round(culture_score, 1),
            'recommendation': recommendation,
            'matched_skills': list(set(candidate.get('skills', [])) & set(position.get('required_skills', []))),
            'missing_skills': list(set(position.get('required_skills', [])) - set(candidate.get('skills', [])))
        }
        
        session_id = f"match_{datetime.now().timestamp()}"
        results_cache[session_id] = result
        
        return jsonify({'success': True, 'session_id': session_id, 'result': result})
    
    except Exception as e:
        logger.exception("Match error")
        return jsonify({'error': str(e)}), 500


@app.route('/api/batch-match', methods=['POST'])
def api_batch_match():
    """Match multiple candidates to a position."""
    try:
        data = request.json
        position = data.get('position', {})
        candidates = data.get('candidates', [])
        
        if not position.get('title') or not candidates:
            return jsonify({'error': 'Position and candidates required'}), 400
        
        # Calculate matches
        matches = []
        for cand in candidates:
            skill_score = _score_skills(cand, position)
            exp_score = _score_experience(cand, position)
            culture_score = _score_cultural_fit(cand, position)
            
            overall_score = (
                skill_score * 0.4 +
                exp_score * 0.3 +
                culture_score * 0.2 +
                75 * 0.1
            )
            
            matches.append({
                'candidate_name': cand.get('name'),
                'overall_score': round(overall_score, 1),
                'skill_match': round(skill_score, 1),
                'experience_match': round(exp_score, 1),
                'cultural_fit': round(culture_score, 1)
            })
        
        # Sort by score
        matches = sorted(matches, key=lambda x: x['overall_score'], reverse=True)
        
        session_id = f"batch_{datetime.now().timestamp()}"
        results_cache[session_id] = {'type': 'batch', 'position': position, 'matches': matches}
        
        return jsonify({'success': True, 'session_id': session_id, 'matches': matches})
    
    except Exception as e:
        logger.exception("Batch match error")
        return jsonify({'error': str(e)}), 500


@app.route('/api/export/<session_id>', methods=['GET'])
def api_export(session_id):
    """Export results as JSON."""
    try:
        if session_id not in results_cache:
            return jsonify({'error': 'Session not found'}), 404
        
        data = results_cache[session_id]
        json_data = json.dumps(data, indent=2)
        
        return send_file(
            io.BytesIO(json_data.encode()),
            mimetype='application/json',
            as_attachment=True,
            download_name=f"match_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
    
    except Exception as e:
        logger.exception("Export error")
        return jsonify({'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check."""
    return jsonify({'status': 'ok', 'service': 'AI Talent Matching Agent'})


def _score_skills(candidate, position):
    """Score skill match."""
    cand_skills = set(candidate.get('skills', []))
    req_skills = set(position.get('required_skills', []))
    if not req_skills:
        return 75.0
    matches = len(cand_skills & req_skills)
    return (matches / len(req_skills)) * 100


def _score_experience(candidate, position):
    """Score experience match."""
    cand_exp = candidate.get('years_experience', 0)
    req_exp = position.get('required_experience', 0)
    if cand_exp >= req_exp:
        return min(100, 75 + (10 * (cand_exp - req_exp)))
    else:
        return (cand_exp / req_exp) * 75 if req_exp > 0 else 50


def _score_cultural_fit(candidate, position):
    """Score cultural fit."""
    cand_level = candidate.get('seniority_level', 'mid')
    pos_level = position.get('seniority_level', 'mid')
    return 85.0 if cand_level == pos_level else 65.0


if __name__ == '__main__':
    print("\n🚀 Starting AI Talent Matching Agent Web Interface")
    print("📍 Access at: http://localhost:5001")
    print("   API Docs: http://localhost:5001/api/health\n")
    
    app.run(debug=True, host='0.0.0.0', port=5001)
