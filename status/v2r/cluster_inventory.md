# V2R cluster inventory

2026-09-26T05:42:02.542331+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318782570496 available bytes; 82.22% used; 112476275 free inodes.

server1 `/home`: 318782570496 available bytes; 82.22% used; 112476275 free inodes.

server1 `/tmp`: 318782570496 available bytes; 82.22% used; 112476275 free inodes.

server1 `/var/tmp`: 318782570496 available bytes; 82.22% used; 112476275 free inodes.

server1 `/mnt/raid5`: 242160615424 available bytes; 98.89% used; 337540162 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22926966784 available bytes; 98.72% used; 110406217 free inodes.

server2 `/home`: 22926966784 available bytes; 98.72% used; 110406217 free inodes.

server2 `/tmp`: 22926966784 available bytes; 98.72% used; 110406217 free inodes.

server2 `/var/tmp`: 22926966784 available bytes; 98.72% used; 110406217 free inodes.

server2 `/mnt/raid5`: 276099989504 available bytes; 98.09% used; 445048304 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83210792960 available bytes; 95.36% used; 114149715 free inodes.

server3 `/home`: 83210792960 available bytes; 95.36% used; 114149715 free inodes.

server3 `/data`: 124336230400 available bytes; 98.28% used; 225824043 free inodes.

server3 `/tmp`: 83210792960 available bytes; 95.36% used; 114149715 free inodes.

server3 `/var/tmp`: 83210792960 available bytes; 95.36% used; 114149715 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094600192 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094600192 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106990821376 available bytes; 98.52% used; 224929134 free inodes.

server4 `/tmp`: 106094600192 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094600192 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
