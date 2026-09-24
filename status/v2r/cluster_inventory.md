# V2R cluster inventory

2026-09-24T10:00:13.186278+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324428288000 available bytes; 81.90% used; 112489541 free inodes.

server1 `/home`: 324428288000 available bytes; 81.90% used; 112489541 free inodes.

server1 `/tmp`: 324428288000 available bytes; 81.90% used; 112489541 free inodes.

server1 `/var/tmp`: 324428288000 available bytes; 81.90% used; 112489541 free inodes.

server1 `/mnt/raid5`: 500704759808 available bytes; 97.70% used; 337701353 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57755041792 available bytes; 96.78% used; 110430740 free inodes.

server2 `/home`: 57755041792 available bytes; 96.78% used; 110430740 free inodes.

server2 `/tmp`: 57755041792 available bytes; 96.78% used; 110430740 free inodes.

server2 `/var/tmp`: 57755041792 available bytes; 96.78% used; 110430740 free inodes.

server2 `/mnt/raid5`: 513656397824 available bytes; 96.45% used; 445176762 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 85317120000 available bytes; 95.24% used; 114170633 free inodes.

server3 `/home`: 85317120000 available bytes; 95.24% used; 114170633 free inodes.

server3 `/data`: 164501684224 available bytes; 97.73% used; 225819272 free inodes.

server3 `/tmp`: 85317120000 available bytes; 95.24% used; 114170633 free inodes.

server3 `/var/tmp`: 85317120000 available bytes; 95.24% used; 114170633 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105748115456 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105748115456 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154568069120 available bytes; 97.86% used; 225273210 free inodes.

server4 `/tmp`: 105748115456 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105748115456 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
