# V2R cluster inventory

2026-09-25T01:38:04.311742+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319076753408 available bytes; 82.20% used; 112480765 free inodes.

server1 `/home`: 319076753408 available bytes; 82.20% used; 112480765 free inodes.

server1 `/tmp`: 319076753408 available bytes; 82.20% used; 112480765 free inodes.

server1 `/var/tmp`: 319076753408 available bytes; 82.20% used; 112480765 free inodes.

server1 `/mnt/raid5`: 416470446080 available bytes; 98.09% used; 337612027 free inodes.
| server2 | True | ['2', '6'] | [] |

server2 `/`: 23048777728 available bytes; 98.71% used; 110410766 free inodes.

server2 `/home`: 23048777728 available bytes; 98.71% used; 110410766 free inodes.

server2 `/tmp`: 23048777728 available bytes; 98.71% used; 110410766 free inodes.

server2 `/var/tmp`: 23048777728 available bytes; 98.71% used; 110410766 free inodes.

server2 `/mnt/raid5`: 490851876864 available bytes; 96.61% used; 445161141 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84353875968 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84353875968 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 146557476864 available bytes; 97.97% used; 225812151 free inodes.

server3 `/tmp`: 84353875968 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84353875968 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105778651136 available bytes; 94.10% used; 114348287 free inodes.

server4 `/home`: 105778651136 available bytes; 94.10% used; 114348287 free inodes.

server4 `/data`: 53315940352 available bytes; 99.26% used; 225030611 free inodes.

server4 `/tmp`: 105778651136 available bytes; 94.10% used; 114348287 free inodes.

server4 `/var/tmp`: 105778651136 available bytes; 94.10% used; 114348287 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
