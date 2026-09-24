# V2R cluster inventory

2026-09-24T00:55:10.039950+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325529190400 available bytes; 81.84% used; 112500325 free inodes.

server1 `/home`: 325529190400 available bytes; 81.84% used; 112500325 free inodes.

server1 `/tmp`: 325529190400 available bytes; 81.84% used; 112500325 free inodes.

server1 `/var/tmp`: 325529190400 available bytes; 81.84% used; 112500325 free inodes.

server1 `/mnt/raid5`: 1040277843968 available bytes; 95.23% used; 337734843 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40979902464 available bytes; 97.71% used; 110432241 free inodes.

server2 `/home`: 40979902464 available bytes; 97.71% used; 110432241 free inodes.

server2 `/tmp`: 40979902464 available bytes; 97.71% used; 110432241 free inodes.

server2 `/var/tmp`: 40979902464 available bytes; 97.71% used; 110432241 free inodes.

server2 `/mnt/raid5`: 532013080576 available bytes; 96.32% used; 445202540 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292345647104 available bytes; 83.69% used; 114189060 free inodes.

server3 `/home`: 292345647104 available bytes; 83.69% used; 114189060 free inodes.

server3 `/data`: 82160914432 available bytes; 98.86% used; 225843370 free inodes.

server3 `/tmp`: 292345647104 available bytes; 83.69% used; 114189060 free inodes.

server3 `/var/tmp`: 292345647104 available bytes; 83.69% used; 114189060 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106028978176 available bytes; 94.08% used; 114349677 free inodes.

server4 `/home`: 106028978176 available bytes; 94.08% used; 114349677 free inodes.

server4 `/data`: 292876582912 available bytes; 95.95% used; 225414551 free inodes.

server4 `/tmp`: 106028978176 available bytes; 94.08% used; 114349677 free inodes.

server4 `/var/tmp`: 106028978176 available bytes; 94.08% used; 114349677 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
