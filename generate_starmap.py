import os
import json
import glob
import re

def build_catalog():
    topics = []

    # 1. AEGIS Flagship
    topics.append({
        "id": "aegis_drone_defense",
        "name": "AEGIS Multi-Medium Drone Defense System",
        "category": "Defense & Aero",
        "folder": "tinkering/frontier_hybrids",
        "url": "https://github.com/am-LLM/tinkering/blob/main/frontier_hybrids/aegis_drone_defense_system.py",
        "desc": "Cost-asymmetric kinetic C-UAS/C-USV interceptor with passive acoustic TDoA triangulation and 15-state ES-EKF optical flow.",
        "tags": ["C-UAS", "TDoA", "True Proportional Nav", "Defense", "EKF"],
        "size": 3.0,
        "cluster": "defense"
    })

    # 2. Frontier Engines (1-70)
    engine_files = sorted(glob.glob("/Users/alimalik/tinkering/frontier_hybrids/engine_*.py"))
    for f in engine_files:
        name = os.path.basename(f).replace(".py", "")
        with open(f, "r") as fp:
            content = fp.read()
        title_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
        clean_name = name.replace("engine_", "").replace("_", " ").title()
        desc = "Production cross-domain physical, AI & cryptographic engine."
        if title_match:
            lines = [l.strip() for l in title_match.group(1).strip().split("\n") if l.strip()]
            if lines:
                clean_name = lines[0][:65]
                if len(lines) > 1:
                    desc = " ".join(lines[1:3])[:190]
        
        # Determine cluster
        lname = name.lower()
        if any(w in lname for w in ["ai", "thought", "cognitron", "guardrail", "jailbreak", "snn", "compiler", "pruning", "llm"]):
            cluster = "ai"
            cat = "AI & QA"
        elif any(w in lname for w in ["bci", "rodent", "interspecies", "organ", "tcell", "dna", "crispr", "myoglobin", "pain", "sepsis", "calcium", "bionic", "tissue", "optogenetic"]):
            cluster = "bio"
            cat = "Bionics & Bio"
        elif any(w in lname for w in ["quantum", "cryocooler", "perovskite", "superconducting", "mram", "fluxon", "seebeck", "laser", "das"]):
            cluster = "quantum"
            cat = "Quantum & Energy"
        elif any(w in lname for w in ["scada", "radar", "sonar", "hypersonic", "plasma", "sail", "debris", "damper", "thruster", "ew", "traffic", "damper"]):
            cluster = "defense"
            cat = "Defense & Aero"
        else:
            cluster = "frontier"
            cat = "Frontier Engines"

        topics.append({
            "id": name,
            "name": clean_name,
            "category": cat,
            "folder": "tinkering/frontier_hybrids",
            "url": f"https://github.com/am-LLM/tinkering/blob/main/frontier_hybrids/{name}.py",
            "desc": desc,
            "tags": ["Frontier Engine", "Math Solver", "Python 3.14"],
            "size": 2.2 if "68" in name or "69" in name or "70" in name or "67" in name or "66" in name else 1.6,
            "cluster": cluster
        })

    # 3. Domain Laboratories
    domain_labs = [
        ("Aerospace GNC & Flight Dynamics", "aerospace_gnc", "15-state ES-EKF, ULA MVDR beamforming, Space Shuttle TMR FDIR, and Z3 formal proofs.", "Defense & Aero", "defense"),
        ("Acoustic & Seismic Metamaterials", "acoustic_seismic_metamaterials", "Westervelt non-linear acoustic fields and lithospheric rate-state friction.", "Frontier Engines", "frontier"),
        ("Advanced Quantum SCADA", "advanced_quantum_scada", "Tokamak MHD equilibrium, QKD satellite links, and Modbus/DNP3 DPI firewalls.", "Quantum & Energy", "quantum"),
        ("Cyber Forensic & Post-Quantum Crypto", "cyber_forensic_crypto", "Hardened RISC-V gate model, tamper-evident Merkle blackbox, and BFT consensus.", "AI & QA", "ai"),
        ("Frugal Mechanics & Thermal Dynamics", "frugal_mechanics", "1D MOC water-hammer acoustic solver, Seebeck MPPT, and 2-RC ECM battery models.", "Quantum & Energy", "quantum"),
        ("GeoSeismic InSAR Vision & Navigation", "geoseismic_insar_vision", "Satellite SAR interferometry, phase unwrapping, and subterranean fault mapping.", "Defense & Aero", "defense"),
        ("Isomorphic Physics & Side-Channel Bridge", "isomorphic_hybrid", "Bidirectional state-space physics bridge and silicon DPA/CPA side-channel guards.", "Frontier Engines", "frontier"),
        ("NLP OSINT Knowledge DAG Engine", "nlp_osint_knowledge_dag", "Automated threat intelligence extraction, entity linking, and causal DAG reasoning.", "AI & QA", "ai"),
        ("Pediatric Cognitive Systems", "pediatric_cognitive_systems", "Developmental neural networks, active inference child-cognition models.", "Bionics & Bio", "bio"),
        ("Frontier Quant Hybrids & High-Speed Finance", "frontier_quant_hybrids", "Zero-allocation C limit order book, jump-diffusion volatility, and microstructure models.", "Business Strategy", "strategy"),
    ]
    for title, folder, desc, cat, cluster in domain_labs:
        topics.append({
            "id": f"lab_{folder}",
            "name": title,
            "category": cat,
            "folder": f"tinkering/domain_laboratories/{folder}",
            "url": f"https://github.com/am-LLM/tinkering/tree/main/domain_laboratories/{folder}",
            "desc": desc,
            "tags": ["Domain Lab", "Empirical Testbed"],
            "size": 2.4,
            "cluster": cluster
        })

    # 4. Enterprise Business Strategy & Market Analysis
    strategy_topics = [
        ("Quantitative Valuation & Financial Modeling", "DCF valuation, sensitivity matrices, unit economics (LTV/CAC), and capital allocation frameworks.", ["Valuation", "DCF", "LTV/CAC", "Financial Modeling"]),
        ("Go-To-Market (GTM) Strategy & TAM Sizing", "Asymmetric market entry frameworks, bottom-up TAM/SAM/SOM market sizing, and pricing strategies.", ["GTM", "Market Sizing", "TAM/SAM", "Pricing"]),
        ("Product-Led Growth (PLG) & Viral Mechanics", "Behavioral viral loops, K-factor optimization, activation funnel engineering, and organic product adoption.", ["PLG", "Viral Loops", "Growth", "Retention"]),
        ("Enterprise Risk, QHSE & ISO 22301 BCM", "Business Continuity Management, NIST SP 800-30 threat modeling, and crisis continuity architecture.", ["BCM", "ISO 22301", "NIST SP 800-30", "Risk"]),
        ("Competitive Intelligence & Supply-Chain OSINT", "Systematic open-source market intelligence, competitor vulnerability auditing, and supply-chain mapping.", ["OSINT", "Competitive Intel", "Supply Chain"]),
        ("Venture Capital Term Sheets & Governance", "Cap table modeling, liquidation preference analysis, vesting frameworks, and board governance.", ["Venture Capital", "Term Sheets", "Governance"]),
        ("Gray-Zone Escalation & Economic Game Theory", "Multi-agent non-cooperative game theory, economic warfare resilience, and geopolitical risk mitigation.", ["Game Theory", "Geopolitics", "Economic Defense"]),
    ]
    for i, (title, desc, tags) in enumerate(strategy_topics):
        topics.append({
            "id": f"strategy_{i+1}",
            "name": title,
            "category": "Business Strategy",
            "folder": "am-LLM/strategy",
            "url": "https://github.com/am-LLM/am-LLM#1--business-strategy-market-analysis--growth",
            "desc": desc,
            "tags": tags,
            "size": 2.5,
            "cluster": "strategy"
        })

    # 5. AI Management & Quality Assurance
    ai_qa_topics = [
        ("Hierarchical Multi-Agent Swarms", "Coordinator-Lead-Specialist autonomous agent architectures with strict contracts and reactive wakeups.", ["Multi-Agent", "Swarms", "Agentic AI", "Orchestration"]),
        ("Formal Verification & SMT (Z3) Safety Gates", "Mathematical proof of boundary invariants, zero hallucination constraints, and state-space safety.", ["Z3 Solver", "SMT", "Formal Verification", "Safety"]),
        ("AI Model Evals & Latency-Budget Profiling", "Automated evaluation benchmarks, test-time compute search (MCTS), and token-per-dollar optimization.", ["Model Evals", "MCTS", "Benchmarking", "Latency"]),
        ("Representation Engineering (RepE) Latent Steering", "Real-time subspace projection and activation clamping to neutralize adversarial attacks in latent space.", ["RepE", "Latent Steering", "Mechanistic Interpretability"]),
        ("Zero-Trust Automated Test Harnesses", "100% pass-rate regression testbenches, property-based fuzzing, and mutation testing suites.", ["QA", "Property Testing", "CI/CD", "Regression"]),
        ("Synthetic Dataset Generation & Curriculum AI", "Automated generation of dense technical bootcamps, code synthesis benchmarks, and verified training corpora.", ["Synthetic Data", "Curriculum", "Fine-Tuning"]),
    ]
    for i, (title, desc, tags) in enumerate(ai_qa_topics):
        topics.append({
            "id": f"ai_qa_{i+1}",
            "name": title,
            "category": "AI & QA",
            "folder": "am-LLM/ai_and_qa",
            "url": "https://github.com/am-LLM/am-LLM#2--ai-project-management--applied-engineering-leadership",
            "desc": desc,
            "tags": tags,
            "size": 2.5,
            "cluster": "ai"
        })

    # 6. Continuum Fields (Sample of key fields across the 418 continuum)
    continuum_fields = sorted(glob.glob("/Users/alimalik/tinkering/engineering_continuum/field_*"))
    for f in continuum_fields:
        name = os.path.basename(f)
        num_match = re.search(r"field_(\d+)_", name)
        num = num_match.group(1) if num_match else "000"
        title = name.replace(f"field_{num}_", "").replace("_", " ").title()
        topics.append({
            "id": name,
            "name": f"Field {num}: {title[:40]}",
            "category": "Continuum Fields",
            "folder": f"tinkering/engineering_continuum/{name}",
            "url": f"https://github.com/am-LLM/tinkering/tree/main/engineering_continuum/{name}",
            "desc": f"Empirical field investigation module covering verified mathematical mechanics, algorithms, and simulation models for {title.lower()}.",
            "tags": ["Continuum", f"Field {num}", "Mathematical Simulation"],
            "size": 1.0,
            "cluster": "continuum"
        })

    return topics

