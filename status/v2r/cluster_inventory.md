# V2R cluster inventory

2026-09-26T04:00:23.552621+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318416846848 available bytes; 82.24% used; 112476270 free inodes.

server1 `/home`: 318416846848 available bytes; 82.24% used; 112476270 free inodes.

server1 `/tmp`: 318416846848 available bytes; 82.24% used; 112476270 free inodes.

server1 `/var/tmp`: 318416846848 available bytes; 82.24% used; 112476270 free inodes.

server1 `/mnt/raid5`: 330953682944 available bytes; 98.48% used; 337545665 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22931800064 available bytes; 98.72% used; 110406198 free inodes.

server2 `/home`: 22931800064 available bytes; 98.72% used; 110406198 free inodes.

server2 `/tmp`: 22931800064 available bytes; 98.72% used; 110406198 free inodes.

server2 `/var/tmp`: 22931800064 available bytes; 98.72% used; 110406198 free inodes.

server2 `/mnt/raid5`: 286341726208 available bytes; 98.02% used; 445051511 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84525793280 available bytes; 95.28% used; 114173539 free inodes.

server3 `/home`: 84525793280 available bytes; 95.28% used; 114173539 free inodes.

server3 `/data`: 124589899776 available bytes; 98.28% used; 225820106 free inodes.

server3 `/tmp`: 84525793280 available bytes; 95.28% used; 114173539 free inodes.

server3 `/var/tmp`: 84525793280 available bytes; 95.28% used; 114173539 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105850974208 available bytes; 94.09% used; 114347414 free inodes.

server4 `/home`: 105850974208 available bytes; 94.09% used; 114347414 free inodes.

server4 `/data`: 109755510784 available bytes; 98.48% used; 224929441 free inodes.

server4 `/tmp`: 105850974208 available bytes; 94.09% used; 114347414 free inodes.

server4 `/var/tmp`: 105850974208 available bytes; 94.09% used; 114347414 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
