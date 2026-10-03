import os
import json
import glob
import re

def build_catalog():
    topics = []

    # 1. AEGIS Flagship (AEGIS-AERO)
    topics.append({
        "id": "aegis_drone_defense",
        "name": "AEGIS Multi-Medium Drone Defense System",
        "category": "Defense & C-UAS",
        "folder": "tinkering/frontier_hybrids",
        "url": "https://github.com/am-LLM/tinkering/blob/main/frontier_hybrids/aegis_drone_defense_system.py",
        "desc": "Cost-asymmetric kinetic C-UAS/C-USV interceptor solving the $15k vs $2M missile dilemma with passive acoustic TDoA triangulation and 15-state ES-EKF optical flow.",
        "tags": ["C-UAS", "TDoA", "True Proportional Nav", "Defense", "EKF"],
        "size": 4.0,
        "cluster": "aegis_aero"
    })

    # 2. Frontier Engines (1-70) mapped to specific constellations
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
        # Constellation Classification Rules
        if any(w in lname for w in ["guardrail", "jailbreak", "thought", "cognitron", "llm_poison"]):
            if "poison" in lname or "scada" in lname:
                cluster = "cyber"
                cat = "Cyber & Post-Quantum"
            else:
                cluster = "cognitive_ai"
                cat = "Cognitive AI & SLMs"
        elif any(w in lname for w in ["bci", "rodent", "interspecies", "organ", "tcell", "dna", "crispr", "myoglobin", "pain", "sepsis", "calcium", "bionic", "tissue", "optogenetic"]):
            if "crispr" in lname:
                cluster = "veritas_qa"
                cat = "Formal QA & Compilers"
            else:
                cluster = "neuro_bio"
                cat = "BCI & Interspecies Bio"
        elif any(w in lname for w in ["scada", "crypto", "braid", "zk", "pqzk"]):
            cluster = "cyber"
            cat = "Cyber & Post-Quantum"
        elif any(w in lname for w in ["jump_diffusion", "circuit_breaker", "cbf", "frechet", "evt"]):
            cluster = "forecasting"
            cat = "Forecasting & Risk"
        elif any(w in lname for w in ["pruning", "compiler", "crystallizer", "causal"]):
            cluster = "veritas_qa"
            cat = "Formal QA & Compilers"
        elif any(w in lname for w in ["quantum", "cryocooler", "perovskite", "superconducting", "mram", "fluxon", "seebeck", "laser", "das", "power", "microgrid"]):
            cluster = "quantum_energy"
            cat = "Quantum & Energy"
        elif any(w in lname for w in ["drone", "hypersonic", "plasma", "sail", "radar", "sonar", "debris", "damper", "thruster", "ew", "traffic"]):
            cluster = "aegis_aero"
            cat = "Defense & C-UAS"
        else:
            cluster = "quantum_energy"
            cat = "Quantum & Energy"

        is_flagship = any(k in name for k in ["68", "69", "70", "67", "66", "55", "51", "04", "02", "01"])
        topics.append({
            "id": name,
            "name": clean_name,
            "category": cat,
            "folder": "tinkering/frontier_hybrids",
            "url": f"https://github.com/am-LLM/tinkering/blob/main/frontier_hybrids/{name}.py",
            "desc": desc,
            "tags": ["Frontier Engine", cat, "Python 3.14"],
            "size": 3.2 if is_flagship else 2.2,
            "cluster": cluster
        })

    # 3. Domain Laboratories
    domain_labs = [
        ("Aerospace GNC & Flight Dynamics", "aerospace_gnc", "15-state ES-EKF, ULA MVDR beamforming, Space Shuttle TMR FDIR, and Z3 formal proofs.", "Defense & C-UAS", "aegis_aero"),
        ("Acoustic & Seismic Metamaterials", "acoustic_seismic_metamaterials", "Westervelt non-linear acoustic fields and lithospheric rate-state friction.", "Quantum & Energy", "quantum_energy"),
        ("Advanced Quantum SCADA Tokamak", "advanced_quantum_scada", "Tokamak MHD equilibrium, QKD satellite links, and Modbus/DNP3 DPI firewalls.", "Cyber & Post-Quantum", "cyber"),
        ("Cyber Forensic & Post-Quantum Crypto", "cyber_forensic_crypto", "Hardened RISC-V gate model, tamper-evident Merkle blackbox, and BFT consensus.", "Cyber & Post-Quantum", "cyber"),
        ("Frugal Mechanics & Thermal Dynamics", "frugal_mechanics", "1D MOC water-hammer acoustic solver, Seebeck MPPT, and 2-RC ECM battery models.", "Quantum & Energy", "quantum_energy"),
        ("GeoSeismic InSAR Vision & Earthquake Forecasting", "geoseismic_insar_vision", "Satellite SAR interferometry, phase unwrapping, and subterranean fault mapping for seismic forecasting.", "Forecasting & Risk", "forecasting"),
        ("Isomorphic Physics & Side-Channel Guard", "isomorphic_hybrid", "Bidirectional state-space physics bridge and silicon DPA/CPA side-channel guards.", "Formal QA & Compilers", "veritas_qa"),
        ("NLP OSINT Knowledge DAG Engine", "nlp_osint_knowledge_dag", "Automated threat intelligence extraction, entity linking, and causal DAG reasoning.", "Sales, Marketing & Strategy", "sales_growth"),
        ("Pediatric Cognitive Systems", "pediatric_cognitive_systems", "Developmental neural networks, active inference child-cognition models.", "BCI & Interspecies Bio", "neuro_bio"),
        ("Frontier Quant Limit Order Book & High-Speed Finance", "frontier_quant_hybrids", "Zero-allocation C limit order book, jump-diffusion volatility, and microstructure risk models.", "Forecasting & Risk", "forecasting"),
    ]
    for title, folder, desc, cat, cluster in domain_labs:
        topics.append({
            "id": f"lab_{folder}",
            "name": title,
            "category": cat,
            "folder": f"tinkering/domain_laboratories/{folder}",
            "url": f"https://github.com/am-LLM/tinkering/tree/main/domain_laboratories/{folder}",
            "desc": desc,
            "tags": ["Domain Lab", cat, "Empirical Testbed"],
            "size": 3.4,
            "cluster": cluster
        })

    # 4. Sales, Marketing, Growth & Enterprise Business (GROWTH-CORE)
    sales_growth_topics = [
        ("Asymmetric Go-To-Market (GTM) Strategy & TAM Sizing", "Asymmetric market entry frameworks, bottom-up TAM/SAM/SOM market sizing, and pricing strategies.", ["GTM", "Market Sizing", "TAM/SAM", "Pricing"]),
        ("Product-Led Growth (PLG) & Behavioral Viral Loops", "Viral K-factor optimization, activation funnel engineering, and organic product adoption mechanics.", ["PLG", "Viral Loops", "Growth", "Retention"]),
        ("Customer Acquisition Unit Economics (LTV/CAC)", "LTV/CAC payback curves, gross margin optimization, cohort retention, and burn-multiple analysis.", ["LTV/CAC", "Unit Economics", "Payback Curves", "Finance"]),
        ("Competitive Intelligence & Supply-Chain OSINT", "Systematic open-source market intelligence, competitor vulnerability auditing, and supply-chain mapping.", ["OSINT", "Competitive Intel", "Supply Chain"]),
        ("Venture Capital Term Sheets & Governance", "Cap table modeling, liquidation preference analysis, vesting frameworks, and board governance.", ["Venture Capital", "Term Sheets", "Governance"]),
        ("Enterprise Risk, QHSE & ISO 22301 BCM", "Business Continuity Management, NIST SP 800-30 threat modeling, and crisis continuity architecture.", ["BCM", "ISO 22301", "NIST SP 800-30", "Risk"]),
    ]
    for i, (title, desc, tags) in enumerate(sales_growth_topics):
        topics.append({
            "id": f"growth_{i+1}",
            "name": title,
            "category": "Sales, Marketing & Strategy",
            "folder": "am-LLM/business_growth",
            "url": "https://github.com/am-LLM/am-LLM#1--business-strategy-market-analysis--growth",
            "desc": desc,
            "tags": tags,
            "size": 3.5,
            "cluster": "sales_growth"
        })

    # 5. Forecasting, Prediction & Quantitative Risk (ORACLE-NEXUS)
    forecasting_topics = [
        ("Quantitative DCF & Multi-Scenario Sensitivity Forecasting", "Discounted cash-flow forecasting, multi-variable Monte Carlo sensitivity matrices, and capital allocation.", ["DCF", "Sensitivity Modeling", "Forecasting", "Monte Carlo"]),
        ("Stochastic Jump-Diffusion & Volatility Prediction", "Merton jump-diffusion process, non-linear volatility smile estimation, and extreme regime-shift prediction.", ["Jump Diffusion", "Stochastic Calculus", "Volatility", "Prediction"]),
        ("Extreme Value Theory (EVT) & Fréchet Tail Forecasting", "Heavy-tailed risk modeling, generalized extreme value distributions, and black-swan tail-risk prediction.", ["EVT", "Frechet Bounds", "Tail Risk", "Time Series"]),
        ("Continuous Neural ODEs & Dynamic State Predictors", "Continuous-time normalizing flows and neural ordinary differential equations for irregular time-series forecasting.", ["Neural ODE", "Continuous Normalizing Flows", "Deep Learning", "Prediction"]),
        ("Multi-Agent Non-Cooperative Game Theory & Conflict Forecasting", "Game-theoretic payoff matrices, gray-zone escalation forecasting, and geopolitical risk mitigation.", ["Game Theory", "Geopolitics", "Conflict Forecasting"]),
    ]
    for i, (title, desc, tags) in enumerate(forecasting_topics):
        topics.append({
            "id": f"forecast_{i+1}",
            "name": title,
            "category": "Forecasting & Risk",
            "folder": "am-LLM/forecasting_and_risk",
            "url": "https://github.com/am-LLM/am-LLM#1--business-strategy-market-analysis--growth",
            "desc": desc,
            "tags": tags,
            "size": 3.5,
            "cluster": "forecasting"
        })

    # 6. Cognitive AI, SLMs & Guardrails (COGNITIVE-SYNTH)
    cognitive_ai_topics = [
        ("COGNITRON-1.58b Ternary SLM Architecture", "BitNet 1.58-bit ternary integer adds, MCTS test-time compute scaling, and active inference reasoning.", ["BitNet", "SLMs", "Active Inference", "Test-Time Compute"]),
        ("Representation Engineering (RepE) Task Jailbreak Defense", "Real-time subspace projection and activation clamping to neutralize adversarial attacks in latent space.", ["RepE", "Latent Steering", "Mechanistic Interpretability", "Guardrails"]),
        ("Sparse Autoencoders (SAE) Mechanistic Firewalls", "Overcomplete top-K dictionary decomposition for detecting and clamping malicious activation features.", ["SAE", "Mechanistic Interpretability", "Safety"]),
        ("Hierarchical Autonomous Multi-Agent Swarms", "Coordinator-Lead-Specialist autonomous agent topologies with formal contracts and reactive event loops.", ["Multi-Agent", "Swarms", "Agentic AI", "Orchestration"]),
        ("AI Model Evaluations & Latency-Budget Profiling", "Automated evaluation benchmarks, process reward models (PRM), and token-per-dollar optimization.", ["Model Evals", "Benchmarking", "Latency Optimization"]),
    ]
    for i, (title, desc, tags) in enumerate(cognitive_ai_topics):
        topics.append({
            "id": f"ai_synth_{i+1}",
            "name": title,
            "category": "Cognitive AI & SLMs",
            "folder": "am-LLM/cognitive_ai",
            "url": "https://github.com/am-LLM/am-LLM#2--ai-project-management--applied-engineering-leadership",
            "desc": desc,
            "tags": tags,
            "size": 3.5,
            "cluster": "cognitive_ai"
        })

    # 7. Zero-Trust QA & Formal Verification (VERITAS-QA)
    veritas_qa_topics = [
        ("Formal SMT (Z3) Mathematical Invariant Proofs", "Mathematical proof of state-space boundary invariants, safety barriers, and zero hallucination constraints.", ["Z3 Solver", "SMT", "Formal Verification", "Safety"]),
        ("100% Empirical Pass-Rate Automated Test Harnesses", "End-to-end automated test runner (verify_all.py) ensuring 100% test pass rate across 70 engines and laboratories.", ["QA", "Empirical Testing", "verify_all.py", "CI/CD"]),
        ("Property-Based Adversarial Fuzzing & Mutation Testing", "Hypothesis-based randomized stress testing, heavy-tailed boundary assertions, and code mutation scoring.", ["Property Testing", "Fuzzing", "Mutation Testing"]),
    ]
    for i, (title, desc, tags) in enumerate(veritas_qa_topics):
        topics.append({
            "id": f"qa_{i+1}",
            "name": title,
            "category": "Formal QA & Compilers",
            "folder": "am-LLM/quality_assurance",
            "url": "https://github.com/am-LLM/am-LLM#3--quality-assurance-qa-verification--reliability-engineering",
            "desc": desc,
            "tags": tags,
            "size": 3.5,
            "cluster": "veritas_qa"
        })

    # 8. Continuum Fields (418 Modules)
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
        .category-filters {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }}
        .filter-btn {{
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: var(--text-secondary);
            font-size: 0.76rem;
            font-weight: 700;
            padding: 6px 11px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 5px;
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
        <header class="header-bar">
            <div class="brand-title">
                <h1>⚡ ALI MALIK</h1>
                <span class="brand-badge">500+ RESEARCH TOPIC UNIVERSE</span>
            </div>

            <div class="search-container">
                <span class="search-icon">🔍</span>
                <input type="text" id="search-box" class="search-input" placeholder="Search any topic (e.g. Cyber, GTM, Forecasting, BCI)..." autocomplete="off">
                <div id="search-results" class="search-results"></div>
            </div>

            <div class="category-filters">
                <button class="filter-btn active" data-cat="all"><span class="dot" style="background: #ffffff;"></span> All Galaxy</button>
                <button class="filter-btn" data-cat="Cyber & Post-Quantum"><span class="dot" style="background: #a855f7;"></span> Cyber</button>
                <button class="filter-btn" data-cat="Sales, Marketing & Strategy"><span class="dot" style="background: #f59e0b;"></span> Sales & Marketing</button>
                <button class="filter-btn" data-cat="Forecasting & Risk"><span class="dot" style="background: #facc15;"></span> Forecasting</button>
                <button class="filter-btn" data-cat="Cognitive AI & SLMs"><span class="dot" style="background: #e879f9;"></span> Cognitive AI</button>
                <button class="filter-btn" data-cat="Defense & C-UAS"><span class="dot" style="background: #ff3366;"></span> Defense & C-UAS</button>
                <button class="filter-btn" data-cat="BCI & Interspecies Bio"><span class="dot" style="background: #00ffaa;"></span> BCI & Bio</button>
                <button class="filter-btn" data-cat="Formal QA & Compilers"><span class="dot" style="background: #ffffff;"></span> Formal QA</button>
                <button class="filter-btn" data-cat="Quantum & Energy"><span class="dot" style="background: #38bdf8;"></span> Quantum & Energy</button>
                <button class="filter-btn" data-cat="Continuum Fields"><span class="dot" style="background: #c4b5fd;"></span> 418 Continuum</button>
            </div>

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

        <aside id="side-panel" class="side-panel">
            <button id="panel-close-btn" class="panel-close">✕</button>
            <span id="panel-cat" class="panel-cat-badge">Domain Focus</span>
            <h2 id="panel-title" class="panel-title">Topic Title</h2>
            <div id="panel-folder" class="panel-folder">Repository Folder</div>
            <p id="panel-desc" class="panel-desc">Description text goes here.</p>
            <div id="panel-tags" class="panel-tags"></div>
            <a id="panel-link" href="#" target="_blank" class="panel-btn">
                <span>View Source on GitHub</span>
                <span>➔</span>
            </a>
        </aside>

        <div id="tooltip">
            <div id="tooltip-cat" class="t-cat">CATEGORY</div>
            <div id="tooltip-title" class="t-title">Star Title</div>
        </div>

        <footer class="footer-bar">
            <div>🚀 <b>Navigation:</b> Left-Click + Drag: Rotate | Scroll: Zoom | Right-Click: Pan | Click Star or Planet: Warp & Inspect</div>
            <div class="footer-links">
                <a href="https://github.com/am-LLM" target="_blank">GitHub Profile</a>
                <a href="https://github.com/am-LLM/tinkering" target="_blank">Tinkering Master Repo</a>
            </div>
        </footer>
    </div>

    <!-- Three.js, OrbitControls, Tween.js from CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tween.js/18.6.4/tween.umd.js"></script>

    <script>
        const TOPICS = {topics_json};

        const THEMES = {{
            "theme-cyber": {{
                catColors: {{
                    "Cyber & Post-Quantum": 0xa855f7,
                    "Sales, Marketing & Strategy": 0xf59e0b,
                    "Forecasting & Risk": 0xfacc15,
                    "Cognitive AI & SLMs": 0xe879f9,
                    "Defense & C-UAS": 0xff3366,
                    "BCI & Interspecies Bio": 0x00ffaa,
                    "Formal QA & Compilers": 0xffffff,
                    "Quantum & Energy": 0x38bdf8,
                    "Continuum Fields": 0xc4b5fd
                }},
                lineColor: 0x00f0ff,
                ambientColor: 0xffffff,
                pointColor1: 0x00f0ff,
                pointColor2: 0xffd166,
                fogColor: 0x060d1f
            }},
            "theme-solar": {{
                catColors: {{
                    "Cyber & Post-Quantum": 0xf43f5e,
                    "Sales, Marketing & Strategy": 0xfbbf24,
                    "Forecasting & Risk": 0xf59e0b,
                    "Cognitive AI & SLMs": 0xfb7185,
                    "Defense & C-UAS": 0xe11d48,
                    "BCI & Interspecies Bio": 0xd97706,
                    "Formal QA & Compilers": 0xffedd5,
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
                catColors: {{
                    "Cyber & Post-Quantum": 0x818cf8,
                    "Sales, Marketing & Strategy": 0x60a5fa,
                    "Forecasting & Risk": 0x38bdf8,
                    "Cognitive AI & SLMs": 0xa5b4fc,
                    "Defense & C-UAS": 0x3b82f6,
                    "BCI & Interspecies Bio": 0x06b6d4,
                    "Formal QA & Compilers": 0xe0f2fe,
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
                catColors: {{
                    "Cyber & Post-Quantum": 0x10b981,
                    "Sales, Marketing & Strategy": 0xa3e635,
                    "Forecasting & Risk": 0x84cc16,
                    "Cognitive AI & SLMs": 0x34d399,
                    "Defense & C-UAS": 0x059669,
                    "BCI & Interspecies Bio": 0x00ffaa,
                    "Formal QA & Compilers": 0xdcfce7,
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
                catColors: {{
                    "Cyber & Post-Quantum": 0xc084fc,
                    "Sales, Marketing & Strategy": 0xfbbf24,
                    "Forecasting & Risk": 0x38bdf8,
                    "Cognitive AI & SLMs": 0xf472b6,
                    "Defense & C-UAS": 0xf43f5e,
                    "BCI & Interspecies Bio": 0x4ade80,
                    "Formal QA & Compilers": 0xffffff,
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

        // The 8 Distinct Sector Focus Planets
        const SECTORS = {{
            "cyber": {{
                name: "🛡️ CYBER-VAULT: PQC & SCADA",
                pos: {{ x: -125, y: 45, z: -75 }},
                color: "#a855f7",
                hex: 0xa855f7,
                cat: "Cyber & Post-Quantum"
            }},
            "sales_growth": {{
                name: "💼 GROWTH-CORE: SALES & MARKETING",
                pos: {{ x: 135, y: 45, z: 65 }},
                color: "#f59e0b",
                hex: 0xf59e0b,
                cat: "Sales, Marketing & Strategy"
            }},
            "forecasting": {{
                name: "📈 ORACLE-NEXUS: FORECASTING & RISK",
                pos: {{ x: 115, y: -45, z: 95 }},
                color: "#facc15",
                hex: 0xfacc15,
                cat: "Forecasting & Risk"
            }},
            "cognitive_ai": {{
                name: "🧠 COGNITIVE-SYNTH: AI & SLMS",
                pos: {{ x: 0, y: 85, z: -20 }},
                color: "#e879f9",
                hex: 0xe879f9,
                cat: "Cognitive AI & SLMs"
            }},
            "aegis_aero": {{
                name: "🎯 AEGIS-AERO: DEFENSE & C-UAS",
                pos: {{ x: -125, y: -40, z: 75 }},
                color: "#ff3366",
                hex: 0xff3366,
                cat: "Defense & C-UAS"
            }},
            "neuro_bio": {{
                name: "🧬 NEURO-BIO: BCI & INTERSPECIES",
                pos: {{ x: 90, y: -50, z: -90 }},
                color: "#00ffaa",
                hex: 0x00ffaa,
                cat: "BCI & Interspecies Bio"
            }},
            "veritas_qa": {{
                name: "🔬 VERITAS-QA: FORMAL SMT & COMPILERS",
                pos: {{ x: -35, y: -55, z: -120 }},
                color: "#ffffff",
                hex: 0xffffff,
                cat: "Formal QA & Compilers"
            }},
            "quantum_energy": {{
                name: "⚡ QUANTUM-GRID: QUANTUM & ENERGY",
                pos: {{ x: -40, y: 45, z: 120 }},
                color: "#38bdf8",
                hex: 0x38bdf8,
                cat: "Quantum & Energy"
            }},
            "continuum": {{
                name: "📚 418 FIELD CONTINUUM",
                pos: {{ x: 0, y: -20, z: 0 }},
                color: "#c4b5fd",
                hex: 0xc4b5fd,
                cat: "Continuum Fields"
            }}
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

        const camera = new THREE.PerspectiveCamera(58, window.innerWidth / window.innerHeight, 0.1, 4500);
        camera.position.set(0, 160, 380);

        const renderer = new THREE.WebGLRenderer({{ canvas, antialias: true, alpha: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.maxDistance = 1200;
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
            starPos[i] = (Math.random() - 0.5) * 2500;
            starPos[i+1] = (Math.random() - 0.5) * 2500;
            starPos[i+2] = (Math.random() - 0.5) * 2500;
        }}
        starGeo.setAttribute("position", new THREE.BufferAttribute(starPos, 3));
        const starMat = new THREE.PointsMaterial({{ color: 0xe2e8f0, size: 1.8, transparent: true, opacity: 0.75 }});
        const starPoints = new THREE.Points(starGeo, starMat);
        scene.add(starPoints);

        // Unified Galaxy Root Group
        const galaxyGroup = new THREE.Group();
        scene.add(galaxyGroup);

        // 3D Text Billboard Generator
        function createTextSprite(text, colorHex) {{
            const canvas = document.createElement("canvas");
            canvas.width = 512;
            canvas.height = 128;
            const ctx = canvas.getContext("2d");
            ctx.fillStyle = "rgba(8, 16, 38, 0.88)";
            ctx.strokeStyle = colorHex;
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.roundRect(8, 8, 496, 112, 18);
            ctx.fill();
            ctx.stroke();

            ctx.font = "bold 32px 'Outfit', sans-serif";
            ctx.fillStyle = "#ffffff";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            ctx.shadowColor = colorHex;
            ctx.shadowBlur = 14;
            ctx.fillText(text, 256, 64);

            const texture = new THREE.CanvasTexture(canvas);
            const mat = new THREE.SpriteMaterial({{ map: texture, transparent: true, opacity: 0.96 }});
            const sprite = new THREE.Sprite(mat);
            sprite.scale.set(42, 10.5, 1);
            return sprite;
        }}

        // Glowing Star Texture Generator
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

        // Build Sector Focus Planets & Billboards
        const sectorPlanetMeshes = [];
        for (const [key, sector] of Object.entries(SECTORS)) {{
            const center = sector.pos;

            // 1. Sector Focus Planet Sphere
            const sphereGeo = new THREE.SphereGeometry(key === "continuum" ? 6 : 4.5, 24, 24);
            const sphereMat = new THREE.MeshStandardMaterial({{
                color: sector.hex,
                emissive: sector.hex,
                emissiveIntensity: 0.65,
                roughness: 0.2,
                metalness: 0.8
            }});
            const planetMesh = new THREE.Mesh(sphereGeo, sphereMat);
            planetMesh.position.set(center.x, center.y, center.z);
            planetMesh.userData = {{
                isPlanetFocus: true,
                name: sector.name,
                category: sector.cat,
                cluster: key,
                desc: `Central planetary anchor for ${{sector.name}}. Orbiting stars represent verified engineering engines, research papers, and models.`
            }};
            galaxyGroup.add(planetMesh);
            sectorPlanetMeshes.push(planetMesh);

            // 2. Orbital Rings
            const ringGeo = new THREE.RingGeometry(key === "continuum" ? 20 : 10, key === "continuum" ? 21.5 : 11.2, 32);
            const ringMat = new THREE.MeshBasicMaterial({{
                color: sector.hex,
                side: THREE.DoubleSide,
                transparent: true,
                opacity: 0.55
            }});
            const ringMesh = new THREE.Mesh(ringGeo, ringMat);
            ringMesh.position.set(center.x, center.y, center.z);
            ringMesh.rotation.x = Math.PI / 2.3;
            galaxyGroup.add(ringMesh);

            // 3. Volumetric Nebula Sphere
            const nebGeo = new THREE.SphereGeometry(key === "continuum" ? 68 : 42, 16, 16);
            const nebMat = new THREE.MeshBasicMaterial({{
                color: sector.hex,
                wireframe: true,
                transparent: true,
                opacity: 0.08
            }});
            const nebMesh = new THREE.Mesh(nebGeo, nebMat);
            nebMesh.position.set(center.x, center.y, center.z);
            galaxyGroup.add(nebMesh);

            // 4. Sector Title Billboard
            const billboard = createTextSprite(sector.name, sector.color);
            billboard.position.set(center.x, center.y + 24, center.z);
            galaxyGroup.add(billboard);
        }}

        // Layout Stars Around Their Exact Sector Focus Planet
        const nodeMeshes = [];
        const nodeDataMap = new Map();
        const raycaster = new THREE.Raycaster();
        const mouse = new THREE.Vector2();

        TOPICS.forEach((item, index) => {{
            const sector = SECTORS[item.cluster] || SECTORS["continuum"];
            const center = sector.pos;
            let pos;

            if (item.cluster === "continuum") {{
                const angle = index * 0.16;
                const radius = 26 + Math.sqrt(index) * 10.5;
                pos = new THREE.Vector3(
                    center.x + Math.cos(angle) * radius + (Math.random() - 0.5) * 16,
                    center.y + (Math.random() - 0.5) * 24,
                    center.z + Math.sin(angle) * radius + (Math.random() - 0.5) * 16
                );
            }} else {{
                const u = Math.random();
                const v = Math.random();
                const theta = u * 2.0 * Math.PI;
                const phi = Math.acos(2.0 * v - 1.0);
                const r = 10 + Math.cbrt(Math.random()) * 30;
                pos = new THREE.Vector3(
                    center.x + r * Math.sin(phi) * Math.cos(theta),
                    center.y + r * Math.sin(phi) * Math.sin(theta),
                    center.z + r * Math.cos(phi)
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
            const scale = (item.size || 2.0) * 4.6;
            sprite.scale.set(scale, scale, 1);
            sprite.position.copy(pos);
            sprite.userData = item;

            galaxyGroup.add(sprite);
            nodeMeshes.push(sprite);
            nodeDataMap.set(item.id, {{ mesh: sprite, data: item }});
        }});

        // Constellation Lines
        const lineMat = new THREE.LineBasicMaterial({{ color: activeTheme.lineColor, transparent: true, opacity: 0.28 }});
        const lineGeo = new THREE.BufferGeometry();
        const linePositions = [];
        for (let i = 0; i < nodeMeshes.length; i += 3) {{
            for (let j = i + 1; j < Math.min(i + 8, nodeMeshes.length); j++) {{
                if (nodeMeshes[i].userData.category === nodeMeshes[j].userData.category) {{
                    const p1 = nodeMeshes[i].position;
                    const p2 = nodeMeshes[j].position;
                    if (p1.distanceTo(p2) < 45) {{
                        linePositions.push(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z);
                    }}
                }}
            }}
        }}
        lineGeo.setAttribute("position", new THREE.Float32BufferAttribute(linePositions, 3));
        const linesMesh = new THREE.LineSegments(lineGeo, lineMat);
        galaxyGroup.add(linesMesh);

        // Theme Application
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

            nodeMeshes.forEach(mesh => {{
                const colHex = theme.catColors[mesh.userData.category] || 0x00f0ff;
                mesh.material.map = createGlowSprite("#" + colHex.toString(16).padStart(6, '0'));
                mesh.material.needsUpdate = true;
            }});

            playChime(750, "triangle");
        }}

        const themeSelect = document.getElementById("theme-select");
        themeSelect.value = currentThemeKey;
        themeSelect.addEventListener("change", (e) => {{
            applyTheme(e.target.value);
        }});

        // UI Panel & Interaction Handlers
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
            panelCat.textContent = item.category || "PLANETARY FOCUS";
            panelCat.style.color = colHex;
            panelCat.style.borderColor = colHex;
            panelCat.style.background = colHex + "22";
            panelTitle.textContent = item.name;
            panelFolder.textContent = item.folder || "am-LLM Master Index";
            panelDesc.textContent = item.desc;
            panelLink.href = item.url || "https://github.com/am-LLM/tinkering";

            panelTags.innerHTML = "";
            (item.tags || ["Planetary Focus", "Domain Constellation"]).forEach(tag => {{
                const t = document.createElement("span");
                t.className = "tag-pill";
                t.textContent = tag;
                panelTags.appendChild(t);
            }});

            sidePanel.classList.add("open");
        }}

        function flyToNode(mesh, targetDist = 38) {{
            controls.autoRotate = false;
            const targetPos = new THREE.Vector3();
            mesh.getWorldPosition(targetPos);
            const camTargetPos = targetPos.clone().add(new THREE.Vector3(0, 12, targetDist));

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

        window.addEventListener("resize", () => {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }});

        const interactiveObjects = [...nodeMeshes, ...sectorPlanetMeshes];

        window.addEventListener("mousemove", (e) => {{
            mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
            mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;

            tooltip.style.left = e.clientX + "px";
            tooltip.style.top = e.clientY + "px";

            raycaster.setFromCamera(mouse, camera);
            const intersects = raycaster.intersectObjects(interactiveObjects);

            if (intersects.length > 0) {{
                const hit = intersects[0].object;
                if (hoveredNode !== hit) {{
                    hoveredNode = hit;
                    const colHex = "#" + (activeTheme.catColors[hit.userData.category] || 0x00f0ff).toString(16).padStart(6, '0');
                    tooltipCat.textContent = hit.userData.category || "PLANETARY FOCUS";
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

        window.addEventListener("click", (e) => {{
            if (e.target.closest(".hud-layer") && !e.target.closest("#webgl-canvas")) return;
            raycaster.setFromCamera(mouse, camera);
            const intersects = raycaster.intersectObjects(interactiveObjects);
            if (intersects.length > 0) {{
                const target = intersects[0].object;
                flyToNode(target);
            }}
        }});

        document.getElementById("panel-close-btn").addEventListener("click", () => {{
            sidePanel.classList.remove("open");
            controls.autoRotate = true;
        }});

        document.getElementById("reset-cam-btn").addEventListener("click", () => {{
            sidePanel.classList.remove("open");
            controls.autoRotate = true;
            new TWEEN.Tween(camera.position).to({{ x: 0, y: 160, z: 380 }}, 1000).easing(TWEEN.Easing.Cubic.Out).start();
            new TWEEN.Tween(controls.target).to({{ x: 0, y: 0, z: 0 }}, 1000).easing(TWEEN.Easing.Cubic.Out).start();
        }});

        const audioBtn = document.getElementById("audio-toggle-btn");
        audioBtn.addEventListener("click", () => {{
            soundEnabled = !soundEnabled;
            audioBtn.textContent = soundEnabled ? "🔊 Sound" : "🔇 Muted";
        }});

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
            galaxyGroup.rotation.y += 0.0002;
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
