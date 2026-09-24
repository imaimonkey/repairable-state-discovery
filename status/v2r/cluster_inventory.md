# V2R cluster inventory

2026-09-24T12:48:49.722081+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324039557120 available bytes; 81.92% used; 112481557 free inodes.

server1 `/home`: 324039557120 available bytes; 81.92% used; 112481557 free inodes.

server1 `/tmp`: 324039557120 available bytes; 81.92% used; 112481557 free inodes.

server1 `/var/tmp`: 324039557120 available bytes; 81.92% used; 112481557 free inodes.

server1 `/mnt/raid5`: 403360456704 available bytes; 98.15% used; 337680084 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57576640512 available bytes; 96.79% used; 110429145 free inodes.

server2 `/home`: 57576640512 available bytes; 96.79% used; 110429145 free inodes.

server2 `/tmp`: 57576640512 available bytes; 96.79% used; 110429145 free inodes.

server2 `/var/tmp`: 57576640512 available bytes; 96.79% used; 110429145 free inodes.

server2 `/mnt/raid5`: 507912212480 available bytes; 96.49% used; 445171091 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85686255616 available bytes; 95.22% used; 114197016 free inodes.

server3 `/home`: 85686255616 available bytes; 95.22% used; 114197016 free inodes.

server3 `/data`: 163112968192 available bytes; 97.75% used; 225814378 free inodes.

server3 `/tmp`: 85686255616 available bytes; 95.22% used; 114197016 free inodes.

server3 `/var/tmp`: 85686255616 available bytes; 95.22% used; 114197016 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105779884032 available bytes; 94.10% used; 114348780 free inodes.

server4 `/home`: 105779884032 available bytes; 94.10% used; 114348780 free inodes.

server4 `/data`: 90045898752 available bytes; 98.76% used; 225257228 free inodes.

server4 `/tmp`: 105779884032 available bytes; 94.10% used; 114348780 free inodes.

server4 `/var/tmp`: 105779884032 available bytes; 94.10% used; 114348780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
