# V2R cluster inventory

2026-09-25T07:59:49.941851+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318860087296 available bytes; 82.21% used; 112480369 free inodes.

server1 `/home`: 318860087296 available bytes; 82.21% used; 112480369 free inodes.

server1 `/tmp`: 318860087296 available bytes; 82.21% used; 112480369 free inodes.

server1 `/var/tmp`: 318860087296 available bytes; 82.21% used; 112480369 free inodes.

server1 `/mnt/raid5`: 386617286656 available bytes; 98.23% used; 337557918 free inodes.
| server2 | True | ['0'] | [] |

server2 `/`: 22844088320 available bytes; 98.73% used; 110410483 free inodes.

server2 `/home`: 22844088320 available bytes; 98.73% used; 110410483 free inodes.

server2 `/tmp`: 22844088320 available bytes; 98.73% used; 110410483 free inodes.

server2 `/var/tmp`: 22844088320 available bytes; 98.73% used; 110410483 free inodes.

server2 `/mnt/raid5`: 334225674240 available bytes; 97.69% used; 445095401 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84437921792 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84437921792 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142388899840 available bytes; 98.03% used; 225812208 free inodes.

server3 `/tmp`: 84437921792 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84437921792 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105625575424 available bytes; 94.11% used; 114350336 free inodes.

server4 `/home`: 105625575424 available bytes; 94.11% used; 114350336 free inodes.

server4 `/data`: 249043722240 available bytes; 96.56% used; 225009892 free inodes.

server4 `/tmp`: 105625575424 available bytes; 94.11% used; 114350336 free inodes.

server4 `/var/tmp`: 105625575424 available bytes; 94.11% used; 114350336 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
