# V2R cluster inventory

2026-09-25T12:06:47.250313+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319128866816 available bytes; 82.20% used; 112478316 free inodes.

server1 `/home`: 319128866816 available bytes; 82.20% used; 112478316 free inodes.

server1 `/tmp`: 319128866816 available bytes; 82.20% used; 112478316 free inodes.

server1 `/var/tmp`: 319128866816 available bytes; 82.20% used; 112478316 free inodes.

server1 `/mnt/raid5`: 364359405568 available bytes; 98.33% used; 337548551 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22910763008 available bytes; 98.72% used; 110409968 free inodes.

server2 `/home`: 22910763008 available bytes; 98.72% used; 110409968 free inodes.

server2 `/tmp`: 22910763008 available bytes; 98.72% used; 110409968 free inodes.

server2 `/var/tmp`: 22910763008 available bytes; 98.72% used; 110409968 free inodes.

server2 `/mnt/raid5`: 325900111872 available bytes; 97.75% used; 445081209 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84212252672 available bytes; 95.30% used; 114154982 free inodes.

server3 `/home`: 84212252672 available bytes; 95.30% used; 114154982 free inodes.

server3 `/data`: 142123929600 available bytes; 98.04% used; 225812527 free inodes.

server3 `/tmp`: 84212252672 available bytes; 95.30% used; 114154982 free inodes.

server3 `/var/tmp`: 84212252672 available bytes; 95.30% used; 114154982 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105593622528 available bytes; 94.11% used; 114350234 free inodes.

server4 `/home`: 105593622528 available bytes; 94.11% used; 114350234 free inodes.

server4 `/data`: 231984697344 available bytes; 96.79% used; 224967802 free inodes.

server4 `/tmp`: 105593622528 available bytes; 94.11% used; 114350234 free inodes.

server4 `/var/tmp`: 105593622528 available bytes; 94.11% used; 114350234 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
