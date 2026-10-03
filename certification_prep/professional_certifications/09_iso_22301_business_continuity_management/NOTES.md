# ISO 22301:2019 Business Continuity Management Systems (BCMS)

## 1. Business Impact Analysis (BIA) Lifecycle & Core Metrics

```
                     DISRUPTION TIMELINE & RECOVERY TARGETS
 Normal State      Disruption Occurs                Disaster Declared       RTO Reached
 ────┬─────────────────────X────────────────────────────────┼────────────────────┬────► Time
     │                     │                                │                    │
     │<── RPO (Data Loss) ─┤                                │                    │
     │    (Backup Window)  │                                │<── RTO (Downtime) ─┤
     │                     │                                                     │
     │                     │<───────────── Maximum Tolerable Downtime (MTD) ─────┤
```

### Critical Parameter Definitions:
1. **Maximum Tolerable Period of Disruption ($MTPD$ / $MTD$)**:
   The maximum time a business process can remain disrupted before irreversible existential damage occurs.
2. **Recovery Time Objective ($RTO$)**:
   Target time to restore disrupted activities and services ($RTO \le MTPD$).
3. **Recovery Point Objective ($RPO$)**:
   The maximum allowable data loss period expressed in units of time ($RPO \le \text{Data Backup Interval}$).
4. **Minimum Business Continuity Objective ($MBCO$)**:
   The minimum level of services or products that is acceptable to the organization to achieve its business objectives during a disruption.
