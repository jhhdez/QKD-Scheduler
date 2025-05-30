This repo contains the code developed for allocation and scheduling of QKD transceivers in a switched-QKD network.

Given a traffic matrix of key demands between adjacent network nodes, a Mixed Integer Linear Programming approach is used to compute the necessary QKD transceivers at each node and a free-conflict scheduling

Files in this repo:
1. MBS (MILP-based Scheduler, higher runtime, best solution, impractical when network size increase).
2. ADS_rMBS (Allocation-Driven w/ relaxed MILP-based Scheduler, lower runtime than MBS, worse than MBS regarding the solution, practical when network size increase).
3. ADS_RRR (Allocation-Driven w/ relaxed Round Robin Scheduler, the fastest, worse than MBS and ADS_rMBS regarding the solution, practical when network size increase).
