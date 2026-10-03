#!/usr/bin/env python3
"""
CCNP Enterprise: Deterministic BGP Best-Path Selection Algorithm Simulator
Evaluates routes based on standard Cisco BGP decision hierarchy.
"""

class BGPRoute:
    def __init__(self, prefix: str, weight: int, local_pref: int, as_path_len: int, med: int, is_ebgp: bool):
        self.prefix = prefix
        self.weight = weight
        self.local_pref = local_pref
        self.as_path_len = as_path_len
        self.med = med
        self.is_ebgp = is_ebgp

def select_best_path(routes: list) -> BGPRoute:
    # 1. Highest Weight -> 2. Highest Local Pref -> 3. Shortest AS Path -> 4. Lowest MED -> 5. eBGP over iBGP
    return max(routes, key=lambda r: (r.weight, r.local_pref, -r.as_path_len, -r.med, int(r.is_ebgp)))

if __name__ == "__main__":
    candidates = [
        BGPRoute("10.0.0.0/24", weight=0, local_pref=100, as_path_len=3, med=50, is_ebgp=True),
        BGPRoute("10.0.0.0/24", weight=100, local_pref=100, as_path_len=4, med=100, is_ebgp=False),
        BGPRoute("10.0.0.0/24", weight=0, local_pref=200, as_path_len=2, med=10, is_ebgp=True)
    ]
    best = select_best_path(candidates)
    print(f"[*] Best BGP Path Selected: Weight={best.weight}, LocalPref={best.local_pref}, AS-Len={best.as_path_len}")
