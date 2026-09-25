# V2R cluster inventory

2026-09-25T11:42:13.850648+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319061774336 available bytes; 82.20% used; 112478824 free inodes.

server1 `/home`: 319061774336 available bytes; 82.20% used; 112478824 free inodes.

server1 `/tmp`: 319061774336 available bytes; 82.20% used; 112478824 free inodes.

server1 `/var/tmp`: 319061774336 available bytes; 82.20% used; 112478824 free inodes.

server1 `/mnt/raid5`: 364356456448 available bytes; 98.33% used; 337549191 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22906044416 available bytes; 98.72% used; 110409985 free inodes.

server2 `/home`: 22906044416 available bytes; 98.72% used; 110409985 free inodes.

server2 `/tmp`: 22906044416 available bytes; 98.72% used; 110409985 free inodes.

server2 `/var/tmp`: 22906044416 available bytes; 98.72% used; 110409985 free inodes.

server2 `/mnt/raid5`: 327024168960 available bytes; 97.74% used; 445083114 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84214018048 available bytes; 95.30% used; 114154994 free inodes.

server3 `/home`: 84214018048 available bytes; 95.30% used; 114154994 free inodes.

server3 `/data`: 142115459072 available bytes; 98.04% used; 225813472 free inodes.

server3 `/tmp`: 84214018048 available bytes; 95.30% used; 114154994 free inodes.

server3 `/var/tmp`: 84214018048 available bytes; 95.30% used; 114154994 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105602805760 available bytes; 94.11% used; 114350248 free inodes.

server4 `/home`: 105602805760 available bytes; 94.11% used; 114350248 free inodes.

server4 `/data`: 233346781184 available bytes; 96.78% used; 224976051 free inodes.

server4 `/tmp`: 105602805760 available bytes; 94.11% used; 114350248 free inodes.

server4 `/var/tmp`: 105602805760 available bytes; 94.11% used; 114350248 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
