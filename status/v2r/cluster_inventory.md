# V2R cluster inventory

2026-09-25T17:54:22.681148+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318660083712 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318660083712 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318660083712 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318660083712 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 371239477248 available bytes; 98.30% used; 337542644 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23107690496 available bytes; 98.71% used; 110407932 free inodes.

server2 `/home`: 23107690496 available bytes; 98.71% used; 110407932 free inodes.

server2 `/tmp`: 23107690496 available bytes; 98.71% used; 110407932 free inodes.

server2 `/var/tmp`: 23107690496 available bytes; 98.71% used; 110407932 free inodes.

server2 `/mnt/raid5`: 315336593408 available bytes; 97.82% used; 445068059 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84391305216 available bytes; 95.29% used; 114152615 free inodes.

server3 `/home`: 84391305216 available bytes; 95.29% used; 114152615 free inodes.

server3 `/data`: 132528541696 available bytes; 98.17% used; 225810657 free inodes.

server3 `/tmp`: 84391305216 available bytes; 95.29% used; 114152615 free inodes.

server3 `/var/tmp`: 84391305216 available bytes; 95.29% used; 114152615 free inodes.
| server4 | True | ['0', '3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105616904192 available bytes; 94.11% used; 114349622 free inodes.

server4 `/home`: 105616904192 available bytes; 94.11% used; 114349622 free inodes.

server4 `/data`: 229739139072 available bytes; 96.82% used; 224932522 free inodes.

server4 `/tmp`: 105616904192 available bytes; 94.11% used; 114349622 free inodes.

server4 `/var/tmp`: 105616904192 available bytes; 94.11% used; 114349622 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