def generate_html():
    topics = build_catalog()
    topics_json = json.dumps(topics)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ali Malik (@am-LLM) — 3D Universal Knowledge Starmap</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;700&family=Outfit:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #030712;
            --panel: rgba(15, 23, 42, 0.85);
            --border: rgba(56, 189, 248, 0.2);
            --border-hover: rgba(56, 189, 248, 0.6);
            --cyan: #38bdf8;
            --gold: #fbbf24;
            --crimson: #f43f5e;
            --emerald: #34d399;
            --violet: #a855f7;
            --text: #f8fafc;
            --text-dim: #94a3b8;
        }}
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            user-select: none;
        }}
        body {{
            background: var(--bg);
            color: var(--text);
            font-family: 'Outfit', -apple-system, sans-serif;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
        }}
        #webgl-canvas {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }}
        /* UI Overlay */
        .hud-layer {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 10;
            pointer-events: none;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 20px;
        }}
        .hud-layer * {{
            pointer-events: auto;
        }}
        /* Top Navigation Header */
        .header-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--panel);
            backdrop-filter: blur(16px);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 12px 24px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
            gap: 16px;
            flex-wrap: wrap;
        }}
        .brand-title {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .brand-title h1 {{
            font-size: 1.15rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, #fff, var(--cyan));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .brand-badge {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            background: rgba(56, 189, 248, 0.15);
            color: var(--cyan);
            border: 1px solid var(--border);
            padding: 3px 8px;
            border-radius: 6px;
            font-weight: 600;
        }}
        /* Search Box */
        .search-container {{
            position: relative;
            flex: 1;
            max-width: 380px;
        }}
        .search-input {{
            width: 100%;
            background: rgba(2, 6, 23, 0.7);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 8px 14px 8px 36px;
            color: #fff;
            font-family: 'Outfit', sans-serif;
            font-size: 0.88rem;
            outline: none;
            transition: all 0.2s ease;
        }}
        .search-input:focus {{
            border-color: var(--cyan);
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
            background: rgba(2, 6, 23, 0.95);
        }}
        .search-icon {{
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-dim);
            font-size: 0.85rem;
        }}
        /* Category Filters */
        .category-filters {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}
        .filter-btn {{
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            color: var(--text-dim);
            font-size: 0.78rem;
            font-weight: 600;
            padding: 6px 12px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .filter-btn:hover, .filter-btn.active {{
            background: rgba(56, 189, 248, 0.2);
            color: #fff;
            border-color: var(--cyan);
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.25);
        }}
        .filter-btn .dot {{
            width: 7px;
            height: 7px;
            border-radius: 50%;
        }}
        /* Action Controls */
        .controls-group {{
            display: flex;
            gap: 8px;
        }}
        .ctrl-btn {{
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid var(--border);
            color: var(--text);
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .ctrl-btn:hover {{
            background: var(--cyan);
            color: #030712;
            border-color: var(--cyan);
        }}
        /* Side HUD Card / Modal */
        .side-panel {{
            position: absolute;
            right: 20px;
            top: 90px;
            width: 380px;
            max-height: calc(100vh - 120px);
            background: var(--panel);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 24px;
            box-shadow: 0 16px 40px rgba(0,0,0,0.6);
            display: none;
            flex-direction: column;
            gap: 16px;
            z-index: 20;
            overflow-y: auto;
            animation: slideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateX(30px); }}
            to {{ opacity: 1; transform: translateX(0); }}
        }}
        .side-panel.open {{
            display: flex;
        }}
        .panel-close {{
            position: absolute;
            top: 16px;
            right: 16px;
            background: transparent;
            border: none;
            color: var(--text-dim);
            font-size: 1.2rem;
            cursor: pointer;
        }}
        .panel-close:hover {{
            color: #fff;
        }}
        .panel-cat-badge {{
            display: inline-block;
            align-self: flex-start;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            padding: 4px 10px;
            border-radius: 6px;
            letter-spacing: 0.05em;
        }}
        .panel-title {{
            font-size: 1.3rem;
            font-weight: 700;
            line-height: 1.3;
            color: #fff;
        }}
        .panel-folder {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            color: var(--text-dim);
            background: rgba(0, 0, 0, 0.4);
            padding: 6px 10px;
            border-radius: 6px;
            word-break: break-all;
        }}
        .panel-desc {{
            font-size: 0.9rem;
            line-height: 1.6;
            color: #cbd5e1;
        }}
        .panel-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }}
        .tag-pill {{
            font-size: 0.7rem;
            font-family: 'JetBrains Mono', monospace;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #94a3b8;
            padding: 3px 8px;
            border-radius: 4px;
        }}
        .panel-btn {{
            margin-top: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: linear-gradient(135deg, var(--cyan), #0284c7);
            color: #030712;
            text-decoration: none;
            font-weight: 700;
            font-size: 0.88rem;
            padding: 12px 18px;
            border-radius: 10px;
            transition: all 0.2s;
            box-shadow: 0 4px 14px rgba(56, 189, 248, 0.35);
        }}
        .panel-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(56, 189, 248, 0.5);
        }}
        /* Hover Tooltip */
        #tooltip {{
            position: absolute;
            pointer-events: none;
            background: rgba(15, 23, 42, 0.92);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            padding: 10px 16px;
            border-radius: 12px;
            color: #fff;
            font-size: 0.82rem;
            box-shadow: 0 8px 24px rgba(0,0,0,0.5);
            display: none;
            z-index: 30;
            max-width: 280px;
            transform: translate(15px, 15px);
        }}
        #tooltip .t-cat {{
            font-size: 0.68rem;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 700;
            margin-bottom: 2px;
        }}
        #tooltip .t-title {{
            font-weight: 700;
            font-size: 0.88rem;
        }}
        /* Footer Bar */
        .footer-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            color: var(--text-dim);
            background: var(--panel);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 8px 18px;
        }}
        .footer-links a {{
            color: var(--cyan);
            text-decoration: none;
            margin-left: 14px;
        }}
        .footer-links a:hover {{
            text-decoration: underline;
        }}
        /* Search Dropdown */
        .search-results {{
            position: absolute;
            top: 46px;
            left: 0;
            width: 100%;
            max-height: 320px;
            overflow-y: auto;
            background: rgba(15, 23, 42, 0.96);
            backdrop-filter: blur(16px);
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: 0 12px 30px rgba(0,0,0,0.7);
            display: none;
            z-index: 100;
        }}
        .search-result-item {{
            padding: 10px 14px;
            cursor: pointer;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            transition: all 0.15s;
        }}
        .search-result-item:hover {{
            background: rgba(56, 189, 248, 0.15);
        }}
        .search-result-item .s-title {{
            font-size: 0.85rem;
            font-weight: 600;
            color: #fff;
        }}
        .search-result-item .s-cat {{
            font-size: 0.7rem;
            font-family: 'JetBrains Mono', monospace;
            color: var(--cyan);
        }}
    </style>
