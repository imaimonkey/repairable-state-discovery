# V2R cluster inventory

2026-09-25T19:50:34.949894+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318712864768 available bytes; 82.22% used; 112476335 free inodes.

server1 `/home`: 318712864768 available bytes; 82.22% used; 112476335 free inodes.

server1 `/tmp`: 318712864768 available bytes; 82.22% used; 112476335 free inodes.

server1 `/var/tmp`: 318712864768 available bytes; 82.22% used; 112476335 free inodes.

server1 `/mnt/raid5`: 370831962112 available bytes; 98.30% used; 337540708 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23100252160 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23100252160 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23100252160 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23100252160 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 311469395968 available bytes; 97.85% used; 445063709 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84380766208 available bytes; 95.29% used; 114152628 free inodes.

server3 `/home`: 84380766208 available bytes; 95.29% used; 114152628 free inodes.

server3 `/data`: 128253661184 available bytes; 98.23% used; 225808713 free inodes.

server3 `/tmp`: 84380766208 available bytes; 95.29% used; 114152628 free inodes.

server3 `/var/tmp`: 84380766208 available bytes; 95.29% used; 114152628 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674076160 available bytes; 94.10% used; 114349568 free inodes.

server4 `/home`: 105674076160 available bytes; 94.10% used; 114349568 free inodes.

server4 `/data`: 229542297600 available bytes; 96.83% used; 224929321 free inodes.

server4 `/tmp`: 105674076160 available bytes; 94.10% used; 114349568 free inodes.

server4 `/var/tmp`: 105674076160 available bytes; 94.10% used; 114349568 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
