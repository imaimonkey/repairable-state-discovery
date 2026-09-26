# V2R cluster inventory

2026-09-26T14:42:50.433566+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318125510656 available bytes; 82.25% used; 112474360 free inodes.

server1 `/home`: 318125510656 available bytes; 82.25% used; 112474360 free inodes.

server1 `/tmp`: 318125510656 available bytes; 82.25% used; 112474360 free inodes.

server1 `/var/tmp`: 318125510656 available bytes; 82.25% used; 112474360 free inodes.

server1 `/mnt/raid5`: 673989853184 available bytes; 96.91% used; 337531917 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 14395011072 available bytes; 99.20% used; 110378815 free inodes.

server2 `/home`: 14395011072 available bytes; 99.20% used; 110378815 free inodes.

server2 `/tmp`: 14395011072 available bytes; 99.20% used; 110378815 free inodes.

server2 `/var/tmp`: 14395011072 available bytes; 99.20% used; 110378815 free inodes.

server2 `/mnt/raid5`: 634572947456 available bytes; 95.62% used; 444974254 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82628284416 available bytes; 95.39% used; 114110777 free inodes.

server3 `/home`: 82628284416 available bytes; 95.39% used; 114110777 free inodes.

server3 `/data`: 1346878074880 available bytes; 81.39% used; 225805068 free inodes.

server3 `/tmp`: 82628284416 available bytes; 95.39% used; 114110777 free inodes.

server3 `/var/tmp`: 82628284416 available bytes; 95.39% used; 114110777 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105886609408 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105886609408 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410998669312 available bytes; 94.32% used; 224826627 free inodes.

server4 `/tmp`: 105886609408 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105886609408 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
