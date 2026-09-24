# V2R cluster inventory

2026-09-24T00:54:08.080248+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325530849280 available bytes; 81.84% used; 112500340 free inodes.

server1 `/home`: 325530849280 available bytes; 81.84% used; 112500340 free inodes.

server1 `/tmp`: 325530849280 available bytes; 81.84% used; 112500340 free inodes.

server1 `/var/tmp`: 325530849280 available bytes; 81.84% used; 112500340 free inodes.

server1 `/mnt/raid5`: 1044306505728 available bytes; 95.21% used; 337734873 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40980697088 available bytes; 97.71% used; 110432247 free inodes.

server2 `/home`: 40980697088 available bytes; 97.71% used; 110432247 free inodes.

server2 `/tmp`: 40980697088 available bytes; 97.71% used; 110432247 free inodes.

server2 `/var/tmp`: 40980697088 available bytes; 97.71% used; 110432247 free inodes.

server2 `/mnt/raid5`: 532046680064 available bytes; 96.32% used; 445202600 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292346679296 available bytes; 83.69% used; 114189062 free inodes.

server3 `/home`: 292346679296 available bytes; 83.69% used; 114189062 free inodes.

server3 `/data`: 82164678656 available bytes; 98.86% used; 225843390 free inodes.

server3 `/tmp`: 292346679296 available bytes; 83.69% used; 114189062 free inodes.

server3 `/var/tmp`: 292346679296 available bytes; 83.69% used; 114189062 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106030538752 available bytes; 94.08% used; 114349701 free inodes.

server4 `/home`: 106030538752 available bytes; 94.08% used; 114349701 free inodes.

server4 `/data`: 292878180352 available bytes; 95.95% used; 225414558 free inodes.

server4 `/tmp`: 106030538752 available bytes; 94.08% used; 114349701 free inodes.

server4 `/var/tmp`: 106030538752 available bytes; 94.08% used; 114349701 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
