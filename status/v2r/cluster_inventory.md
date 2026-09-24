# V2R cluster inventory

2026-09-24T09:10:36.937880+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324473610240 available bytes; 81.90% used; 112490029 free inodes.

server1 `/home`: 324473610240 available bytes; 81.90% used; 112490029 free inodes.

server1 `/tmp`: 324473610240 available bytes; 81.90% used; 112490029 free inodes.

server1 `/var/tmp`: 324473610240 available bytes; 81.90% used; 112490029 free inodes.

server1 `/mnt/raid5`: 503273267200 available bytes; 97.69% used; 337715696 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57779879936 available bytes; 96.78% used; 110430941 free inodes.

server2 `/home`: 57779879936 available bytes; 96.78% used; 110430941 free inodes.

server2 `/tmp`: 57779879936 available bytes; 96.78% used; 110430941 free inodes.

server2 `/var/tmp`: 57779879936 available bytes; 96.78% used; 110430941 free inodes.

server2 `/mnt/raid5`: 515202985984 available bytes; 96.44% used; 445178273 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85471961088 available bytes; 95.23% used; 114173915 free inodes.

server3 `/home`: 85471961088 available bytes; 95.23% used; 114173915 free inodes.

server3 `/data`: 166995259392 available bytes; 97.69% used; 225821613 free inodes.

server3 `/tmp`: 85471961088 available bytes; 95.23% used; 114173915 free inodes.

server3 `/var/tmp`: 85471961088 available bytes; 95.23% used; 114173915 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105758720000 available bytes; 94.10% used; 114349075 free inodes.

server4 `/home`: 105758720000 available bytes; 94.10% used; 114349075 free inodes.

server4 `/data`: 318902456320 available bytes; 95.59% used; 225273364 free inodes.

server4 `/tmp`: 105758720000 available bytes; 94.10% used; 114349075 free inodes.

server4 `/var/tmp`: 105758720000 available bytes; 94.10% used; 114349075 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
