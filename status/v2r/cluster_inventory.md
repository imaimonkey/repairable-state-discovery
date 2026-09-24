# V2R cluster inventory

2026-09-24T01:40:36.322550+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325458788352 available bytes; 81.84% used; 112499489 free inodes.

server1 `/home`: 325458788352 available bytes; 81.84% used; 112499489 free inodes.

server1 `/tmp`: 325458788352 available bytes; 81.84% used; 112499489 free inodes.

server1 `/var/tmp`: 325458788352 available bytes; 81.84% used; 112499489 free inodes.

server1 `/mnt/raid5`: 853731012608 available bytes; 96.08% used; 337733889 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40936837120 available bytes; 97.72% used; 110431913 free inodes.

server2 `/home`: 40936837120 available bytes; 97.72% used; 110431913 free inodes.

server2 `/tmp`: 40936837120 available bytes; 97.72% used; 110431913 free inodes.

server2 `/var/tmp`: 40936837120 available bytes; 97.72% used; 110431913 free inodes.

server2 `/mnt/raid5`: 530465345536 available bytes; 96.33% used; 445201065 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292723724288 available bytes; 83.66% used; 114211239 free inodes.

server3 `/home`: 292723724288 available bytes; 83.66% used; 114211239 free inodes.

server3 `/data`: 71404515328 available bytes; 99.01% used; 225842057 free inodes.

server3 `/tmp`: 292723724288 available bytes; 83.66% used; 114211239 free inodes.

server3 `/var/tmp`: 292723724288 available bytes; 83.66% used; 114211239 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105955618816 available bytes; 94.09% used; 114348640 free inodes.

server4 `/home`: 105955618816 available bytes; 94.09% used; 114348640 free inodes.

server4 `/data`: 289771249664 available bytes; 96.00% used; 225388547 free inodes.

server4 `/tmp`: 105955618816 available bytes; 94.09% used; 114348640 free inodes.

server4 `/var/tmp`: 105955618816 available bytes; 94.09% used; 114348640 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
