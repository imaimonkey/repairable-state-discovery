# V2R cluster inventory

2026-09-24T19:20:02.056931+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323995484160 available bytes; 81.93% used; 112481468 free inodes.

server1 `/home`: 323995484160 available bytes; 81.93% used; 112481468 free inodes.

server1 `/tmp`: 323995484160 available bytes; 81.93% used; 112481468 free inodes.

server1 `/var/tmp`: 323995484160 available bytes; 81.93% used; 112481468 free inodes.

server1 `/mnt/raid5`: 415634898944 available bytes; 98.09% used; 337633530 free inodes.
| server2 | True | [] | [] |

server2 `/`: 54461861888 available bytes; 96.96% used; 110411908 free inodes.

server2 `/home`: 54461861888 available bytes; 96.96% used; 110411908 free inodes.

server2 `/tmp`: 54461861888 available bytes; 96.96% used; 110411908 free inodes.

server2 `/var/tmp`: 54461861888 available bytes; 96.96% used; 110411908 free inodes.

server2 `/mnt/raid5`: 495172239360 available bytes; 96.58% used; 445158884 free inodes.
| server3 | True | ['1'] | [] |

server3 `/`: 84406931456 available bytes; 95.29% used; 114156139 free inodes.

server3 `/home`: 84406931456 available bytes; 95.29% used; 114156139 free inodes.

server3 `/data`: 152358182912 available bytes; 97.89% used; 225799656 free inodes.

server3 `/tmp`: 84406931456 available bytes; 95.29% used; 114156139 free inodes.

server3 `/var/tmp`: 84406931456 available bytes; 95.29% used; 114156139 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105660289024 available bytes; 94.10% used; 114348467 free inodes.

server4 `/home`: 105660289024 available bytes; 94.10% used; 114348467 free inodes.

server4 `/data`: 89893801984 available bytes; 98.76% used; 225267058 free inodes.

server4 `/tmp`: 105660289024 available bytes; 94.10% used; 114348467 free inodes.

server4 `/var/tmp`: 105660289024 available bytes; 94.10% used; 114348467 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
