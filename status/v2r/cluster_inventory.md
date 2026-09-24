# V2R cluster inventory

2026-09-24T11:55:51.319818+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324289327104 available bytes; 81.91% used; 112488402 free inodes.

server1 `/home`: 324289327104 available bytes; 81.91% used; 112488402 free inodes.

server1 `/tmp`: 324289327104 available bytes; 81.91% used; 112488402 free inodes.

server1 `/var/tmp`: 324289327104 available bytes; 81.91% used; 112488402 free inodes.

server1 `/mnt/raid5`: 413762703360 available bytes; 98.10% used; 337686159 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57634201600 available bytes; 96.78% used; 110429742 free inodes.

server2 `/home`: 57634201600 available bytes; 96.78% used; 110429742 free inodes.

server2 `/tmp`: 57634201600 available bytes; 96.78% used; 110429742 free inodes.

server2 `/var/tmp`: 57634201600 available bytes; 96.78% used; 110429742 free inodes.

server2 `/mnt/raid5`: 509846630400 available bytes; 96.48% used; 445172408 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85751238656 available bytes; 95.21% used; 114198131 free inodes.

server3 `/home`: 85751238656 available bytes; 95.21% used; 114198131 free inodes.

server3 `/data`: 163624468480 available bytes; 97.74% used; 225815759 free inodes.

server3 `/tmp`: 85751238656 available bytes; 95.21% used; 114198131 free inodes.

server3 `/var/tmp`: 85751238656 available bytes; 95.21% used; 114198131 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105727291392 available bytes; 94.10% used; 114348830 free inodes.

server4 `/home`: 105727291392 available bytes; 94.10% used; 114348830 free inodes.

server4 `/data`: 115380936704 available bytes; 98.41% used; 225257886 free inodes.

server4 `/tmp`: 105727291392 available bytes; 94.10% used; 114348830 free inodes.

server4 `/var/tmp`: 105727291392 available bytes; 94.10% used; 114348830 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
