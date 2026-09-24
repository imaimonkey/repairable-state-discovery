# V2R cluster inventory

2026-09-24T23:23:45.137895+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319006380032 available bytes; 82.20% used; 112480773 free inodes.

server1 `/home`: 319006380032 available bytes; 82.20% used; 112480773 free inodes.

server1 `/tmp`: 319006380032 available bytes; 82.20% used; 112480773 free inodes.

server1 `/var/tmp`: 319006380032 available bytes; 82.20% used; 112480773 free inodes.

server1 `/mnt/raid5`: 415246950400 available bytes; 98.10% used; 337613961 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23118348288 available bytes; 98.71% used; 110410804 free inodes.

server2 `/home`: 23118348288 available bytes; 98.71% used; 110410804 free inodes.

server2 `/tmp`: 23118348288 available bytes; 98.71% used; 110410804 free inodes.

server2 `/var/tmp`: 23118348288 available bytes; 98.71% used; 110410804 free inodes.

server2 `/mnt/raid5`: 486335676416 available bytes; 96.64% used; 445151368 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84370202624 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84370202624 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148388401152 available bytes; 97.95% used; 225801036 free inodes.

server3 `/tmp`: 84370202624 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84370202624 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105799761920 available bytes; 94.10% used; 114348305 free inodes.

server4 `/home`: 105799761920 available bytes; 94.10% used; 114348305 free inodes.

server4 `/data`: 61443706880 available bytes; 99.15% used; 225156427 free inodes.

server4 `/tmp`: 105799761920 available bytes; 94.10% used; 114348305 free inodes.

server4 `/var/tmp`: 105799761920 available bytes; 94.10% used; 114348305 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
