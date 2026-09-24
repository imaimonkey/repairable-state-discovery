# V2R cluster inventory

2026-09-24T17:21:25.191253+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324006318080 available bytes; 81.92% used; 112481437 free inodes.

server1 `/home`: 324006318080 available bytes; 81.92% used; 112481437 free inodes.

server1 `/tmp`: 324006318080 available bytes; 81.92% used; 112481437 free inodes.

server1 `/var/tmp`: 324006318080 available bytes; 81.92% used; 112481437 free inodes.

server1 `/mnt/raid5`: 416461504512 available bytes; 98.09% used; 337647390 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57044434944 available bytes; 96.82% used; 110417781 free inodes.

server2 `/home`: 57044434944 available bytes; 96.82% used; 110417781 free inodes.

server2 `/tmp`: 57044434944 available bytes; 96.82% used; 110417781 free inodes.

server2 `/var/tmp`: 57044434944 available bytes; 96.82% used; 110417781 free inodes.

server2 `/mnt/raid5`: 499076767744 available bytes; 96.55% used; 445162972 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84408324096 available bytes; 95.29% used; 114156148 free inodes.

server3 `/home`: 84408324096 available bytes; 95.29% used; 114156148 free inodes.

server3 `/data`: 158996893696 available bytes; 97.80% used; 225786995 free inodes.

server3 `/tmp`: 84408324096 available bytes; 95.29% used; 114156148 free inodes.

server3 `/var/tmp`: 84408324096 available bytes; 95.29% used; 114156148 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105681780736 available bytes; 94.10% used; 114348569 free inodes.

server4 `/home`: 105681780736 available bytes; 94.10% used; 114348569 free inodes.

server4 `/data`: 88133062656 available bytes; 98.78% used; 225254356 free inodes.

server4 `/tmp`: 105681780736 available bytes; 94.10% used; 114348569 free inodes.

server4 `/var/tmp`: 105681780736 available bytes; 94.10% used; 114348569 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
