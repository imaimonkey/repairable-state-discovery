# V2R cluster inventory

2026-09-23T22:19:48.421119+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325707747328 available bytes; 81.83% used; 112501406 free inodes.

server1 `/home`: 325707747328 available bytes; 81.83% used; 112501406 free inodes.

server1 `/tmp`: 325707747328 available bytes; 81.83% used; 112501406 free inodes.

server1 `/var/tmp`: 325707747328 available bytes; 81.83% used; 112501406 free inodes.

server1 `/mnt/raid5`: 1388106309632 available bytes; 93.63% used; 337739858 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41091702784 available bytes; 97.71% used; 110432646 free inodes.

server2 `/home`: 41091702784 available bytes; 97.71% used; 110432646 free inodes.

server2 `/tmp`: 41091702784 available bytes; 97.71% used; 110432646 free inodes.

server2 `/var/tmp`: 41091702784 available bytes; 97.71% used; 110432646 free inodes.

server2 `/mnt/raid5`: 536456712192 available bytes; 96.29% used; 445207049 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292838486016 available bytes; 83.66% used; 114216288 free inodes.

server3 `/home`: 292838486016 available bytes; 83.66% used; 114216288 free inodes.

server3 `/data`: 82439766016 available bytes; 98.86% used; 225847519 free inodes.

server3 `/tmp`: 292838486016 available bytes; 83.66% used; 114216288 free inodes.

server3 `/var/tmp`: 292838486016 available bytes; 83.66% used; 114216288 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106405122048 available bytes; 94.06% used; 114354907 free inodes.

server4 `/home`: 106405122048 available bytes; 94.06% used; 114354907 free inodes.

server4 `/data`: 300111245312 available bytes; 95.85% used; 225439530 free inodes.

server4 `/tmp`: 106405122048 available bytes; 94.06% used; 114354907 free inodes.

server4 `/var/tmp`: 106405122048 available bytes; 94.06% used; 114354907 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
