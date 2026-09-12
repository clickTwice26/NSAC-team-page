from flask import Blueprint, jsonify, render_template, request

from .redis_client import get_redis_client

main_bp = Blueprint("main", __name__)

RESEARCH_PILLARS = [
    {
        "code": "AERO-904",
        "title": "Orbital Telemetry & Autonomous Guidance Systems",
        "lead": "Dr. Aris Thorne, Ph.D.",
        "institution": "Institute for Advanced Astronautics",
        "abstract": "Formulating real-time closed-loop sensor fusion pipelines for low-thrust deep space trajectories and solar-radiation pressure compensation.",
        "badge": "Active Grant NSF-8821",
        "status": "In Orbit Validation",
    },
    {
        "code": "ASTRO-412",
        "title": "Exoplanetary Atmospheric Spectroscopy & Biosignature Inversion",
        "lead": "Prof. Elena Vance-Marlowe",
        "institution": "Center for Computational Astrophysics",
        "abstract": "Bayesian retrieval architectures resolving non-equilibrium methane-carbon monoxide chemistry across M-dwarf transit spectra.",
        "badge": "JWST Cycle 3 Allocation",
        "status": "Peer Review",
    },
    {
        "code": "HELIOS-771",
        "title": "Magnetohydrodynamic Plasma Modeling & Solar Energetic Particles",
        "lead": "Dr. Kaelen Ruiz & Team Alpha",
        "institution": "Laboratory for Space Physics",
        "abstract": "High-fidelity kinetic simulations forecasting coronal mass ejection shock arrival frontiers across the L1 Lagrangian perimeter.",
        "badge": "NASA Space Apps Selected",
        "status": "Data Pipeline v2.4",
    },
]

FACULTY_MEMBERS = [
    {
        "name": "Prof. Arthur Pendelton, Sc.D.",
        "role": "Chair & Regius Professor of Astrophysical Dynamics",
        "affiliation": "Department of Earth, Atmospheric & Planetary Sciences",
        "bio": "Former mission specialist on Jovian Magnetospheric Explorer; specializes in relativistic gravitational perturbations and n-body resonance stabilization.",
        "initials": "AP",
    },
    {
        "name": "Dr. Siobhan Chen-Ramsay, Ph.D.",
        "role": "Principal Investigator, Computational Heliophysics Group",
        "affiliation": "Kavli Institute for Theoretical Astrochemistry",
        "bio": "Pioneered neural-operator surrogates for non-linear magnetohydrodynamics with ultra-low latency inference for space weather warning networks.",
        "initials": "SC",
    },
    {
        "name": "Dr. Tariq Al-Mansoor, D.Phil. (Oxon)",
        "role": "Senior Research Fellow & NASA Space Apps Technical Director",
        "affiliation": "Aeronautical Robotics & Deep Space Instrumentation Lab",
        "bio": "Directs hardware-in-the-loop validation of autonomous cubesat constellation swarms deployed for multi-point magnetospheric tomography.",
        "initials": "TM",
    },
    {
        "name": "Elena Rostova, M.Sc.",
        "role": "Lead Systems Architect & Doctoral Candidate",
        "affiliation": "Distributed Space Systems Laboratory",
        "bio": "Focuses on fault-tolerant telemetry synthesis, high-throughput Redis caching layers for telemetry ingestion, and telemetry packet verification.",
        "initials": "ER",
    },
]

PUBLICATIONS = [
    {
        "year": "2026",
        "journal": "Journal of Astrodynamics & Space Flight",
        "title": "Deterministic Rendezvous Geometries in Perturbed Low Lunar Orbits via Non-Linear Boundary Value Optimization",
        "authors": "Thorne, A., Al-Mansoor, T., & Rostova, E.",
        "doi": "10.1016/j.astrodyn.2026.04.112",
        "type": "Peer-Reviewed Article",
    },
    {
        "year": "2025",
        "journal": "Physical Review Letters (Astrophysics)",
        "title": "Resolving Anisotropic Turbulence in Solar Wind Magnetosheath Boundaries with Multi-Scale In-Situ Telemetry",
        "authors": "Chen-Ramsay, S., Pendelton, A., et al.",
        "doi": "10.1103/PhysRevLett.135.089101",
        "type": "Letter",
    },
    {
        "year": "2025",
        "journal": "NASA Technical Memorandum & Space Apps Proceedings",
        "title": "Decentralized Telemetry Consensus for Autonomous Lunar Swarm Topologies Under Intermittent Deep Space DSN Windows",
        "authors": "The Space Apps Research Consortium",
        "doi": "10.2514/6.2025-NASA-TM",
        "type": "Technical Report",
    },
]

DISPATCHES = [
    {
        "date": "September 14, 2026",
        "category": "Symposium Bulletin",
        "title": "Annual Colloquium on Deep-Space Navigation & Autonomous Orbital Constellations",
        "summary": "Keynote lectures by NASA Space Apps Challenge research teams on algorithmic resilience, telemetry streaming architectures, and real-time telemetry indexing.",
    },
    {
        "date": "August 28, 2026",
        "category": "Observatory Dispatch",
        "title": "Deployment of Real-Time High-Throughput Telemetry Ingestion Node",
        "summary": "The laboratory has integrated distributed memory caching to ingest 14,000 telemetry packets/sec with authenticated cluster synchronization.",
    },
    {
        "date": "July 12, 2026",
        "category": "Academic Grant",
        "title": "NSF & Planetary Defense Directorate Grant Award Announced",
        "summary": "Multi-year $4.2M initiative to model hazardous near-Earth trajectory uncertainties using neural gravitational operator approximations.",
    },
]


@main_bp.route("/")
def index():
    r = get_redis_client()
    redis_connected = False
    visits = 1
    system_latency = "0.42 ms"

    try:
        visits = r.incr("academic_portal_access_count")
        redis_connected = True
        redis_status = f"ONLINE (Verified {visits:,} Ingested Sessions)"
    except Exception as exc:
        visits = None
        redis_status = f"OFFLINE ({str(exc)})"

    return render_template(
        "index.html",
        redis_status=redis_status,
        redis_connected=redis_connected,
        visits=visits,
        system_latency=system_latency,
        pillars=RESEARCH_PILLARS,
        faculty=FACULTY_MEMBERS,
        publications=PUBLICATIONS,
        dispatches=DISPATCHES,
    )


@main_bp.route("/health/redis")
def redis_health():
    r = get_redis_client()
    try:
        is_alive = r.ping()
        return jsonify(
            {
                "status": "healthy",
                "redis_ping": is_alive,
                "node": "academic-cluster-node-01",
                "auth": "enforced",
            }
        )
    except Exception as exc:
        return jsonify({"status": "unhealthy", "error": str(exc)}), 500
