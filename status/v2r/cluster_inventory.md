# V2R cluster inventory

2026-09-25T19:53:38.349409+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318712246272 available bytes; 82.22% used; 112476335 free inodes.

server1 `/home`: 318712246272 available bytes; 82.22% used; 112476335 free inodes.

server1 `/tmp`: 318712246272 available bytes; 82.22% used; 112476335 free inodes.

server1 `/var/tmp`: 318712246272 available bytes; 82.22% used; 112476335 free inodes.

server1 `/mnt/raid5`: 370826383360 available bytes; 98.30% used; 337540687 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23095099392 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23095099392 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23095099392 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23095099392 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 311379668992 available bytes; 97.85% used; 445063595 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381507584 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84381507584 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 128248311808 available bytes; 98.23% used; 225808665 free inodes.

server3 `/tmp`: 84381507584 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84381507584 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105673990144 available bytes; 94.10% used; 114349572 free inodes.

server4 `/home`: 105673990144 available bytes; 94.10% used; 114349572 free inodes.

server4 `/data`: 229438668800 available bytes; 96.83% used; 224929225 free inodes.

server4 `/tmp`: 105673990144 available bytes; 94.10% used; 114349572 free inodes.

server4 `/var/tmp`: 105673990144 available bytes; 94.10% used; 114349572 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
