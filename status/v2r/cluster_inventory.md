# V2R cluster inventory

2026-09-27T02:45:32.054553+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315084296192 available bytes; 82.42% used; 112443417 free inodes.

server1 `/home`: 315084296192 available bytes; 82.42% used; 112443417 free inodes.

server1 `/tmp`: 315084296192 available bytes; 82.42% used; 112443417 free inodes.

server1 `/var/tmp`: 315084296192 available bytes; 82.42% used; 112443417 free inodes.

server1 `/mnt/raid5`: 637181054976 available bytes; 97.08% used; 337401566 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17626685440 available bytes; 99.02% used; 110365008 free inodes.

server2 `/home`: 17626685440 available bytes; 99.02% used; 110365008 free inodes.

server2 `/tmp`: 17626685440 available bytes; 99.02% used; 110365008 free inodes.

server2 `/var/tmp`: 17626685440 available bytes; 99.02% used; 110365008 free inodes.

server2 `/mnt/raid5`: 580530503680 available bytes; 95.99% used; 444884179 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78707691520 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78707691520 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1336616747008 available bytes; 81.53% used; 225762145 free inodes.

server3 `/tmp`: 78707691520 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78707691520 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111035953152 available bytes; 93.80% used; 114373255 free inodes.

server4 `/home`: 111035953152 available bytes; 93.80% used; 114373255 free inodes.

server4 `/data`: 396960841728 available bytes; 94.51% used; 224781464 free inodes.

server4 `/tmp`: 111035953152 available bytes; 93.80% used; 114373255 free inodes.

server4 `/var/tmp`: 111035953152 available bytes; 93.80% used; 114373255 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
