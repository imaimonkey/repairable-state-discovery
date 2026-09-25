# V2R cluster inventory

2026-09-25T09:07:27.190811+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318836928512 available bytes; 82.21% used; 112480389 free inodes.

server1 `/home`: 318836928512 available bytes; 82.21% used; 112480389 free inodes.

server1 `/tmp`: 318836928512 available bytes; 82.21% used; 112480389 free inodes.

server1 `/var/tmp`: 318836928512 available bytes; 82.21% used; 112480389 free inodes.

server1 `/mnt/raid5`: 343533383680 available bytes; 98.42% used; 337556969 free inodes.
| server2 | True | ['5', '6'] | [] |

server2 `/`: 22839791616 available bytes; 98.73% used; 110410494 free inodes.

server2 `/home`: 22839791616 available bytes; 98.73% used; 110410494 free inodes.

server2 `/tmp`: 22839791616 available bytes; 98.73% used; 110410494 free inodes.

server2 `/var/tmp`: 22839791616 available bytes; 98.73% used; 110410494 free inodes.

server2 `/mnt/raid5`: 332348436480 available bytes; 97.70% used; 445092870 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84436082688 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84436082688 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142374248448 available bytes; 98.03% used; 225811042 free inodes.

server3 `/tmp`: 84436082688 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84436082688 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632870400 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105632870400 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 243371040768 available bytes; 96.64% used; 224998662 free inodes.

server4 `/tmp`: 105632870400 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105632870400 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
