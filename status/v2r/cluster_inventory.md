# V2R cluster inventory

2026-09-26T02:11:06.274240+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318518779904 available bytes; 82.23% used; 112476298 free inodes.

server1 `/home`: 318518779904 available bytes; 82.23% used; 112476298 free inodes.

server1 `/tmp`: 318518779904 available bytes; 82.23% used; 112476298 free inodes.

server1 `/var/tmp`: 318518779904 available bytes; 82.23% used; 112476298 free inodes.

server1 `/mnt/raid5`: 345204981760 available bytes; 98.42% used; 337546246 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22938914816 available bytes; 98.72% used; 110406226 free inodes.

server2 `/home`: 22938914816 available bytes; 98.72% used; 110406226 free inodes.

server2 `/tmp`: 22938914816 available bytes; 98.72% used; 110406226 free inodes.

server2 `/var/tmp`: 22938914816 available bytes; 98.72% used; 110406226 free inodes.

server2 `/mnt/raid5`: 289511702528 available bytes; 98.00% used; 445054496 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84330360832 available bytes; 95.29% used; 114152374 free inodes.

server3 `/home`: 84330360832 available bytes; 95.29% used; 114152374 free inodes.

server3 `/data`: 124790300672 available bytes; 98.28% used; 225817320 free inodes.

server3 `/tmp`: 84330360832 available bytes; 95.29% used; 114152374 free inodes.

server3 `/var/tmp`: 84330360832 available bytes; 95.29% used; 114152374 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105433432064 available bytes; 94.12% used; 114348357 free inodes.

server4 `/home`: 105433432064 available bytes; 94.12% used; 114348357 free inodes.

server4 `/data`: 130902654976 available bytes; 98.19% used; 224915757 free inodes.

server4 `/tmp`: 105433432064 available bytes; 94.12% used; 114348357 free inodes.

server4 `/var/tmp`: 105433432064 available bytes; 94.12% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
