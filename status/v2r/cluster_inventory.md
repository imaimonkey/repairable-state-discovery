# V2R cluster inventory

2026-09-23T23:42:32.994764+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325610303488 available bytes; 81.84% used; 112501190 free inodes.

server1 `/home`: 325610303488 available bytes; 81.84% used; 112501190 free inodes.

server1 `/tmp`: 325610303488 available bytes; 81.84% used; 112501190 free inodes.

server1 `/var/tmp`: 325610303488 available bytes; 81.84% used; 112501190 free inodes.

server1 `/mnt/raid5`: 1340966350848 available bytes; 93.85% used; 337735852 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41034731520 available bytes; 97.71% used; 110432515 free inodes.

server2 `/home`: 41034731520 available bytes; 97.71% used; 110432515 free inodes.

server2 `/tmp`: 41034731520 available bytes; 97.71% used; 110432515 free inodes.

server2 `/var/tmp`: 41034731520 available bytes; 97.71% used; 110432515 free inodes.

server2 `/mnt/raid5`: 533544873984 available bytes; 96.31% used; 445205065 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292491857920 available bytes; 83.68% used; 114191260 free inodes.

server3 `/home`: 292491857920 available bytes; 83.68% used; 114191260 free inodes.

server3 `/data`: 82295177216 available bytes; 98.86% used; 225845192 free inodes.

server3 `/tmp`: 292491857920 available bytes; 83.68% used; 114191260 free inodes.

server3 `/var/tmp`: 292491857920 available bytes; 83.68% used; 114191260 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106193100800 available bytes; 94.07% used; 114351912 free inodes.

server4 `/home`: 106193100800 available bytes; 94.07% used; 114351912 free inodes.

server4 `/data`: 292991913984 available bytes; 95.95% used; 225420236 free inodes.

server4 `/tmp`: 106193100800 available bytes; 94.07% used; 114351912 free inodes.

server4 `/var/tmp`: 106193100800 available bytes; 94.07% used; 114351912 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
