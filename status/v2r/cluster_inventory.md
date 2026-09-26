# V2R cluster inventory

2026-09-26T05:27:23.949127+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318794657792 available bytes; 82.22% used; 112476291 free inodes.

server1 `/home`: 318794657792 available bytes; 82.22% used; 112476291 free inodes.

server1 `/tmp`: 318794657792 available bytes; 82.22% used; 112476291 free inodes.

server1 `/var/tmp`: 318794657792 available bytes; 82.22% used; 112476291 free inodes.

server1 `/mnt/raid5`: 278257614848 available bytes; 98.72% used; 337542007 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22920257536 available bytes; 98.72% used; 110406207 free inodes.

server2 `/home`: 22920257536 available bytes; 98.72% used; 110406207 free inodes.

server2 `/tmp`: 22920257536 available bytes; 98.72% used; 110406207 free inodes.

server2 `/var/tmp`: 22920257536 available bytes; 98.72% used; 110406207 free inodes.

server2 `/mnt/raid5`: 276593803264 available bytes; 98.09% used; 445048602 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84065624064 available bytes; 95.31% used; 114165910 free inodes.

server3 `/home`: 84065624064 available bytes; 95.31% used; 114165910 free inodes.

server3 `/data`: 124357509120 available bytes; 98.28% used; 225824798 free inodes.

server3 `/tmp`: 84065624064 available bytes; 95.31% used; 114165910 free inodes.

server3 `/var/tmp`: 84065624064 available bytes; 95.31% used; 114165910 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106095005696 available bytes; 94.08% used; 114348207 free inodes.

server4 `/home`: 106095005696 available bytes; 94.08% used; 114348207 free inodes.

server4 `/data`: 106991546368 available bytes; 98.52% used; 224929230 free inodes.

server4 `/tmp`: 106095005696 available bytes; 94.08% used; 114348207 free inodes.

server4 `/var/tmp`: 106095005696 available bytes; 94.08% used; 114348207 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
