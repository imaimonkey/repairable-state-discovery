# V2R cluster inventory

2026-09-25T00:45:40.667536+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319087824896 available bytes; 82.20% used; 112480771 free inodes.

server1 `/home`: 319087824896 available bytes; 82.20% used; 112480771 free inodes.

server1 `/tmp`: 319087824896 available bytes; 82.20% used; 112480771 free inodes.

server1 `/var/tmp`: 319087824896 available bytes; 82.20% used; 112480771 free inodes.

server1 `/mnt/raid5`: 416831029248 available bytes; 98.09% used; 337618150 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23076974592 available bytes; 98.71% used; 110410769 free inodes.

server2 `/home`: 23076974592 available bytes; 98.71% used; 110410769 free inodes.

server2 `/tmp`: 23076974592 available bytes; 98.71% used; 110410769 free inodes.

server2 `/var/tmp`: 23076974592 available bytes; 98.71% used; 110410769 free inodes.

server2 `/mnt/raid5`: 501371588608 available bytes; 96.54% used; 445163261 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352417792 available bytes; 95.29% used; 114156086 free inodes.

server3 `/home`: 84352417792 available bytes; 95.29% used; 114156086 free inodes.

server3 `/data`: 148638941184 available bytes; 97.95% used; 225813150 free inodes.

server3 `/tmp`: 84352417792 available bytes; 95.29% used; 114156086 free inodes.

server3 `/var/tmp`: 84352417792 available bytes; 95.29% used; 114156086 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105788530688 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105788530688 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56417173504 available bytes; 99.22% used; 225036929 free inodes.

server4 `/tmp`: 105788530688 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105788530688 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
