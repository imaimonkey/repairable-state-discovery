# V2R cluster inventory

2026-09-25T12:03:43.725859+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319129317376 available bytes; 82.20% used; 112478322 free inodes.

server1 `/home`: 319129317376 available bytes; 82.20% used; 112478322 free inodes.

server1 `/tmp`: 319129317376 available bytes; 82.20% used; 112478322 free inodes.

server1 `/var/tmp`: 319129317376 available bytes; 82.20% used; 112478322 free inodes.

server1 `/mnt/raid5`: 364369346560 available bytes; 98.33% used; 337548573 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22910021632 available bytes; 98.72% used; 110409952 free inodes.

server2 `/home`: 22910021632 available bytes; 98.72% used; 110409952 free inodes.

server2 `/tmp`: 22910021632 available bytes; 98.72% used; 110409952 free inodes.

server2 `/var/tmp`: 22910021632 available bytes; 98.72% used; 110409952 free inodes.

server2 `/mnt/raid5`: 325907296256 available bytes; 97.75% used; 445081804 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84213268480 available bytes; 95.30% used; 114154984 free inodes.

server3 `/home`: 84213268480 available bytes; 95.30% used; 114154984 free inodes.

server3 `/data`: 142120947712 available bytes; 98.04% used; 225812577 free inodes.

server3 `/tmp`: 84213268480 available bytes; 95.30% used; 114154984 free inodes.

server3 `/var/tmp`: 84213268480 available bytes; 95.30% used; 114154984 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105593696256 available bytes; 94.11% used; 114350234 free inodes.

server4 `/home`: 105593696256 available bytes; 94.11% used; 114350234 free inodes.

server4 `/data`: 232644767744 available bytes; 96.78% used; 224972401 free inodes.

server4 `/tmp`: 105593696256 available bytes; 94.11% used; 114350234 free inodes.

server4 `/var/tmp`: 105593696256 available bytes; 94.11% used; 114350234 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
