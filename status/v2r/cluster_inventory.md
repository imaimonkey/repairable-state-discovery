# V2R cluster inventory

2026-09-25T13:02:10.681543+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319109562368 available bytes; 82.20% used; 112477582 free inodes.

server1 `/home`: 319109562368 available bytes; 82.20% used; 112477582 free inodes.

server1 `/tmp`: 319109562368 available bytes; 82.20% used; 112477582 free inodes.

server1 `/var/tmp`: 319109562368 available bytes; 82.20% used; 112477582 free inodes.

server1 `/mnt/raid5`: 364239482880 available bytes; 98.33% used; 337547907 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 8302964736 available bytes; 99.54% used; 110408782 free inodes.

server2 `/home`: 8302964736 available bytes; 99.54% used; 110408782 free inodes.

server2 `/tmp`: 8302964736 available bytes; 99.54% used; 110408782 free inodes.

server2 `/var/tmp`: 8302964736 available bytes; 99.54% used; 110408782 free inodes.

server2 `/mnt/raid5`: 324263358464 available bytes; 97.76% used; 445078040 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84207398912 available bytes; 95.30% used; 114154972 free inodes.

server3 `/home`: 84207398912 available bytes; 95.30% used; 114154972 free inodes.

server3 `/data`: 142355292160 available bytes; 98.03% used; 225810159 free inodes.

server3 `/tmp`: 84207398912 available bytes; 95.30% used; 114154972 free inodes.

server3 `/var/tmp`: 84207398912 available bytes; 95.30% used; 114154972 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105656725504 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105656725504 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 232001138688 available bytes; 96.79% used; 224959930 free inodes.

server4 `/tmp`: 105656725504 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105656725504 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
