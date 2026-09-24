# V2R cluster inventory

2026-09-24T17:33:39.718376+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324003856384 available bytes; 81.92% used; 112481446 free inodes.

server1 `/home`: 324003856384 available bytes; 81.92% used; 112481446 free inodes.

server1 `/tmp`: 324003856384 available bytes; 81.92% used; 112481446 free inodes.

server1 `/var/tmp`: 324003856384 available bytes; 81.92% used; 112481446 free inodes.

server1 `/mnt/raid5`: 416444665856 available bytes; 98.09% used; 337645970 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 56916606976 available bytes; 96.82% used; 110412483 free inodes.

server2 `/home`: 56916606976 available bytes; 96.82% used; 110412483 free inodes.

server2 `/tmp`: 56916606976 available bytes; 96.82% used; 110412483 free inodes.

server2 `/var/tmp`: 56916606976 available bytes; 96.82% used; 110412483 free inodes.

server2 `/mnt/raid5`: 498686255104 available bytes; 96.55% used; 445162594 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84407877632 available bytes; 95.29% used; 114156148 free inodes.

server3 `/home`: 84407877632 available bytes; 95.29% used; 114156148 free inodes.

server3 `/data`: 158914592768 available bytes; 97.80% used; 225786778 free inodes.

server3 `/tmp`: 84407877632 available bytes; 95.29% used; 114156148 free inodes.

server3 `/var/tmp`: 84407877632 available bytes; 95.29% used; 114156148 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105681342464 available bytes; 94.10% used; 114348565 free inodes.

server4 `/home`: 105681342464 available bytes; 94.10% used; 114348565 free inodes.

server4 `/data`: 89066745856 available bytes; 98.77% used; 225253939 free inodes.

server4 `/tmp`: 105681342464 available bytes; 94.10% used; 114348565 free inodes.

server4 `/var/tmp`: 105681342464 available bytes; 94.10% used; 114348565 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