</head>
<body>
    <canvas id="webgl-canvas"></canvas>

    <div class="hud-layer">
        <!-- Top Navigation -->
        <header class="header-bar">
            <div class="brand-title">
                <h1>⚡ ALI MALIK</h1>
                <span class="brand-badge">500+ RESEARCH TOPIC UNIVERSE</span>
            </div>

            <!-- Real-time Search -->
            <div class="search-container">
                <span class="search-icon">🔍</span>
                <input type="text" id="search-box" class="search-input" placeholder="Warp to topic (e.g. BCI, Jailbreak, Valuation, SCADA, TDoA)..." autocomplete="off">
                <div id="search-results" class="search-results"></div>
            </div>

            <!-- Category Filters -->
            <div class="category-filters">
                <button class="filter-btn active" data-cat="all"><span class="dot" style="background: #fff;"></span> All Galaxy</button>
                <button class="filter-btn" data-cat="Frontier Engines"><span class="dot" style="background: var(--cyan);"></span> 70 Engines</button>
                <button class="filter-btn" data-cat="Business Strategy"><span class="dot" style="background: var(--gold);"></span> Strategy & Valuation</button>
                <button class="filter-btn" data-cat="AI & QA"><span class="dot" style="background: var(--violet);"></span> AI & QA Testing</button>
                <button class="filter-btn" data-cat="Defense & Aero"><span class="dot" style="background: var(--crimson);"></span> Defense & Aero</button>
                <button class="filter-btn" data-cat="Bionics & Bio"><span class="dot" style="background: var(--emerald);"></span> BCI & Interspecies</button>
                <button class="filter-btn" data-cat="Continuum Fields"><span class="dot" style="background: #94a3b8;"></span> 418 Continuum</button>
            </div>

            <!-- Controls -->
            <div class="controls-group">
                <button id="reset-cam-btn" class="ctrl-btn" title="Reset Galaxy View">🔄 Reset</button>
                <button id="audio-toggle-btn" class="ctrl-btn" title="Toggle Synthesizer Sound FX">🔊 Sound</button>
            </div>
        </header>

        <!-- Side Detail Panel -->
        <aside id="side-panel" class="side-panel">
            <button id="panel-close-btn" class="panel-close">✕</button>
            <span id="panel-cat" class="panel-cat-badge">Frontier Engine</span>
            <h2 id="panel-title" class="panel-title">Engine Name</h2>
            <div id="panel-folder" class="panel-folder">tinkering/frontier_hybrids</div>
            <p id="panel-desc" class="panel-desc">Description text goes here.</p>
            <div id="panel-tags" class="panel-tags"></div>
            <a id="panel-link" href="#" target="_blank" class="panel-btn">
                <span>View Source on GitHub</span>
                <span>➔</span>
            </a>
        </aside>

        <!-- Hover Tooltip -->
        <div id="tooltip">
            <div id="tooltip-cat" class="t-cat">CATEGORY</div>
            <div id="tooltip-title" class="t-title">Star Title</div>
        </div>

        <!-- Footer Bar -->
        <footer class="footer-bar">
            <div>🚀 <b>Navigation:</b> Left-Click + Drag: Rotate | Scroll: Zoom | Right-Click: Pan | Click Star: Warp & Inspect</div>
            <div class="footer-links">
                <a href="https://github.com/am-LLM" target="_blank">GitHub Profile</a>
                <a href="https://github.com/am-LLM/tinkering" target="_blank">Tinkering Master Repo</a>
            </div>
        </footer>
    </div>

    <!-- Three.js and OrbitControls from CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tween.js/18.6.4/tween.umd.js"></script>

    <script>
        // Topic Data Catalog
        const TOPICS = {topics_json};

        // Category Palette Mapping
        const CATEGORY_COLORS = {{
            "Frontier Engines": 0x38bdf8,   // Cyan
            "Business Strategy": 0xfbbf24,  // Gold
            "AI & QA": 0xa855f7,            // Violet
            "Defense & Aero": 0xf43f5e,     // Crimson
            "Bionics & Bio": 0x34d399,      // Emerald
            "Quantum & Energy": 0x38bdf8,   // Blue
            "Continuum Fields": 0x64748b    // Slate
        }};

        const CLUSTER_CENTERS = {{
            "defense": {{ x: -140, y: 30, z: -80 }},
            "ai": {{ x: 0, y: 70, z: 0 }},
            "strategy": {{ x: 130, y: 40, z: 70 }},
            "bio": {{ x: -70, y: -60, z: 120 }},
            "quantum": {{ x: 90, y: -50, z: -100 }},
            "frontier": {{ x: -40, y: 20, z: -120 }},
            "continuum": {{ x: 0, y: -20, z: 0 }}
        }};

        // Web Audio Synthesizer (Zero asset dependency)
        let audioCtx = null;
        let soundEnabled = true;

        function playChime(freq = 520, type = "sine") {{
            if (!soundEnabled) return;
            try {{
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.06, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 0.35);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.35);
            }} catch(e) {{}}
        }}

        // Scene, Camera, Renderer
        const canvas = document.getElementById("webgl-canvas");
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x030712, 0.0018);

        const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 3000);
        camera.position.set(0, 160, 360);

        const renderer = new THREE.WebGLRenderer({{ canvas, antialias: true, alpha: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.maxDistance = 900;
        controls.minDistance = 20;
        controls.autoRotate = true;
        controls.autoRotateSpeed = 0.4;

        // Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
        scene.add(ambientLight);

        // Cosmic Starfield Background
        const starGeo = new THREE.BufferGeometry();
        const starCount = 3500;
        const starPos = new Float32Array(starCount * 3);
        for (let i = 0; i < starCount * 3; i += 3) {{
            starPos[i] = (Math.random() - 0.5) * 2000;
            starPos[i+1] = (Math.random() - 0.5) * 2000;
            starPos[i+2] = (Math.random() - 0.5) * 2000;
        }}
        starGeo.setAttribute("position", new THREE.BufferAttribute(starPos, 3));
        const starMat = new THREE.PointsMaterial({{ color: 0x94a3b8, size: 1.2, transparent: true, opacity: 0.6 }});
        const starPoints = new THREE.Points(starGeo, starMat);
        scene.add(starPoints);

        // Nebula Clouds (Glowing billowy particles)
        const nebulaGroup = new THREE.Group();
        for (const [key, center] of Object.entries(CLUSTER_CENTERS)) {{
            const nebGeo = new THREE.SphereGeometry(35, 12, 12);
            let nColor = 0x38bdf8;
            if (key === "strategy") nColor = 0xfbbf24;
            if (key === "ai") nColor = 0xa855f7;
            if (key === "defense") nColor = 0xf43f5e;
            if (key === "bio") nColor = 0x34d399;
            const nebMat = new THREE.MeshBasicMaterial({{
                color: nColor,
                wireframe: true,
                transparent: true,
                opacity: 0.04
            }});
            const nebMesh = new THREE.Mesh(nebGeo, nebMat);
            nebMesh.position.set(center.x, center.y, center.z);
            nebulaGroup.add(nebMesh);
        }}
        scene.add(nebulaGroup);

        // Node Mesh Representation
        const nodeMeshes = [];
        const nodeDataMap = new Map();
        const raycaster = new THREE.Raycaster();
        const mouse = new THREE.Vector2();

        // Node Texture Generator
        function createGlowSprite(colorHex) {{
            const canvas = document.createElement("canvas");
            canvas.width = 64;
            canvas.height = 64;
            const ctx = canvas.getContext("2d");
            const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
            grad.addColorStop(0, "#ffffff");
            grad.addColorStop(0.2, colorHex);
            grad.addColorStop(0.6, colorHex + "44");
            grad.addColorStop(1, "transparent");
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 64, 64);
            return new THREE.CanvasTexture(canvas);
        }}

        // Layout Nodes into Galaxy
        TOPICS.forEach((item, index) => {{
            const cluster = CLUSTER_CENTERS[item.cluster] || CLUSTER_CENTERS["continuum"];
            let pos;

            if (item.cluster === "continuum") {{
                // Spiral disc layout for continuum
                const angle = index * 0.15;
                const radius = 60 + Math.sqrt(index) * 11;
                pos = new THREE.Vector3(
                    cluster.x + Math.cos(angle) * radius + (Math.random() - 0.5) * 20,
                    cluster.y + (Math.random() - 0.5) * 35,
                    cluster.z + Math.sin(angle) * radius + (Math.random() - 0.5) * 20
                );
            }} else {{
                // Clustered sphere layout
                const u = Math.random();
                const v = Math.random();
                const theta = u * 2.0 * Math.PI;
                const phi = Math.acos(2.0 * v - 1.0);
                const r = Math.cbrt(Math.random()) * 48;
                pos = new THREE.Vector3(
                    cluster.x + r * Math.sin(phi) * Math.cos(theta),
                    cluster.y + r * Math.sin(phi) * Math.sin(theta),
                    cluster.z + r * Math.cos(phi)
                );
            }}

            const colHex = CATEGORY_COLORS[item.category] || 0x38bdf8;
            const spriteMat = new THREE.SpriteMaterial({{
                map: createGlowSprite("#" + colHex.toString(16).padStart(6, '0')),
                color: 0xffffff,
                transparent: true,
                blending: THREE.AdditiveBlending
            }});

            const sprite = new THREE.Sprite(spriteMat);
            const scale = (item.size || 1.5) * 5.0;
            sprite.scale.set(scale, scale, 1);
            sprite.position.copy(pos);
            sprite.userData = item;

            scene.add(sprite);
            nodeMeshes.push(sprite);
            nodeDataMap.set(item.id, {{ mesh: sprite, data: item }});
        }});

        // Constellation Connecting Lines
        const lineMat = new THREE.LineBasicMaterial({{ color: 0x38bdf8, transparent: true, opacity: 0.15 }});
        const lineGeo = new THREE.BufferGeometry();
        const linePositions = [];
        for (let i = 0; i < nodeMeshes.length; i += 3) {{
            for (let j = i + 1; j < Math.min(i + 8, nodeMeshes.length); j++) {{
                if (nodeMeshes[i].userData.category === nodeMeshes[j].userData.category) {{
                    const p1 = nodeMeshes[i].position;
                    const p2 = nodeMeshes[j].position;
                    if (p1.distanceTo(p2) < 55) {{
                        linePositions.push(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z);
                    }}
                }}
            }}
        }}
        lineGeo.setAttribute("position", new THREE.Float32BufferAttribute(linePositions, 3));
        const linesMesh = new THREE.LineSegments(lineGeo, lineMat);
        scene.add(linesMesh);

        // UI Interactions
        const tooltip = document.getElementById("tooltip");
        const tooltipCat = document.getElementById("tooltip-cat");
        const tooltipTitle = document.getElementById("tooltip-title");
        const sidePanel = document.getElementById("side-panel");
        const panelCat = document.getElementById("panel-cat");
        const panelTitle = document.getElementById("panel-title");
        const panelFolder = document.getElementById("panel-folder");
        const panelDesc = document.getElementById("panel-desc");
        const panelTags = document.getElementById("panel-tags");
        const panelLink = document.getElementById("panel-link");
        const searchBox = document.getElementById("search-box");
        const searchResults = document.getElementById("search-results");

        let hoveredNode = null;
        let selectedNode = null;

        function showPanel(item) {{
            panelCat.textContent = item.category;
            panelCat.style.background = "rgba(56, 189, 248, 0.2)";
            panelCat.style.color = "#38bdf8";
            panelTitle.textContent = item.name;
            panelFolder.textContent = item.folder;
            panelDesc.textContent = item.desc;
            panelLink.href = item.url;

            panelTags.innerHTML = "";
            (item.tags || []).forEach(tag => {{
                const t = document.createElement("span");
                t.className = "tag-pill";
                t.textContent = tag;
                panelTags.appendChild(t);
            }});

            sidePanel.classList.add("open");
        }}

        function flyToNode(mesh, targetDist = 45) {{
            controls.autoRotate = false;
            const targetPos = mesh.position.clone();
            const camTargetPos = targetPos.clone().add(new THREE.Vector3(0, 15, targetDist));

            playChime(640, "triangle");

            new TWEEN.Tween(camera.position)
                .to(camTargetPos, 1200)
                .easing(TWEEN.Easing.Cubic.Out)
                .start();

            new TWEEN.Tween(controls.target)
                .to(targetPos, 1200)
                .easing(TWEEN.Easing.Cubic.Out)
                .start();

            showPanel(mesh.userData);
        }}

        // Window Resize
        window.addEventListener("resize", () => {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }});

        // Mouse Move for Hover Tooltip
        window.addEventListener("mousemove", (e) => {{
            mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
            mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;

            tooltip.style.left = e.clientX + "px";
            tooltip.style.top = e.clientY + "px";

            raycaster.setFromCamera(mouse, camera);
            const intersects = raycaster.intersectObjects(nodeMeshes);

            if (intersects.length > 0) {{
                const hit = intersects[0].object;
                if (hoveredNode !== hit) {{
                    hoveredNode = hit;
                    tooltipCat.textContent = hit.userData.category;
                    tooltipCat.style.color = "#38bdf8";
                    tooltipTitle.textContent = hit.userData.name;
                    tooltip.style.display = "block";
                    playChime(800, "sine");
                }}
            }} else {{
                if (hoveredNode) {{
                    hoveredNode = null;
                    tooltip.style.display = "none";
                }}
            }}
        }});

        // Click to Warp & Select
        window.addEventListener("click", (e) => {{
            if (e.target.closest(".hud-layer") && !e.target.closest("#webgl-canvas")) return;
            raycaster.setFromCamera(mouse, camera);
            const intersects = raycaster.intersectObjects(nodeMeshes);
            if (intersects.length > 0) {{
                const target = intersects[0].object;
                flyToNode(target);
            }}
        }});

        // Close Panel
        document.getElementById("panel-close-btn").addEventListener("click", () => {{
            sidePanel.classList.remove("open");
            controls.autoRotate = true;
        }});

        // Reset Camera
        document.getElementById("reset-cam-btn").addEventListener("click", () => {{
            sidePanel.classList.remove("open");
            controls.autoRotate = true;
            new TWEEN.Tween(camera.position).to({{ x: 0, y: 160, z: 360 }}, 1000).easing(TWEEN.Easing.Cubic.Out).start();
            new TWEEN.Tween(controls.target).to({{ x: 0, y: 0, z: 0 }}, 1000).easing(TWEEN.Easing.Cubic.Out).start();
        }});

        // Audio Toggle
        const audioBtn = document.getElementById("audio-toggle-btn");
        audioBtn.addEventListener("click", () => {{
            soundEnabled = !soundEnabled;
            audioBtn.textContent = soundEnabled ? "🔊 Sound" : "🔇 Muted";
        }});

        // Category Filter Buttons
        document.querySelectorAll(".filter-btn").forEach(btn => {{
            btn.addEventListener("click", () => {{
                document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
                btn.classList.add("active");
                const cat = btn.getAttribute("data-cat");

                nodeMeshes.forEach(mesh => {{
                    if (cat === "all" || mesh.userData.category === cat) {{
                        mesh.visible = true;
                    }} else {{
                        mesh.visible = false;
                    }}
                }});
                playChime(480, "square");
            }});
        }});

        // Search Autocomplete & Warp
        searchBox.addEventListener("input", (e) => {{
            const q = e.target.value.toLowerCase().trim();
            if (!q) {{
                searchResults.style.display = "none";
                return;
            }}
            const matches = TOPICS.filter(t => 
                t.name.toLowerCase().includes(q) || 
                t.desc.toLowerCase().includes(q) ||
                t.category.toLowerCase().includes(q) ||
                (t.tags && t.tags.some(tag => tag.toLowerCase().includes(q)))
            ).slice(0, 8);

            if (matches.length === 0) {{
                searchResults.style.display = "none";
                return;
            }}

            searchResults.innerHTML = "";
            matches.forEach(item => {{
                const div = document.createElement("div");
                div.className = "search-result-item";
                div.innerHTML = `<div class="s-title">${{item.name}}</div><div class="s-cat">${{item.category}} • ${{item.folder}}</div>`;
                div.addEventListener("click", () => {{
                    const entry = nodeDataMap.get(item.id);
                    if (entry) {{
                        flyToNode(entry.mesh);
                    }}
                    searchResults.style.display = "none";
                    searchBox.value = "";
                }});
                searchResults.appendChild(div);
            }});
            searchResults.style.display = "block";
        }});

        // Hide search on outside click
        window.addEventListener("click", (e) => {{
            if (!e.target.closest(".search-container")) {{
                searchResults.style.display = "none";
            }}
        }});

        // Animation Loop
        function animate(time) {{
            requestAnimationFrame(animate);
            TWEEN.update();
            controls.update();
            starPoints.rotation.y += 0.0002;
            nebulaGroup.rotation.y += 0.0003;
            renderer.render(scene, camera);
        }}
        requestAnimationFrame(animate);
    </script>
</body>
</html>
"""
    return html

if __name__ == "__main__":
    html_content = generate_html()
    
    # Write to am-LLM root
    with open("/Users/alimalik/am-LLM/index.html", "w") as fp:
        fp.write(html_content)
    print("Wrote /Users/alimalik/am-LLM/index.html")

    # Write to tinkering root & docs/
    with open("/Users/alimalik/tinkering/index.html", "w") as fp:
        fp.write(html_content)
    os.makedirs("/Users/alimalik/tinkering/docs", exist_ok=True)
    with open("/Users/alimalik/tinkering/docs/index.html", "w") as fp:
        fp.write(html_content)
    print("Wrote /Users/alimalik/tinkering/index.html and docs/index.html")
