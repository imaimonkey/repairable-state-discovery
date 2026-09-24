# V2R cluster inventory

2026-09-24T21:25:20.139185+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323952381952 available bytes; 81.93% used; 112481414 free inodes.

server1 `/home`: 323952381952 available bytes; 81.93% used; 112481414 free inodes.

server1 `/tmp`: 323952381952 available bytes; 81.93% used; 112481414 free inodes.

server1 `/var/tmp`: 323952381952 available bytes; 81.93% used; 112481414 free inodes.

server1 `/mnt/raid5`: 415508410368 available bytes; 98.09% used; 337628016 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30143111168 available bytes; 98.32% used; 110411345 free inodes.

server2 `/home`: 30143111168 available bytes; 98.32% used; 110411345 free inodes.

server2 `/tmp`: 30143111168 available bytes; 98.32% used; 110411345 free inodes.

server2 `/var/tmp`: 30143111168 available bytes; 98.32% used; 110411345 free inodes.

server2 `/mnt/raid5`: 490570489856 available bytes; 96.61% used; 445155266 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382085120 available bytes; 95.29% used; 114156095 free inodes.

server3 `/home`: 84382085120 available bytes; 95.29% used; 114156095 free inodes.

server3 `/data`: 150380544000 available bytes; 97.92% used; 225803277 free inodes.

server3 `/tmp`: 84382085120 available bytes; 95.29% used; 114156095 free inodes.

server3 `/var/tmp`: 84382085120 available bytes; 95.29% used; 114156095 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632215040 available bytes; 94.11% used; 114348353 free inodes.

server4 `/home`: 105632215040 available bytes; 94.11% used; 114348353 free inodes.

server4 `/data`: 84672061440 available bytes; 98.83% used; 225253139 free inodes.

server4 `/tmp`: 105632215040 available bytes; 94.11% used; 114348353 free inodes.

server4 `/var/tmp`: 105632215040 available bytes; 94.11% used; 114348353 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
