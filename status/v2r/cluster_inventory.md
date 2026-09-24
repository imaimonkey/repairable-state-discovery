# V2R cluster inventory

2026-09-24T20:46:35.515752+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323979919360 available bytes; 81.93% used; 112481427 free inodes.

server1 `/home`: 323979919360 available bytes; 81.93% used; 112481427 free inodes.

server1 `/tmp`: 323979919360 available bytes; 81.93% used; 112481427 free inodes.

server1 `/var/tmp`: 323979919360 available bytes; 81.93% used; 112481427 free inodes.

server1 `/mnt/raid5`: 415593537536 available bytes; 98.09% used; 337632528 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30153015296 available bytes; 98.32% used; 110411382 free inodes.

server2 `/home`: 30153015296 available bytes; 98.32% used; 110411382 free inodes.

server2 `/tmp`: 30153015296 available bytes; 98.32% used; 110411382 free inodes.

server2 `/var/tmp`: 30153015296 available bytes; 98.32% used; 110411382 free inodes.

server2 `/mnt/raid5`: 491766026240 available bytes; 96.60% used; 445156580 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84386066432 available bytes; 95.29% used; 114156102 free inodes.

server3 `/home`: 84386066432 available bytes; 95.29% used; 114156102 free inodes.

server3 `/data`: 151179718656 available bytes; 97.91% used; 225804016 free inodes.

server3 `/tmp`: 84386066432 available bytes; 95.29% used; 114156102 free inodes.

server3 `/var/tmp`: 84386066432 available bytes; 95.29% used; 114156102 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639669760 available bytes; 94.10% used; 114348379 free inodes.

server4 `/home`: 105639669760 available bytes; 94.10% used; 114348379 free inodes.

server4 `/data`: 81177014272 available bytes; 98.88% used; 225256427 free inodes.

server4 `/tmp`: 105639669760 available bytes; 94.10% used; 114348379 free inodes.

server4 `/var/tmp`: 105639669760 available bytes; 94.10% used; 114348379 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
