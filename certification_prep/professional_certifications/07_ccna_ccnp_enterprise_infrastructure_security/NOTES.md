# CCNA & CCNP Enterprise Core & Advanced Routing Notes
**Author**: Ali Malik (`@am-LLM`)  
**Scope**: Cisco 350-401 ENCOR, 300-410 ENARSI. BGP Path Selection, OSPF LSAs, and Network Automation.

---

## 1. BGP Path Selection Algorithm Hierarchy (We Love Oranges As Oranges Mean Pure Refreshment)

1. **Weight** (Cisco proprietary, highest wins, local to router).
2. **Local Preference** (Highest wins, advertised across iBGP).
3. **Originate** (Locally injected routes via `network` or `aggregate-address`).
4. **AS-Path Length** (Shortest path wins).
5. **Origin Code** (`IGP` < `EGP` < `Incomplete ?`).
6. **MED (Multi-Exit Discriminator)** (Lowest wins, advertised between eBGP peers).
7. **eBGP over iBGP** (eBGP preferred).
8. **Router ID** (Lowest BGP Router ID wins).
