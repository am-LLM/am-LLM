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
        "desc": "Cost-asymmetric kinetic C-UAS/C-USV interceptor solving the $15k vs $2M missile dilemma with passive acoustic TDoA triangulation and 15-state ES-EKF optical flow.",
        "tags": ["C-UAS", "TDoA", "True Proportional Nav", "Defense", "EKF"],
        "size": 3.8,
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
        elif any(w in lname for w in ["scada", "radar", "sonar", "hypersonic", "plasma", "sail", "debris", "damper", "thruster", "ew", "traffic"]):
            cluster = "defense"
            cat = "Defense & Aero"
        else:
            cluster = "frontier"
            cat = "Frontier Engines"

        is_flagship = any(k in name for k in ["68", "69", "70", "67", "66", "51", "04", "01"])
        topics.append({
            "id": name,
            "name": clean_name,
            "category": cat,
            "folder": "tinkering/frontier_hybrids",
            "url": f"https://github.com/am-LLM/tinkering/blob/main/frontier_hybrids/{name}.py",
            "desc": desc,
            "tags": ["Frontier Engine", "Math Solver", "Python 3.14"],
            "size": 3.0 if is_flagship else 2.2,
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
            "size": 3.2,
            "cluster": cluster
        })

    # 4. Enterprise Business Strategy & Market Analysis
    strategy_topics = [
        ("Quantitative Valuation & DCF Financial Modeling", "DCF valuation, sensitivity matrices, unit economics (LTV/CAC), and capital allocation frameworks.", ["Valuation", "DCF", "LTV/CAC", "Financial Modeling"]),
        ("Go-To-Market (GTM) Strategy & TAM Sizing", "Asymmetric market entry frameworks, bottom-up TAM/SAM/SOM market sizing, and pricing strategies.", ["GTM", "Market Sizing", "TAM/SAM", "Pricing"]),
        ("Product-Led Growth (PLG) & Viral Dynamics", "Behavioral viral loops, K-factor optimization, activation funnel engineering, and organic product adoption.", ["PLG", "Viral Loops", "Growth", "Retention"]),
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
            "size": 3.4,
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
            "size": 3.4,
            "cluster": "ai"
        })

    # 6. Continuum Fields
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
            "size": 1.5,
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
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            /* Default Cyber Neon Theme */
            --bg-color: #060d1f;
            --bg-grad: radial-gradient(circle at 50% 50%, #0d1b38 0%, #081126 50%, #030712 100%);
            --panel: rgba(13, 23, 48, 0.94);
            --panel-border: rgba(0, 240, 255, 0.45);
            --primary: #00f0ff;
            --accent: #d946ef;
            --text: #ffffff;
            --text-secondary: #cbd5e1;
            --text-dim: #94a3b8;
            --glow: rgba(0, 240, 255, 0.4);
        }}

        /* Theme Presets */
        body.theme-cyber {{
            --bg-color: #060d1f;
            --bg-grad: radial-gradient(circle at 50% 50%, #0e1e3e 0%, #081126 50%, #030712 100%);
            --panel: rgba(13, 23, 48, 0.94);
            --panel-border: rgba(0, 240, 255, 0.45);
            --primary: #00f0ff;
            --accent: #d946ef;
            --glow: rgba(0, 240, 255, 0.4);
        }}

        body.theme-solar {{
            --bg-color: #1a0f05;
            --bg-grad: radial-gradient(circle at 50% 50%, #381f08 0%, #1f1105 50%, #0a0602 100%);
            --panel: rgba(38, 22, 10, 0.94);
            --panel-border: rgba(251, 191, 36, 0.5);
            --primary: #fbbf24;
            --accent: #f43f5e;
            --glow: rgba(251, 191, 36, 0.45);
        }}

        body.theme-cobalt {{
            --bg-color: #040e26;
            --bg-grad: radial-gradient(circle at 50% 50%, #0a2560 0%, #06163b 50%, #020717 100%);
            --panel: rgba(8, 25, 66, 0.94);
            --panel-border: rgba(56, 189, 248, 0.5);
            --primary: #38bdf8;
            --accent: #818cf8;
            --glow: rgba(56, 189, 248, 0.45);
        }}

        body.theme-matrix {{
            --bg-color: #03140b;
            --bg-grad: radial-gradient(circle at 50% 50%, #062b17 0%, #041a0e 50%, #010a05 100%);
            --panel: rgba(6, 36, 20, 0.94);
            --panel-border: rgba(52, 211, 153, 0.5);
            --primary: #00ffaa;
            --accent: #a3e635;
            --glow: rgba(0, 255, 170, 0.45);
        }}

        body.theme-slate {{
            --bg-color: #0f172a;
            --bg-grad: radial-gradient(circle at 50% 50%, #1e293b 0%, #0f172a 50%, #020617 100%);
            --panel: rgba(30, 41, 59, 0.95);
            --panel-border: rgba(148, 163, 184, 0.5);
            --primary: #ffffff;
            --accent: #38bdf8;
            --glow: rgba(255, 255, 255, 0.35);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            user-select: none;
        }}
        body {{
            background: var(--bg-color);
            background-image: var(--bg-grad);
            color: var(--text);
            font-family: 'Outfit', -apple-system, sans-serif;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
            transition: background 0.4s ease;
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
            padding: 16px 20px;
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
            backdrop-filter: blur(24px);
            border: 1px solid var(--panel-border);
            border-radius: 16px;
            padding: 10px 20px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7), 0 0 20px var(--glow);
            gap: 12px;
            flex-wrap: wrap;
            transition: all 0.3s ease;
        }}
        .brand-title {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .brand-title h1 {{
            font-size: 1.15rem;
            font-weight: 800;
            letter-spacing: -0.01em;
            background: linear-gradient(135deg, #ffffff 30%, var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .brand-badge {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            background: rgba(255, 255, 255, 0.1);
            color: var(--primary);
            border: 1px solid var(--panel-border);
            padding: 3px 8px;
            border-radius: 6px;
            font-weight: 700;
        }}
        /* Search Box */
        .search-container {{
            position: relative;
            flex: 1;
            max-width: 320px;
        }}
        .search-input {{
            width: 100%;
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid var(--panel-border);
            border-radius: 10px;
            padding: 8px 14px 8px 36px;
            color: #ffffff;
            font-family: 'Outfit', sans-serif;
            font-size: 0.88rem;
            font-weight: 500;
            outline: none;
            transition: all 0.2s ease;
        }}
        .search-input::placeholder {{
            color: var(--text-dim);
        }}
        .search-input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 14px var(--glow);
            background: rgba(0, 0, 0, 0.7);
        }}
        .search-icon {{
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--primary);
            font-size: 0.9rem;
        }}
        /* Category Filters */
        .category-filters {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }}
        .filter-btn {{
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: var(--text-secondary);
            font-size: 0.78rem;
            font-weight: 700;
            padding: 6px 12px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .filter-btn:hover, .filter-btn.active {{
            background: rgba(255, 255, 255, 0.18);
            color: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 0 12px var(--glow);
            transform: translateY(-1px);
        }}
        .filter-btn .dot {{
            width: 7px;
            height: 7px;
            border-radius: 50%;
            box-shadow: 0 0 8px currentColor;
        }}
        /* Action Controls & Theme Picker */
        .controls-group {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .theme-selector {{
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid var(--panel-border);
            color: var(--primary);
            padding: 6px 10px;
            border-radius: 8px;
            font-family: 'Outfit', sans-serif;
            font-size: 0.8rem;
            font-weight: 700;
            outline: none;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .theme-selector:hover {{
            box-shadow: 0 0 10px var(--glow);
        }}
        .theme-selector option {{
            background: #0b142c;
            color: #fff;
        }}
        .ctrl-btn {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--panel-border);
            color: var(--text);
            padding: 7px 12px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        .ctrl-btn:hover {{
            background: var(--primary);
            color: #030712;
            border-color: var(--primary);
            box-shadow: 0 0 12px var(--glow);
        }}
        /* Side HUD Card / Modal */
        .side-panel {{
            position: absolute;
            right: 20px;
            top: 80px;
            width: 410px;
            max-height: calc(100vh - 110px);
            background: var(--panel);
            backdrop-filter: blur(28px);
            border: 1px solid var(--panel-border);
            border-radius: 20px;
            padding: 24px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.8), 0 0 30px var(--glow);
            display: none;
            flex-direction: column;
            gap: 14px;
            z-index: 20;
            overflow-y: auto;
            animation: slideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateX(40px); }}
            to {{ opacity: 1; transform: translateX(0); }}
        }}
        .side-panel.open {{
            display: flex;
        }}
        .panel-close {{
            position: absolute;
            top: 16px;
            right: 16px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            width: 28px;
            height: 28px;
            color: var(--text-dim);
            font-size: 0.95rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }}
        .panel-close:hover {{
            color: #fff;
            background: rgba(244, 63, 94, 0.4);
            border-color: #f43f5e;
        }}
        .panel-cat-badge {{
            display: inline-block;
            align-self: flex-start;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.74rem;
            font-weight: 800;
            text-transform: uppercase;
            padding: 4px 10px;
            border-radius: 8px;
            letter-spacing: 0.05em;
            background: rgba(255, 255, 255, 0.1);
            color: var(--primary);
            border: 1px solid var(--primary);
            text-shadow: 0 0 10px var(--glow);
        }}
        .panel-title {{
            font-size: 1.3rem;
            font-weight: 800;
            line-height: 1.3;
            color: #ffffff;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
        }}
        .panel-folder {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            color: var(--primary);
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 7px 11px;
            border-radius: 8px;
            word-break: break-all;
        }}
        .panel-desc {{
            font-size: 0.92rem;
            line-height: 1.6;
            color: #e2e8f0;
        }}
        .panel-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }}
        .tag-pill {{
            font-size: 0.7rem;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 600;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #e2e8f0;
            padding: 3px 8px;
            border-radius: 6px;
        }}
        .panel-btn {{
            margin-top: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: #030712;
            text-decoration: none;
            font-weight: 800;
            font-size: 0.9rem;
            padding: 12px 18px;
            border-radius: 12px;
            transition: all 0.2s;
            box-shadow: 0 6px 20px var(--glow);
        }}
        .panel-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 28px var(--glow);
            filter: brightness(1.1);
        }}
        /* Hover Tooltip */
        #tooltip {{
            position: absolute;
            pointer-events: none;
            background: var(--panel);
            backdrop-filter: blur(16px);
            border: 1px solid var(--primary);
            padding: 10px 16px;
            border-radius: 12px;
            color: #ffffff;
            font-size: 0.85rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8), 0 0 15px var(--glow);
            display: none;
            z-index: 30;
            max-width: 290px;
            transform: translate(15px, 15px);
        }}
        #tooltip .t-cat {{
            font-size: 0.7rem;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 800;
            margin-bottom: 2px;
            text-transform: uppercase;
        }}
        #tooltip .t-title {{
            font-weight: 700;
            font-size: 0.92rem;
            color: #ffffff;
        }}
        /* Footer Bar */
        .footer-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            color: var(--text-secondary);
            background: var(--panel);
            backdrop-filter: blur(16px);
            border: 1px solid var(--panel-border);
            border-radius: 12px;
            padding: 8px 18px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
        }}
        .footer-links a {{
            color: var(--primary);
            text-decoration: none;
            font-weight: 700;
            margin-left: 14px;
        }}
        .footer-links a:hover {{
            text-decoration: underline;
            text-shadow: 0 0 8px var(--primary);
        }}
        /* Search Dropdown */
        .search-results {{
            position: absolute;
            top: 46px;
            left: 0;
            width: 100%;
            max-height: 320px;
            overflow-y: auto;
            background: var(--panel);
            backdrop-filter: blur(20px);
            border: 1px solid var(--primary);
            border-radius: 12px;
            box-shadow: 0 16px 40px rgba(0,0,0,0.8), 0 0 20px var(--glow);
            display: none;
            z-index: 100;
        }}
        .search-result-item {{
            padding: 10px 14px;
            cursor: pointer;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            transition: all 0.15s;
        }}
        .search-result-item:hover {{
            background: rgba(255, 255, 255, 0.15);
        }}
        .search-result-item .s-title {{
            font-size: 0.88rem;
            font-weight: 700;
            color: #ffffff;
        }}
        .search-result-item .s-cat {{
            font-size: 0.72rem;
            font-family: 'JetBrains Mono', monospace;
            color: var(--primary);
            margin-top: 2px;
        }}
    </style>
