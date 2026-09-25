# V2R cluster inventory

2026-09-25T01:49:59.958070+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319025655808 available bytes; 82.20% used; 112480597 free inodes.

server1 `/home`: 319025655808 available bytes; 82.20% used; 112480597 free inodes.

server1 `/tmp`: 319025655808 available bytes; 82.20% used; 112480597 free inodes.

server1 `/var/tmp`: 319025655808 available bytes; 82.20% used; 112480597 free inodes.

server1 `/mnt/raid5`: 416444985344 available bytes; 98.09% used; 337610628 free inodes.
| server2 | True | ['2', '3', '6'] | [] | reference_compatible=False |

server2 `/`: 23041232896 available bytes; 98.71% used; 110410780 free inodes.

server2 `/home`: 23041232896 available bytes; 98.71% used; 110410780 free inodes.

server2 `/tmp`: 23041232896 available bytes; 98.71% used; 110410780 free inodes.

server2 `/var/tmp`: 23041232896 available bytes; 98.71% used; 110410780 free inodes.

server2 `/mnt/raid5`: 490500141056 available bytes; 96.61% used; 445161152 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84353851392 available bytes; 95.29% used; 114156080 free inodes.

server3 `/home`: 84353851392 available bytes; 95.29% used; 114156080 free inodes.

server3 `/data`: 146350366720 available bytes; 97.98% used; 225811921 free inodes.

server3 `/tmp`: 84353851392 available bytes; 95.29% used; 114156080 free inodes.

server3 `/var/tmp`: 84353851392 available bytes; 95.29% used; 114156080 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105761492992 available bytes; 94.10% used; 114348274 free inodes.

server4 `/home`: 105761492992 available bytes; 94.10% used; 114348274 free inodes.

server4 `/data`: 53309591552 available bytes; 99.26% used; 225030544 free inodes.

server4 `/tmp`: 105761492992 available bytes; 94.10% used; 114348274 free inodes.

server4 `/var/tmp`: 105761492992 available bytes; 94.10% used; 114348274 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
