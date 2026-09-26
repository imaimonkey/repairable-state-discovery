# V2R cluster inventory

2026-09-26T02:09:34.669101+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318519287808 available bytes; 82.23% used; 112476292 free inodes.

server1 `/home`: 318519287808 available bytes; 82.23% used; 112476292 free inodes.

server1 `/tmp`: 318519287808 available bytes; 82.23% used; 112476292 free inodes.

server1 `/var/tmp`: 318519287808 available bytes; 82.23% used; 112476292 free inodes.

server1 `/mnt/raid5`: 345212399616 available bytes; 98.42% used; 337546272 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22938775552 available bytes; 98.72% used; 110406220 free inodes.

server2 `/home`: 22938775552 available bytes; 98.72% used; 110406220 free inodes.

server2 `/tmp`: 22938775552 available bytes; 98.72% used; 110406220 free inodes.

server2 `/var/tmp`: 22938775552 available bytes; 98.72% used; 110406220 free inodes.

server2 `/mnt/raid5`: 289560961024 available bytes; 98.00% used; 445054680 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84330688512 available bytes; 95.29% used; 114152370 free inodes.

server3 `/home`: 84330688512 available bytes; 95.29% used; 114152370 free inodes.

server3 `/data`: 124790890496 available bytes; 98.28% used; 225817335 free inodes.

server3 `/tmp`: 84330688512 available bytes; 95.29% used; 114152370 free inodes.

server3 `/var/tmp`: 84330688512 available bytes; 95.29% used; 114152370 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105433497600 available bytes; 94.12% used; 114348357 free inodes.

server4 `/home`: 105433497600 available bytes; 94.12% used; 114348357 free inodes.

server4 `/data`: 130903040000 available bytes; 98.19% used; 224915753 free inodes.

server4 `/tmp`: 105433497600 available bytes; 94.12% used; 114348357 free inodes.

server4 `/var/tmp`: 105433497600 available bytes; 94.12% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
