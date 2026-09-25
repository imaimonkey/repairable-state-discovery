# V2R cluster inventory

2026-09-25T17:45:12.377316+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318669377536 available bytes; 82.22% used; 112476354 free inodes.

server1 `/home`: 318669377536 available bytes; 82.22% used; 112476354 free inodes.

server1 `/tmp`: 318669377536 available bytes; 82.22% used; 112476354 free inodes.

server1 `/var/tmp`: 318669377536 available bytes; 82.22% used; 112476354 free inodes.

server1 `/mnt/raid5`: 371253899264 available bytes; 98.30% used; 337542850 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23096365056 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23096365056 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23096365056 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23096365056 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 315570003968 available bytes; 97.82% used; 445067446 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84390973440 available bytes; 95.29% used; 114152617 free inodes.

server3 `/home`: 84390973440 available bytes; 95.29% used; 114152617 free inodes.

server3 `/data`: 132537176064 available bytes; 98.17% used; 225810874 free inodes.

server3 `/tmp`: 84390973440 available bytes; 95.29% used; 114152617 free inodes.

server3 `/var/tmp`: 84390973440 available bytes; 95.29% used; 114152617 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105617133568 available bytes; 94.11% used; 114349621 free inodes.

server4 `/home`: 105617133568 available bytes; 94.11% used; 114349621 free inodes.

server4 `/data`: 229796495360 available bytes; 96.82% used; 224932647 free inodes.

server4 `/tmp`: 105617133568 available bytes; 94.11% used; 114349621 free inodes.

server4 `/var/tmp`: 105617133568 available bytes; 94.11% used; 114349621 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
