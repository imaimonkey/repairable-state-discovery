# V2R cluster inventory

2026-09-26T02:28:46.900864+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318418862080 available bytes; 82.24% used; 112476277 free inodes.

server1 `/home`: 318418862080 available bytes; 82.24% used; 112476277 free inodes.

server1 `/tmp`: 318418862080 available bytes; 82.24% used; 112476277 free inodes.

server1 `/var/tmp`: 318418862080 available bytes; 82.24% used; 112476277 free inodes.

server1 `/mnt/raid5`: 344973791232 available bytes; 98.42% used; 337546162 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22942904320 available bytes; 98.72% used; 110406220 free inodes.

server2 `/home`: 22942904320 available bytes; 98.72% used; 110406220 free inodes.

server2 `/tmp`: 22942904320 available bytes; 98.72% used; 110406220 free inodes.

server2 `/var/tmp`: 22942904320 available bytes; 98.72% used; 110406220 free inodes.

server2 `/mnt/raid5`: 288491888640 available bytes; 98.01% used; 445054433 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84317700096 available bytes; 95.29% used; 114152372 free inodes.

server3 `/home`: 84317700096 available bytes; 95.29% used; 114152372 free inodes.

server3 `/data`: 124785340416 available bytes; 98.28% used; 225817023 free inodes.

server3 `/tmp`: 84317700096 available bytes; 95.29% used; 114152372 free inodes.

server3 `/var/tmp`: 84317700096 available bytes; 95.29% used; 114152372 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106126725120 available bytes; 94.08% used; 114349422 free inodes.

server4 `/home`: 106126725120 available bytes; 94.08% used; 114349422 free inodes.

server4 `/data`: 130847248384 available bytes; 98.19% used; 224915701 free inodes.

server4 `/tmp`: 106126725120 available bytes; 94.08% used; 114349422 free inodes.

server4 `/var/tmp`: 106126725120 available bytes; 94.08% used; 114349422 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
