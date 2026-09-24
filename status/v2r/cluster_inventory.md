# V2R cluster inventory

2026-09-24T01:45:13.421099+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325455687680 available bytes; 81.84% used; 112499467 free inodes.

server1 `/home`: 325455687680 available bytes; 81.84% used; 112499467 free inodes.

server1 `/tmp`: 325455687680 available bytes; 81.84% used; 112499467 free inodes.

server1 `/var/tmp`: 325455687680 available bytes; 81.84% used; 112499467 free inodes.

server1 `/mnt/raid5`: 834470449152 available bytes; 96.17% used; 337733827 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40933756928 available bytes; 97.72% used; 110431875 free inodes.

server2 `/home`: 40933756928 available bytes; 97.72% used; 110431875 free inodes.

server2 `/tmp`: 40933756928 available bytes; 97.72% used; 110431875 free inodes.

server2 `/var/tmp`: 40933756928 available bytes; 97.72% used; 110431875 free inodes.

server2 `/mnt/raid5`: 530339794944 available bytes; 96.34% used; 445201004 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292672921600 available bytes; 83.67% used; 114210143 free inodes.

server3 `/home`: 292672921600 available bytes; 83.67% used; 114210143 free inodes.

server3 `/data`: 71396077568 available bytes; 99.01% used; 225841984 free inodes.

server3 `/tmp`: 292672921600 available bytes; 83.67% used; 114210143 free inodes.

server3 `/var/tmp`: 292672921600 available bytes; 83.67% used; 114210143 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105952940032 available bytes; 94.09% used; 114348600 free inodes.

server4 `/home`: 105952940032 available bytes; 94.09% used; 114348600 free inodes.

server4 `/data`: 289764069376 available bytes; 96.00% used; 225388487 free inodes.

server4 `/tmp`: 105952940032 available bytes; 94.09% used; 114348600 free inodes.

server4 `/var/tmp`: 105952940032 available bytes; 94.09% used; 114348600 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
