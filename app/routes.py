from flask import Blueprint, jsonify, render_template

from .redis_client import get_redis_client

main_bp = Blueprint("main", __name__)

TEAM_INFO = {
    "name": "Nasa",
    "event": "NASA International Space Apps Challenge 2026",
    "track": "Galactic Problem-Solvers & Space Data Computation",
    "motto": "Deciphering Space Telemetry through Scalable Computation",
}

PROJECT_DETAILS = {
    "title": "AstroPulse: Autonomous Deep-Space Telemetry & Orbital Hazard Forecaster",
    "challenge_name": "NASA Space Apps Challenge: Navigating the Cosmos with Open Data",
    "tagline": "A high-performance computational platform analyzing planetary telemetry, solar flare shocks, and orbital trajectories in real-time.",
    "abstract": (
        "AstroPulse is an open-source astrodynamics and telemetry processing engine built by Team Nasa. "
        "By fusing NASA planetary datasets, real-time satellite observations, and high-throughput data processing matrices, "
        "our system predicts orbital collision risks and solar particle storm arrivals up to 48 hours before impact."
    ),
    "features": [
        {
            "icon": "orbit",
            "title": "Orbital Hazard Trajectory Prediction",
            "description": "Calculates n-body relativistic perturbation vectors and near-Earth object closest-approach probabilities in sub-second inference intervals.",
        },
        {
            "icon": "bolt",
            "title": "Real-Time Solar Event Detection",
            "description": "Monitors L1 Lagrangian point data from NASA SOHO and DSCOVR to provide proactive geomagnetic storm alerts for satellite constellations.",
        },
        {
            "icon": "layers",
            "title": "High-Throughput Data Processing Engine",
            "description": "Ingests and indexes over 10,000 telemetry datapoints per second using optimized in-memory streaming pipelines.",
        },
        {
            "icon": "globe",
            "title": "Interactive Scientific Visualization",
            "description": "Presents 3D celestial orbital paths, solar plasma flux curves, and downloadable research-grade CSV and JSON datasets.",
        },
    ],
    "tech_stack": [
        {"name": "Python & Flask 3", "type": "Core Architecture"},
        {"name": "Redis In-Memory Engine", "type": "Data Pipeline"},
        {"name": "Docker & Compose", "type": "Containerization"},
        {"name": "NASA Open APIs & ADS", "type": "Data Sources"},
        {"name": "Gunicorn WSGI", "type": "Production Server"},
    ],
    "repo_url": "https://github.com",
    "demo_url": "#project",
    "presentation_url": "#",
}

TEAM_MEMBERS = [
    {
        "id": 1,
        "name": "Alex Mercer",
        "role": "Team Lead & ML Astrodynamics Engineer",
        "university": "Massachusetts Institute of Technology (MIT)",
        "department": "Aeronautics & Astronautics",
        "bio": "Specializes in orbital trajectory optimization, Bayesian filtering, and coordinating mission pipeline architecture.",
        "photo": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&auto=format&fit=crop&q=80",
        "initials": "AM",
        "github": "https://github.com",
        "linkedin": "https://linkedin.com",
        "email": "alex@team-nasa.space",
    },
    {
        "id": 2,
        "name": "Sarah Lin",
        "role": "Full-Stack & Systems Architect",
        "university": "Harvard University",
        "department": "Computer Science & Applied Mathematics",
        "bio": "Builds high-performance web systems, Flask application factories, Docker microservices, and client rendering pipelines.",
        "photo": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400&auto=format&fit=crop&q=80",
        "initials": "SL",
        "github": "https://github.com",
        "linkedin": "https://linkedin.com",
        "email": "sarah@team-nasa.space",
    },
    {
        "id": 3,
        "name": "David Kim",
        "role": "Distributed Systems & Data Engineer",
        "university": "Stanford University",
        "department": "Computational Engineering",
        "bio": "Architects real-time telemetry streaming, container orchestration, and sub-millisecond memory tiers.",
        "photo": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&auto=format&fit=crop&q=80",
        "initials": "DK",
        "github": "https://github.com",
        "linkedin": "https://linkedin.com",
        "email": "david@team-nasa.space",
    },
    {
        "id": 4,
        "name": "Priya Sharma",
        "role": "Astrophysicist & Planetary Data Analyst",
        "university": "University of Cambridge",
        "department": "Institute of Astronomy",
        "bio": "Analyzes NASA planetary spectroscopy, solar plasma indices, and validates mathematical physics constraints.",
        "photo": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&auto=format&fit=crop&q=80",
        "initials": "PS",
        "github": "https://github.com",
        "linkedin": "https://linkedin.com",
        "email": "priya@team-nasa.space",
    },
    {
        "id": 5,
        "name": "Marcus Vance",
        "role": "UI/UX & Scientific Visualization Specialist",
        "university": "University of California, Berkeley",
        "department": "Cognitive Science & Visual Computing",
        "bio": "Crafts accessible, academic-grade interfaces, celestial orbit visualizers, and scientific communication assets.",
        "photo": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&auto=format&fit=crop&q=80",
        "initials": "MV",
        "github": "https://github.com",
        "linkedin": "https://linkedin.com",
        "email": "marcus@team-nasa.space",
    },
]


@main_bp.route("/")
def index():
    return render_template(
        "index.html",
        team=TEAM_INFO,
        project=PROJECT_DETAILS,
        members=TEAM_MEMBERS,
    )


@main_bp.route("/health")
def health():
    return jsonify(
        {
            "status": "healthy",
            "team": "Nasa",
            "challenge": "NASA Space Apps 2026",
        }
    )
