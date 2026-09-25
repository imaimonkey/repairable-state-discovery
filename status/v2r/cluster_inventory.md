# V2R cluster inventory

2026-09-25T20:10:28.769535+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318718455808 available bytes; 82.22% used; 112476348 free inodes.

server1 `/home`: 318718455808 available bytes; 82.22% used; 112476348 free inodes.

server1 `/tmp`: 318718455808 available bytes; 82.22% used; 112476348 free inodes.

server1 `/var/tmp`: 318718455808 available bytes; 82.22% used; 112476348 free inodes.

server1 `/mnt/raid5`: 370799554560 available bytes; 98.30% used; 337540610 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23089139712 available bytes; 98.71% used; 110407934 free inodes.

server2 `/home`: 23089139712 available bytes; 98.71% used; 110407934 free inodes.

server2 `/tmp`: 23089139712 available bytes; 98.71% used; 110407934 free inodes.

server2 `/var/tmp`: 23089139712 available bytes; 98.71% used; 110407934 free inodes.

server2 `/mnt/raid5`: 310963802112 available bytes; 97.85% used; 445063239 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382265344 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84382265344 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 127196061696 available bytes; 98.24% used; 225808371 free inodes.

server3 `/tmp`: 84382265344 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84382265344 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105673498624 available bytes; 94.10% used; 114349572 free inodes.

server4 `/home`: 105673498624 available bytes; 94.10% used; 114349572 free inodes.

server4 `/data`: 229426298880 available bytes; 96.83% used; 224929205 free inodes.

server4 `/tmp`: 105673498624 available bytes; 94.10% used; 114349572 free inodes.

server4 `/var/tmp`: 105673498624 available bytes; 94.10% used; 114349572 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
