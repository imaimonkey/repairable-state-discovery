# V2R cluster inventory

2026-09-25T19:04:44.476832+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318728376320 available bytes; 82.22% used; 112476332 free inodes.

server1 `/home`: 318728376320 available bytes; 82.22% used; 112476332 free inodes.

server1 `/tmp`: 318728376320 available bytes; 82.22% used; 112476332 free inodes.

server1 `/var/tmp`: 318728376320 available bytes; 82.22% used; 112476332 free inodes.

server1 `/mnt/raid5`: 371005239296 available bytes; 98.30% used; 337540930 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23104352256 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23104352256 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23104352256 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23104352256 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 312801120256 available bytes; 97.84% used; 445065247 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84384083968 available bytes; 95.29% used; 114152623 free inodes.

server3 `/home`: 84384083968 available bytes; 95.29% used; 114152623 free inodes.

server3 `/data`: 131365134336 available bytes; 98.18% used; 225809033 free inodes.

server3 `/tmp`: 84384083968 available bytes; 95.29% used; 114152623 free inodes.

server3 `/var/tmp`: 84384083968 available bytes; 95.29% used; 114152623 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105606434816 available bytes; 94.11% used; 114349594 free inodes.

server4 `/home`: 105606434816 available bytes; 94.11% used; 114349594 free inodes.

server4 `/data`: 229675057152 available bytes; 96.83% used; 224931232 free inodes.

server4 `/tmp`: 105606434816 available bytes; 94.11% used; 114349594 free inodes.

server4 `/var/tmp`: 105606434816 available bytes; 94.11% used; 114349594 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
