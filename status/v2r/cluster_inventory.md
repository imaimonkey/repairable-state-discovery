# V2R cluster inventory

2026-09-24T00:21:40.413506+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325555380224 available bytes; 81.84% used; 112500682 free inodes.

server1 `/home`: 325555380224 available bytes; 81.84% used; 112500682 free inodes.

server1 `/tmp`: 325555380224 available bytes; 81.84% used; 112500682 free inodes.

server1 `/var/tmp`: 325555380224 available bytes; 81.84% used; 112500682 free inodes.

server1 `/mnt/raid5`: 1178971598848 available bytes; 94.59% used; 337735237 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41000476672 available bytes; 97.71% used; 110432365 free inodes.

server2 `/home`: 41000476672 available bytes; 97.71% used; 110432365 free inodes.

server2 `/tmp`: 41000476672 available bytes; 97.71% used; 110432365 free inodes.

server2 `/var/tmp`: 41000476672 available bytes; 97.71% used; 110432365 free inodes.

server2 `/mnt/raid5`: 533058514944 available bytes; 96.32% used; 445203822 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292637388800 available bytes; 83.67% used; 114209079 free inodes.

server3 `/home`: 292637388800 available bytes; 83.67% used; 114209079 free inodes.

server3 `/data`: 82245947392 available bytes; 98.86% used; 225844367 free inodes.

server3 `/tmp`: 292637388800 available bytes; 83.67% used; 114209079 free inodes.

server3 `/var/tmp`: 292637388800 available bytes; 83.67% used; 114209079 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094145536 available bytes; 94.08% used; 114350567 free inodes.

server4 `/home`: 106094145536 available bytes; 94.08% used; 114350567 free inodes.

server4 `/data`: 292914483200 available bytes; 95.95% used; 225414567 free inodes.

server4 `/tmp`: 106094145536 available bytes; 94.08% used; 114350567 free inodes.

server4 `/var/tmp`: 106094145536 available bytes; 94.08% used; 114350567 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
