# V2R cluster inventory

2026-09-26T06:00:26.621760+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318780416000 available bytes; 82.22% used; 112476295 free inodes.

server1 `/home`: 318780416000 available bytes; 82.22% used; 112476295 free inodes.

server1 `/tmp`: 318780416000 available bytes; 82.22% used; 112476295 free inodes.

server1 `/var/tmp`: 318780416000 available bytes; 82.22% used; 112476295 free inodes.

server1 `/mnt/raid5`: 229345759232 available bytes; 98.95% used; 337539972 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22737547264 available bytes; 98.73% used; 110405650 free inodes.

server2 `/home`: 22737547264 available bytes; 98.73% used; 110405650 free inodes.

server2 `/tmp`: 22737547264 available bytes; 98.73% used; 110405650 free inodes.

server2 `/var/tmp`: 22737547264 available bytes; 98.73% used; 110405650 free inodes.

server2 `/mnt/raid5`: 274553794560 available bytes; 98.10% used; 445033480 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82440192000 available bytes; 95.40% used; 114110902 free inodes.

server3 `/home`: 82440192000 available bytes; 95.40% used; 114110902 free inodes.

server3 `/data`: 123992080384 available bytes; 98.29% used; 225822790 free inodes.

server3 `/tmp`: 82440192000 available bytes; 95.40% used; 114110902 free inodes.

server3 `/var/tmp`: 82440192000 available bytes; 95.40% used; 114110902 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094080000 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094080000 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106984685568 available bytes; 98.52% used; 224929125 free inodes.

server4 `/tmp`: 106094080000 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094080000 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
