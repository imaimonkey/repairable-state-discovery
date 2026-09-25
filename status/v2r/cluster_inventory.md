# V2R cluster inventory

2026-09-25T01:57:41.182774+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319025426432 available bytes; 82.20% used; 112480597 free inodes.

server1 `/home`: 319025426432 available bytes; 82.20% used; 112480597 free inodes.

server1 `/tmp`: 319025426432 available bytes; 82.20% used; 112480597 free inodes.

server1 `/var/tmp`: 319025426432 available bytes; 82.20% used; 112480597 free inodes.

server1 `/mnt/raid5`: 416428056576 available bytes; 98.09% used; 337609729 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23025868800 available bytes; 98.72% used; 110410441 free inodes.

server2 `/home`: 23025868800 available bytes; 98.72% used; 110410441 free inodes.

server2 `/tmp`: 23025868800 available bytes; 98.72% used; 110410441 free inodes.

server2 `/var/tmp`: 23025868800 available bytes; 98.72% used; 110410441 free inodes.

server2 `/mnt/raid5`: 493751173120 available bytes; 96.59% used; 445160805 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84352921600 available bytes; 95.29% used; 114156074 free inodes.

server3 `/home`: 84352921600 available bytes; 95.29% used; 114156074 free inodes.

server3 `/data`: 146210459648 available bytes; 97.98% used; 225811763 free inodes.

server3 `/tmp`: 84352921600 available bytes; 95.29% used; 114156074 free inodes.

server3 `/var/tmp`: 84352921600 available bytes; 95.29% used; 114156074 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105761267712 available bytes; 94.10% used; 114348259 free inodes.

server4 `/home`: 105761267712 available bytes; 94.10% used; 114348259 free inodes.

server4 `/data`: 50102996992 available bytes; 99.31% used; 225030423 free inodes.

server4 `/tmp`: 105761267712 available bytes; 94.10% used; 114348259 free inodes.

server4 `/var/tmp`: 105761267712 available bytes; 94.10% used; 114348259 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
