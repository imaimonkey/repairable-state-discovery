# V2R cluster inventory

2026-09-25T10:28:43.670858+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318835744768 available bytes; 82.21% used; 112480401 free inodes.

server1 `/home`: 318835744768 available bytes; 82.21% used; 112480401 free inodes.

server1 `/tmp`: 318835744768 available bytes; 82.21% used; 112480401 free inodes.

server1 `/var/tmp`: 318835744768 available bytes; 82.21% used; 112480401 free inodes.

server1 `/mnt/raid5`: 364846694400 available bytes; 98.33% used; 337555285 free inodes.
| server2 | True | ['3', '5', '6'] | [] |

server2 `/`: 22831583232 available bytes; 98.73% used; 110410490 free inodes.

server2 `/home`: 22831583232 available bytes; 98.73% used; 110410490 free inodes.

server2 `/tmp`: 22831583232 available bytes; 98.73% used; 110410490 free inodes.

server2 `/var/tmp`: 22831583232 available bytes; 98.73% used; 110410490 free inodes.

server2 `/mnt/raid5`: 316279836672 available bytes; 97.81% used; 445090063 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84419608576 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84419608576 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142020022272 available bytes; 98.04% used; 225815778 free inodes.

server3 `/tmp`: 84419608576 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84419608576 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105613418496 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105613418496 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238445645824 available bytes; 96.70% used; 224987775 free inodes.

server4 `/tmp`: 105613418496 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105613418496 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
