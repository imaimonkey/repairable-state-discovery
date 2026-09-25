# V2R cluster inventory

2026-09-25T19:42:56.754312+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318725451776 available bytes; 82.22% used; 112476332 free inodes.

server1 `/home`: 318725451776 available bytes; 82.22% used; 112476332 free inodes.

server1 `/tmp`: 318725451776 available bytes; 82.22% used; 112476332 free inodes.

server1 `/var/tmp`: 318725451776 available bytes; 82.22% used; 112476332 free inodes.

server1 `/mnt/raid5`: 370846408704 available bytes; 98.30% used; 337540736 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23100887040 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23100887040 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23100887040 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23100887040 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 293495808000 available bytes; 97.97% used; 445064059 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381716480 available bytes; 95.29% used; 114152628 free inodes.

server3 `/home`: 84381716480 available bytes; 95.29% used; 114152628 free inodes.

server3 `/data`: 128252776448 available bytes; 98.23% used; 225808831 free inodes.

server3 `/tmp`: 84381716480 available bytes; 95.29% used; 114152628 free inodes.

server3 `/var/tmp`: 84381716480 available bytes; 95.29% used; 114152628 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674334208 available bytes; 94.10% used; 114349574 free inodes.

server4 `/home`: 105674334208 available bytes; 94.10% used; 114349574 free inodes.

server4 `/data`: 229534613504 available bytes; 96.83% used; 224929453 free inodes.

server4 `/tmp`: 105674334208 available bytes; 94.10% used; 114349574 free inodes.

server4 `/var/tmp`: 105674334208 available bytes; 94.10% used; 114349574 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
