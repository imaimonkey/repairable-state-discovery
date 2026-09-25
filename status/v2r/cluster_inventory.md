# V2R cluster inventory

2026-09-25T17:08:29.662621+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318680719360 available bytes; 82.22% used; 112476343 free inodes.

server1 `/home`: 318680719360 available bytes; 82.22% used; 112476343 free inodes.

server1 `/tmp`: 318680719360 available bytes; 82.22% used; 112476343 free inodes.

server1 `/var/tmp`: 318680719360 available bytes; 82.22% used; 112476343 free inodes.

server1 `/mnt/raid5`: 363849646080 available bytes; 98.33% used; 337543647 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23101308928 available bytes; 98.71% used; 110407942 free inodes.

server2 `/home`: 23101308928 available bytes; 98.71% used; 110407942 free inodes.

server2 `/tmp`: 23101308928 available bytes; 98.71% used; 110407942 free inodes.

server2 `/var/tmp`: 23101308928 available bytes; 98.71% used; 110407942 free inodes.

server2 `/mnt/raid5`: 316662157312 available bytes; 97.81% used; 445068849 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84394426368 available bytes; 95.29% used; 114152611 free inodes.

server3 `/home`: 84394426368 available bytes; 95.29% used; 114152611 free inodes.

server3 `/data`: 132804603904 available bytes; 98.16% used; 225811826 free inodes.

server3 `/tmp`: 84394426368 available bytes; 95.29% used; 114152611 free inodes.

server3 `/var/tmp`: 84394426368 available bytes; 95.29% used; 114152611 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105626697728 available bytes; 94.11% used; 114349645 free inodes.

server4 `/home`: 105626697728 available bytes; 94.11% used; 114349645 free inodes.

server4 `/data`: 229880987648 available bytes; 96.82% used; 224933214 free inodes.

server4 `/tmp`: 105626697728 available bytes; 94.11% used; 114349645 free inodes.

server4 `/var/tmp`: 105626697728 available bytes; 94.11% used; 114349645 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
