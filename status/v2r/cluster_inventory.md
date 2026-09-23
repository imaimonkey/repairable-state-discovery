# V2R cluster inventory

2026-09-23T23:36:48.711312+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325614186496 available bytes; 81.84% used; 112501246 free inodes.

server1 `/home`: 325614186496 available bytes; 81.84% used; 112501246 free inodes.

server1 `/tmp`: 325614186496 available bytes; 81.84% used; 112501246 free inodes.

server1 `/var/tmp`: 325614186496 available bytes; 81.84% used; 112501246 free inodes.

server1 `/mnt/raid5`: 1365073694720 available bytes; 93.74% used; 337736108 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41034354688 available bytes; 97.71% used; 110432543 free inodes.

server2 `/home`: 41034354688 available bytes; 97.71% used; 110432543 free inodes.

server2 `/tmp`: 41034354688 available bytes; 97.71% used; 110432543 free inodes.

server2 `/var/tmp`: 41034354688 available bytes; 97.71% used; 110432543 free inodes.

server2 `/mnt/raid5`: 534240534528 available bytes; 96.31% used; 445204995 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292841762816 available bytes; 83.66% used; 114214312 free inodes.

server3 `/home`: 292841762816 available bytes; 83.66% used; 114214312 free inodes.

server3 `/data`: 82307387392 available bytes; 98.86% used; 225845633 free inodes.

server3 `/tmp`: 292841762816 available bytes; 83.66% used; 114214312 free inodes.

server3 `/var/tmp`: 292841762816 available bytes; 83.66% used; 114214312 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106205822976 available bytes; 94.07% used; 114352119 free inodes.

server4 `/home`: 106205822976 available bytes; 94.07% used; 114352119 free inodes.

server4 `/data`: 293020434432 available bytes; 95.95% used; 225421874 free inodes.

server4 `/tmp`: 106205822976 available bytes; 94.07% used; 114352119 free inodes.

server4 `/var/tmp`: 106205822976 available bytes; 94.07% used; 114352119 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
