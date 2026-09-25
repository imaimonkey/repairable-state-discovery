# V2R cluster inventory

2026-09-25T02:00:45.244858+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319024795648 available bytes; 82.20% used; 112480589 free inodes.

server1 `/home`: 319024795648 available bytes; 82.20% used; 112480589 free inodes.

server1 `/tmp`: 319024795648 available bytes; 82.20% used; 112480589 free inodes.

server1 `/var/tmp`: 319024795648 available bytes; 82.20% used; 112480589 free inodes.

server1 `/mnt/raid5`: 395627270144 available bytes; 98.19% used; 337609355 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23026147328 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 23026147328 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 23026147328 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 23026147328 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 489567019008 available bytes; 96.62% used; 445150727 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84352946176 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84352946176 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 146162728960 available bytes; 97.98% used; 225811704 free inodes.

server3 `/tmp`: 84352946176 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84352946176 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105761157120 available bytes; 94.10% used; 114348258 free inodes.

server4 `/home`: 105761157120 available bytes; 94.10% used; 114348258 free inodes.

server4 `/data`: 50098929664 available bytes; 99.31% used; 225030364 free inodes.

server4 `/tmp`: 105761157120 available bytes; 94.10% used; 114348258 free inodes.

server4 `/var/tmp`: 105761157120 available bytes; 94.10% used; 114348258 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
