# V2R cluster inventory

2026-09-26T08:21:03.778175+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318747443200 available bytes; 82.22% used; 112475802 free inodes.

server1 `/home`: 318747443200 available bytes; 82.22% used; 112475802 free inodes.

server1 `/tmp`: 318747443200 available bytes; 82.22% used; 112475802 free inodes.

server1 `/var/tmp`: 318747443200 available bytes; 82.22% used; 112475802 free inodes.

server1 `/mnt/raid5`: 219126927360 available bytes; 98.99% used; 337538993 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22325239808 available bytes; 98.75% used; 110403909 free inodes.

server2 `/home`: 22325239808 available bytes; 98.75% used; 110403909 free inodes.

server2 `/tmp`: 22325239808 available bytes; 98.75% used; 110403909 free inodes.

server2 `/var/tmp`: 22325239808 available bytes; 98.75% used; 110403909 free inodes.

server2 `/mnt/raid5`: 255992557568 available bytes; 98.23% used; 445025263 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82680352768 available bytes; 95.39% used; 114110815 free inodes.

server3 `/home`: 82680352768 available bytes; 95.39% used; 114110815 free inodes.

server3 `/data`: 123914211328 available bytes; 98.29% used; 225829073 free inodes.

server3 `/tmp`: 82680352768 available bytes; 95.39% used; 114110815 free inodes.

server3 `/var/tmp`: 82680352768 available bytes; 95.39% used; 114110815 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106064392192 available bytes; 94.08% used; 114348133 free inodes.

server4 `/home`: 106064392192 available bytes; 94.08% used; 114348133 free inodes.

server4 `/data`: 89378369536 available bytes; 98.76% used; 224883415 free inodes.

server4 `/tmp`: 106064392192 available bytes; 94.08% used; 114348133 free inodes.

server4 `/var/tmp`: 106064392192 available bytes; 94.08% used; 114348133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
