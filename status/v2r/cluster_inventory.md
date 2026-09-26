# V2R cluster inventory

2026-09-26T08:45:30.185879+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318745853952 available bytes; 82.22% used; 112475802 free inodes.

server1 `/home`: 318745853952 available bytes; 82.22% used; 112475802 free inodes.

server1 `/tmp`: 318745853952 available bytes; 82.22% used; 112475802 free inodes.

server1 `/var/tmp`: 318745853952 available bytes; 82.22% used; 112475802 free inodes.

server1 `/mnt/raid5`: 219071520768 available bytes; 99.00% used; 337538861 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22325612544 available bytes; 98.75% used; 110403909 free inodes.

server2 `/home`: 22325612544 available bytes; 98.75% used; 110403909 free inodes.

server2 `/tmp`: 22325612544 available bytes; 98.75% used; 110403909 free inodes.

server2 `/var/tmp`: 22325612544 available bytes; 98.75% used; 110403909 free inodes.

server2 `/mnt/raid5`: 255285043200 available bytes; 98.24% used; 445024742 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82676486144 available bytes; 95.39% used; 114110807 free inodes.

server3 `/home`: 82676486144 available bytes; 95.39% used; 114110807 free inodes.

server3 `/data`: 123901485056 available bytes; 98.29% used; 225828546 free inodes.

server3 `/tmp`: 82676486144 available bytes; 95.39% used; 114110807 free inodes.

server3 `/var/tmp`: 82676486144 available bytes; 95.39% used; 114110807 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106063638528 available bytes; 94.08% used; 114348133 free inodes.

server4 `/home`: 106063638528 available bytes; 94.08% used; 114348133 free inodes.

server4 `/data`: 89355292672 available bytes; 98.77% used; 224883394 free inodes.

server4 `/tmp`: 106063638528 available bytes; 94.08% used; 114348133 free inodes.

server4 `/var/tmp`: 106063638528 available bytes; 94.08% used; 114348133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
