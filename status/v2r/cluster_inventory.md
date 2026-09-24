# V2R cluster inventory

2026-09-24T05:39:58.418018+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324531208192 available bytes; 81.90% used; 112492168 free inodes.

server1 `/home`: 324531208192 available bytes; 81.90% used; 112492168 free inodes.

server1 `/tmp`: 324531208192 available bytes; 81.90% used; 112492168 free inodes.

server1 `/var/tmp`: 324531208192 available bytes; 81.90% used; 112492168 free inodes.

server1 `/mnt/raid5`: 517629095936 available bytes; 97.63% used; 337723949 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57914658816 available bytes; 96.77% used; 110431342 free inodes.

server2 `/home`: 57914658816 available bytes; 96.77% used; 110431342 free inodes.

server2 `/tmp`: 57914658816 available bytes; 96.77% used; 110431342 free inodes.

server2 `/var/tmp`: 57914658816 available bytes; 96.77% used; 110431342 free inodes.

server2 `/mnt/raid5`: 522072608768 available bytes; 96.39% used; 445193700 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126797041664 available bytes; 92.92% used; 114174193 free inodes.

server3 `/home`: 126797041664 available bytes; 92.92% used; 114174193 free inodes.

server3 `/data`: 185254703104 available bytes; 97.44% used; 225839192 free inodes.

server3 `/tmp`: 126797041664 available bytes; 92.92% used; 114174193 free inodes.

server3 `/var/tmp`: 126797041664 available bytes; 92.92% used; 114174193 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105816485888 available bytes; 94.10% used; 114349353 free inodes.

server4 `/home`: 105816485888 available bytes; 94.10% used; 114349353 free inodes.

server4 `/data`: 251502071808 available bytes; 96.52% used; 225358031 free inodes.

server4 `/tmp`: 105816485888 available bytes; 94.10% used; 114349353 free inodes.

server4 `/var/tmp`: 105816485888 available bytes; 94.10% used; 114349353 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
