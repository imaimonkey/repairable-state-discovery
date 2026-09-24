# V2R cluster inventory

2026-09-24T22:22:16.709007+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323946221568 available bytes; 81.93% used; 112481411 free inodes.

server1 `/home`: 323946221568 available bytes; 81.93% used; 112481411 free inodes.

server1 `/tmp`: 323946221568 available bytes; 81.93% used; 112481411 free inodes.

server1 `/var/tmp`: 323946221568 available bytes; 81.93% used; 112481411 free inodes.

server1 `/mnt/raid5`: 415388299264 available bytes; 98.09% used; 337621240 free inodes.
| server2 | True | [] | [] |

server2 `/`: 27018563584 available bytes; 98.49% used; 110411164 free inodes.

server2 `/home`: 27018563584 available bytes; 98.49% used; 110411164 free inodes.

server2 `/tmp`: 27018563584 available bytes; 98.49% used; 110411164 free inodes.

server2 `/var/tmp`: 27018563584 available bytes; 98.49% used; 110411164 free inodes.

server2 `/mnt/raid5`: 488784056320 available bytes; 96.62% used; 445153406 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84378578944 available bytes; 95.29% used; 114156087 free inodes.

server3 `/home`: 84378578944 available bytes; 95.29% used; 114156087 free inodes.

server3 `/data`: 149405364224 available bytes; 97.94% used; 225802215 free inodes.

server3 `/tmp`: 84378578944 available bytes; 95.29% used; 114156087 free inodes.

server3 `/var/tmp`: 84378578944 available bytes; 95.29% used; 114156087 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105810558976 available bytes; 94.10% used; 114348324 free inodes.

server4 `/home`: 105810558976 available bytes; 94.10% used; 114348324 free inodes.

server4 `/data`: 73349488640 available bytes; 98.99% used; 225229882 free inodes.

server4 `/tmp`: 105810558976 available bytes; 94.10% used; 114348324 free inodes.

server4 `/var/tmp`: 105810558976 available bytes; 94.10% used; 114348324 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
