# V2R cluster inventory

2026-09-24T10:06:32.569724+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324424372224 available bytes; 81.90% used; 112489468 free inodes.

server1 `/home`: 324424372224 available bytes; 81.90% used; 112489468 free inodes.

server1 `/tmp`: 324424372224 available bytes; 81.90% used; 112489468 free inodes.

server1 `/var/tmp`: 324424372224 available bytes; 81.90% used; 112489468 free inodes.

server1 `/mnt/raid5`: 500682375168 available bytes; 97.70% used; 337700607 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57747111936 available bytes; 96.78% used; 110430723 free inodes.

server2 `/home`: 57747111936 available bytes; 96.78% used; 110430723 free inodes.

server2 `/tmp`: 57747111936 available bytes; 96.78% used; 110430723 free inodes.

server2 `/var/tmp`: 57747111936 available bytes; 96.78% used; 110430723 free inodes.

server2 `/mnt/raid5`: 513464119296 available bytes; 96.45% used; 445176665 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85380415488 available bytes; 95.24% used; 114173520 free inodes.

server3 `/home`: 85380415488 available bytes; 95.24% used; 114173520 free inodes.

server3 `/data`: 155028017152 available bytes; 97.86% used; 225819147 free inodes.

server3 `/tmp`: 85380415488 available bytes; 95.24% used; 114173520 free inodes.

server3 `/var/tmp`: 85380415488 available bytes; 95.24% used; 114173520 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747582976 available bytes; 94.10% used; 114349001 free inodes.

server4 `/home`: 105747582976 available bytes; 94.10% used; 114349001 free inodes.

server4 `/data`: 153505660928 available bytes; 97.88% used; 225258639 free inodes.

server4 `/tmp`: 105747582976 available bytes; 94.10% used; 114349001 free inodes.

server4 `/var/tmp`: 105747582976 available bytes; 94.10% used; 114349001 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