</head>
<body class="theme-cyber">
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
                <input type="text" id="search-box" class="search-input" placeholder="Search any topic (e.g. BCI, Jailbreak, Valuation, SCADA)..." autocomplete="off">
                <div id="search-results" class="search-results"></div>
            </div>

            <!-- Category Filters -->
            <div class="category-filters">
                <button class="filter-btn active" data-cat="all"><span class="dot" style="background: #ffffff;"></span> All Galaxy</button>
                <button class="filter-btn" data-cat="Frontier Engines"><span class="dot" style="background: #00f0ff;"></span> 70 Engines</button>
                <button class="filter-btn" data-cat="Business Strategy"><span class="dot" style="background: #ffd166;"></span> Strategy & Valuation</button>
                <button class="filter-btn" data-cat="AI & QA"><span class="dot" style="background: #d946ef;"></span> AI & QA Testing</button>
                <button class="filter-btn" data-cat="Defense & Aero"><span class="dot" style="background: #ff3366;"></span> Defense & Aero</button>
                <button class="filter-btn" data-cat="Bionics & Bio"><span class="dot" style="background: #00ffaa;"></span> BCI & Bio</button>
                <button class="filter-btn" data-cat="Continuum Fields"><span class="dot" style="background: #a5b4fc;"></span> 418 Continuum</button>
            </div>

            <!-- Action Controls & Theme Picker -->
            <div class="controls-group">
                <select id="theme-select" class="theme-selector" title="Select Theme Palette">
                    <option value="theme-cyber">⚡ Cyber Neon</option>
                    <option value="theme-solar">☀️ Solar Flare</option>
                    <option value="theme-cobalt">🌌 Deep Cobalt</option>
                    <option value="theme-matrix">🧬 Matrix Emerald</option>
                    <option value="theme-slate">⚪ Crisp Slate</option>
                </select>
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
            <div>🚀 <b>Controls:</b> Left-Click + Drag: Rotate | Scroll: Zoom | Right-Click: Pan | Click Star: Warp & Inspect</div>
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

        // Theme Palettes
        const THEMES = {{
            "theme-cyber": {{
                name: "Cyber Neon",
                catColors: {{
                    "Frontier Engines": 0x00f0ff,
                    "Business Strategy": 0xffd166,
                    "AI & QA": 0xd946ef,
                    "Defense & Aero": 0xff3366,
                    "Bionics & Bio": 0x00ffaa,
                    "Quantum & Energy": 0x38bdf8,
                    "Continuum Fields": 0xa5b4fc
                }},
                lineColor: 0x00f0ff,
                ambientColor: 0xffffff,
                pointColor1: 0x00f0ff,
                pointColor2: 0xffd166,
                fogColor: 0x060d1f
            }},
            "theme-solar": {{
                name: "Solar Flare",
                catColors: {{
                    "Frontier Engines": 0xfbbf24,
                    "Business Strategy": 0xf59e0b,
                    "AI & QA": 0xf43f5e,
                    "Defense & Aero": 0xe11d48,
                    "Bionics & Bio": 0xd97706,
                    "Quantum & Energy": 0xfef08a,
                    "Continuum Fields": 0xfde68a
                }},
                lineColor: 0xfbbf24,
                ambientColor: 0xfffbeb,
                pointColor1: 0xfbbf24,
                pointColor2: 0xf43f5e,
                fogColor: 0x1a0f05
            }},
            "theme-cobalt": {{
                name: "Deep Cobalt",
                catColors: {{
                    "Frontier Engines": 0x38bdf8,
                    "Business Strategy": 0x60a5fa,
                    "AI & QA": 0x818cf8,
                    "Defense & Aero": 0x3b82f6,
                    "Bionics & Bio": 0x06b6d4,
                    "Quantum & Energy": 0x93c5fd,
                    "Continuum Fields": 0xbfdbfe
                }},
                lineColor: 0x38bdf8,
                ambientColor: 0xf0f9ff,
                pointColor1: 0x38bdf8,
                pointColor2: 0x818cf8,
                fogColor: 0x040e26
            }},
            "theme-matrix": {{
                name: "Matrix Emerald",
                catColors: {{
                    "Frontier Engines": 0x00ffaa,
                    "Business Strategy": 0xa3e635,
                    "AI & QA": 0x10b981,
                    "Defense & Aero": 0x059669,
                    "Bionics & Bio": 0x34d399,
                    "Quantum & Energy": 0x6ee7b7,
                    "Continuum Fields": 0xa7f3d0
                }},
                lineColor: 0x00ffaa,
                ambientColor: 0xecfdf5,
                pointColor1: 0x00ffaa,
                pointColor2: 0xa3e635,
                fogColor: 0x03140b
            }},
            "theme-slate": {{
                name: "Crisp Slate",
                catColors: {{
                    "Frontier Engines": 0xffffff,
                    "Business Strategy": 0xf1f5f9,
                    "AI & QA": 0x38bdf8,
                    "Defense & Aero": 0xf43f5e,
                    "Bionics & Bio": 0x4ade80,
                    "Quantum & Energy": 0xe2e8f0,
                    "Continuum Fields": 0x94a3b8
                }},
                lineColor: 0xffffff,
                ambientColor: 0xffffff,
                pointColor1: 0xffffff,
                pointColor2: 0x38bdf8,
                fogColor: 0x0f172a
            }}
        }};

        let currentThemeKey = localStorage.getItem("starmap_theme") || "theme-cyber";
        let activeTheme = THEMES[currentThemeKey] || THEMES["theme-cyber"];

        const CLUSTER_CENTERS = {{
            "defense": {{ x: -140, y: 35, z: -80 }},
            "ai": {{ x: 0, y: 75, z: 0 }},
            "strategy": {{ x: 135, y: 45, z: 75 }},
            "bio": {{ x: -75, y: -65, z: 125 }},
            "quantum": {{ x: 95, y: -55, z: -105 }},
            "frontier": {{ x: -45, y: 25, z: -125 }},
            "continuum": {{ x: 0, y: -25, z: 0 }}
        }};

        // Web Audio Synthesizer
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
                gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
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
        scene.fog = new THREE.FogExp2(activeTheme.fogColor, 0.00025);

        const camera = new THREE.PerspectiveCamera(58, window.innerWidth / window.innerHeight, 0.1, 4000);
        camera.position.set(0, 160, 360);

        const renderer = new THREE.WebGLRenderer({{ canvas, antialias: true, alpha: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.maxDistance = 1100;
        controls.minDistance = 15;
        controls.autoRotate = true;
        controls.autoRotateSpeed = 0.35;

        // Lights
        const ambientLight = new THREE.AmbientLight(activeTheme.ambientColor, 1.4);
        scene.add(ambientLight);

        const pointLight1 = new THREE.PointLight(activeTheme.pointColor1, 2.0, 800);
        pointLight1.position.set(0, 100, 100);
        scene.add(pointLight1);

        const pointLight2 = new THREE.PointLight(activeTheme.pointColor2, 1.8, 800);
        pointLight2.position.set(120, -60, -100);
        scene.add(pointLight2);

        // Background Starfield
        const starGeo = new THREE.BufferGeometry();
        const starCount = 4000;
        const starPos = new Float32Array(starCount * 3);
        for (let i = 0; i < starCount * 3; i += 3) {{
            starPos[i] = (Math.random() - 0.5) * 2200;
            starPos[i+1] = (Math.random() - 0.5) * 2200;
            starPos[i+2] = (Math.random() - 0.5) * 2200;
        }}
        starGeo.setAttribute("position", new THREE.BufferAttribute(starPos, 3));
        const starMat = new THREE.PointsMaterial({{ color: 0xe2e8f0, size: 1.8, transparent: true, opacity: 0.75 }});
        const starPoints = new THREE.Points(starGeo, starMat);
        scene.add(starPoints);

        // Glowing Volumetric Nebula Gas Spheres
        const nebulaGroup = new THREE.Group();
        const nebulaMeshes = [];
        for (const [key, center] of Object.entries(CLUSTER_CENTERS)) {{
            const nebGeo = new THREE.SphereGeometry(45, 16, 16);
            const nebMat = new THREE.MeshBasicMaterial({{
                color: activeTheme.lineColor,
                wireframe: true,
                transparent: true,
                opacity: 0.08
            }});
            const nebMesh = new THREE.Mesh(nebGeo, nebMat);
            nebMesh.position.set(center.x, center.y, center.z);
            nebulaGroup.add(nebMesh);
            nebulaMeshes.push(nebMesh);
        }}
        scene.add(nebulaGroup);

        // 3D Text Billboards for Sector Labels
        function createTextSprite(text, colorHex) {{
            const canvas = document.createElement("canvas");
            canvas.width = 512;
            canvas.height = 128;
            const ctx = canvas.getContext("2d");
            ctx.fillStyle = "rgba(10, 20, 45, 0.8)";
            ctx.strokeStyle = colorHex;
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.roundRect(10, 10, 492, 108, 16);
            ctx.fill();
            ctx.stroke();

            ctx.font = "bold 34px 'Outfit', sans-serif";
            ctx.fillStyle = "#ffffff";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            ctx.shadowColor = colorHex;
            ctx.shadowBlur = 14;
            ctx.fillText(text, 256, 64);

            const texture = new THREE.CanvasTexture(canvas);
            const mat = new THREE.SpriteMaterial({{ map: texture, transparent: true, opacity: 0.95 }});
            const sprite = new THREE.Sprite(mat);
            sprite.scale.set(40, 10, 1);
            return sprite;
        }}

        const sectorLabels = [
            {{ name: "⚡ 70 FRONTIER ENGINES", pos: CLUSTER_CENTERS["frontier"], col: "#00f0ff" }},
            {{ name: "📈 BUSINESS & VALUATION", pos: CLUSTER_CENTERS["strategy"], col: "#ffd166" }},
            {{ name: "🤖 AI SWARMS & QA", pos: CLUSTER_CENTERS["ai"], col: "#d946ef" }},
            {{ name: "🛡️ DEFENSE & AERO", pos: CLUSTER_CENTERS["defense"], col: "#ff3366" }},
            {{ name: "🧬 BCI & INTERSPECIES", pos: CLUSTER_CENTERS["bio"], col: "#00ffaa" }},
            {{ name: "⚡ QUANTUM & SCADA", pos: CLUSTER_CENTERS["quantum"], col: "#38bdf8" }},
            {{ name: "📚 418 FIELD CONTINUUM", pos: {{ x: 0, y: -75, z: 0 }}, col: "#a5b4fc" }}
        ];

        sectorLabels.forEach(s => {{
            const lbl = createTextSprite(s.name, s.col);
            lbl.position.set(s.pos.x, s.pos.y + 40, s.pos.z);
            scene.add(lbl);
        }});

        // Node Mesh Representation
        const nodeMeshes = [];
        const nodeDataMap = new Map();
        const raycaster = new THREE.Raycaster();
        const mouse = new THREE.Vector2();

        // Glow Sprite Texture Generator
        function createGlowSprite(colorHex) {{
            const canvas = document.createElement("canvas");
            canvas.width = 128;
            canvas.height = 128;
            const ctx = canvas.getContext("2d");
            const grad = ctx.createRadialGradient(64, 64, 0, 64, 64, 64);
            grad.addColorStop(0, "#ffffff");
            grad.addColorStop(0.25, colorHex);
            grad.addColorStop(0.55, colorHex + "bb");
            grad.addColorStop(0.85, colorHex + "33");
            grad.addColorStop(1, "transparent");
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 128, 128);
            return new THREE.CanvasTexture(canvas);
        }}

        // Layout Nodes into Galaxy
        TOPICS.forEach((item, index) => {{
            const cluster = CLUSTER_CENTERS[item.cluster] || CLUSTER_CENTERS["continuum"];
            let pos;

            if (item.cluster === "continuum") {{
                const angle = index * 0.16;
                const radius = 65 + Math.sqrt(index) * 11.5;
                pos = new THREE.Vector3(
                    cluster.x + Math.cos(angle) * radius + (Math.random() - 0.5) * 22,
                    cluster.y + (Math.random() - 0.5) * 38,
                    cluster.z + Math.sin(angle) * radius + (Math.random() - 0.5) * 22
                );
            }} else {{
                const u = Math.random();
                const v = Math.random();
                const theta = u * 2.0 * Math.PI;
                const phi = Math.acos(2.0 * v - 1.0);
                const r = Math.cbrt(Math.random()) * 52;
                pos = new THREE.Vector3(
                    cluster.x + r * Math.sin(phi) * Math.cos(theta),
                    cluster.y + r * Math.sin(phi) * Math.sin(theta),
                    cluster.z + r * Math.cos(phi)
                );
            }}

            const colHex = activeTheme.catColors[item.category] || 0x00f0ff;
            const spriteMat = new THREE.SpriteMaterial({{
                map: createGlowSprite("#" + colHex.toString(16).padStart(6, '0')),
                color: 0xffffff,
                transparent: true,
                blending: THREE.AdditiveBlending
            }});

            const sprite = new THREE.Sprite(spriteMat);
            const scale = (item.size || 2.0) * 4.8;
            sprite.scale.set(scale, scale, 1);
            sprite.position.copy(pos);
            sprite.userData = item;

            scene.add(sprite);
            nodeMeshes.push(sprite);
            nodeDataMap.set(item.id, {{ mesh: sprite, data: item }});
        }});

        // Constellation Connecting Lines
        const lineMat = new THREE.LineBasicMaterial({{ color: activeTheme.lineColor, transparent: true, opacity: 0.3 }});
        const lineGeo = new THREE.BufferGeometry();
        const linePositions = [];
        for (let i = 0; i < nodeMeshes.length; i += 3) {{
            for (let j = i + 1; j < Math.min(i + 8, nodeMeshes.length); j++) {{
                if (nodeMeshes[i].userData.category === nodeMeshes[j].userData.category) {{
                    const p1 = nodeMeshes[i].position;
                    const p2 = nodeMeshes[j].position;
                    if (p1.distanceTo(p2) < 65) {{
                        linePositions.push(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z);
                    }}
                }}
            }}
        }}
        lineGeo.setAttribute("position", new THREE.Float32BufferAttribute(linePositions, 3));
        const linesMesh = new THREE.LineSegments(lineGeo, lineMat);
        scene.add(linesMesh);

        // Apply Theme Function
        function applyTheme(themeKey) {{
            const theme = THEMES[themeKey];
            if (!theme) return;
            currentThemeKey = themeKey;
            activeTheme = theme;
            localStorage.setItem("starmap_theme", themeKey);

            document.body.className = themeKey;
            scene.fog.color.setHex(theme.fogColor);
            ambientLight.color.setHex(theme.ambientColor);
            pointLight1.color.setHex(theme.pointColor1);
            pointLight2.color.setHex(theme.pointColor2);
            lineMat.color.setHex(theme.lineColor);

            nebulaMeshes.forEach(m => {{
                m.material.color.setHex(theme.lineColor);
            }});

            // Update all node sprite textures
            nodeMeshes.forEach(mesh => {{
                const colHex = theme.catColors[mesh.userData.category] || 0x00f0ff;
                mesh.material.map = createGlowSprite("#" + colHex.toString(16).padStart(6, '0'));
                mesh.material.needsUpdate = true;
            }});

            playChime(750, "triangle");
        }}

        // Theme Dropdown Listener
        const themeSelect = document.getElementById("theme-select");
        themeSelect.value = currentThemeKey;
        themeSelect.addEventListener("change", (e) => {{
            applyTheme(e.target.value);
        }});

        // UI Element References
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

        function showPanel(item) {{
            const colHex = "#" + (activeTheme.catColors[item.category] || 0x00f0ff).toString(16).padStart(6, '0');
            panelCat.textContent = item.category;
            panelCat.style.color = colHex;
            panelCat.style.borderColor = colHex;
            panelCat.style.background = colHex + "22";
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

        function flyToNode(mesh, targetDist = 42) {{
            controls.autoRotate = false;
            const targetPos = mesh.position.clone();
            const camTargetPos = targetPos.clone().add(new THREE.Vector3(0, 14, targetDist));

            playChime(660, "triangle");

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
                    const colHex = "#" + (activeTheme.catColors[hit.userData.category] || 0x00f0ff).toString(16).padStart(6, '0');
                    tooltipCat.textContent = hit.userData.category;
                    tooltipCat.style.color = colHex;
                    tooltipTitle.textContent = hit.userData.name;
                    tooltip.style.borderColor = colHex;
                    tooltip.style.display = "block";
                    playChime(850, "sine");
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
                playChime(500, "square");
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
    
    with open("/Users/alimalik/am-LLM/index.html", "w") as fp:
        fp.write(html_content)
    print("Wrote /Users/alimalik/am-LLM/index.html")

    with open("/Users/alimalik/tinkering/index.html", "w") as fp:
        fp.write(html_content)
    with open("/Users/alimalik/tinkering/docs/index.html", "w") as fp:
        fp.write(html_content)
    print("Wrote /Users/alimalik/tinkering/index.html and docs/index.html")
