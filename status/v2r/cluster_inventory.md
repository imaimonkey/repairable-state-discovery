# V2R cluster inventory

2026-09-26T08:34:48.786509+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318745968640 available bytes; 82.22% used; 112475801 free inodes.

server1 `/home`: 318745968640 available bytes; 82.22% used; 112475801 free inodes.

server1 `/tmp`: 318745968640 available bytes; 82.22% used; 112475801 free inodes.

server1 `/var/tmp`: 318745968640 available bytes; 82.22% used; 112475801 free inodes.

server1 `/mnt/raid5`: 219096268800 available bytes; 98.99% used; 337538930 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22320095232 available bytes; 98.75% used; 110403904 free inodes.

server2 `/home`: 22320095232 available bytes; 98.75% used; 110403904 free inodes.

server2 `/tmp`: 22320095232 available bytes; 98.75% used; 110403904 free inodes.

server2 `/var/tmp`: 22320095232 available bytes; 98.75% used; 110403904 free inodes.

server2 `/mnt/raid5`: 255570714624 available bytes; 98.23% used; 445024564 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82677911552 available bytes; 95.39% used; 114110814 free inodes.

server3 `/home`: 82677911552 available bytes; 95.39% used; 114110814 free inodes.

server3 `/data`: 123905122304 available bytes; 98.29% used; 225828768 free inodes.

server3 `/tmp`: 82677911552 available bytes; 95.39% used; 114110814 free inodes.

server3 `/var/tmp`: 82677911552 available bytes; 95.39% used; 114110814 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106064019456 available bytes; 94.08% used; 114348137 free inodes.

server4 `/home`: 106064019456 available bytes; 94.08% used; 114348137 free inodes.

server4 `/data`: 89369608192 available bytes; 98.76% used; 224883415 free inodes.

server4 `/tmp`: 106064019456 available bytes; 94.08% used; 114348137 free inodes.

server4 `/var/tmp`: 106064019456 available bytes; 94.08% used; 114348137 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
