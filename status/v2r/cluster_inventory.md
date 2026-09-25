# V2R cluster inventory

2026-09-25T10:19:31.135554+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318835761152 available bytes; 82.21% used; 112480385 free inodes.

server1 `/home`: 318835761152 available bytes; 82.21% used; 112480385 free inodes.

server1 `/tmp`: 318835761152 available bytes; 82.21% used; 112480385 free inodes.

server1 `/var/tmp`: 318835761152 available bytes; 82.21% used; 112480385 free inodes.

server1 `/mnt/raid5`: 364665020416 available bytes; 98.33% used; 337556329 free inodes.
| server2 | True | ['3', '6'] | [] |

server2 `/`: 22833065984 available bytes; 98.73% used; 110410482 free inodes.

server2 `/home`: 22833065984 available bytes; 98.73% used; 110410482 free inodes.

server2 `/tmp`: 22833065984 available bytes; 98.73% used; 110410482 free inodes.

server2 `/var/tmp`: 22833065984 available bytes; 98.73% used; 110410482 free inodes.

server2 `/mnt/raid5`: 315931262976 available bytes; 97.82% used; 445090676 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84416888832 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84416888832 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142027558912 available bytes; 98.04% used; 225816035 free inodes.

server3 `/tmp`: 84416888832 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84416888832 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105613742080 available bytes; 94.11% used; 114350257 free inodes.

server4 `/home`: 105613742080 available bytes; 94.11% used; 114350257 free inodes.

server4 `/data`: 238459256832 available bytes; 96.70% used; 224988838 free inodes.

server4 `/tmp`: 105613742080 available bytes; 94.11% used; 114350257 free inodes.

server4 `/var/tmp`: 105613742080 available bytes; 94.11% used; 114350257 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
