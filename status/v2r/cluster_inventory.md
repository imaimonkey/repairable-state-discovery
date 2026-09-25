# V2R cluster inventory

2026-09-25T19:56:29.727114+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318713135104 available bytes; 82.22% used; 112476337 free inodes.

server1 `/home`: 318713135104 available bytes; 82.22% used; 112476337 free inodes.

server1 `/tmp`: 318713135104 available bytes; 82.22% used; 112476337 free inodes.

server1 `/var/tmp`: 318713135104 available bytes; 82.22% used; 112476337 free inodes.

server1 `/mnt/raid5`: 370818334720 available bytes; 98.30% used; 337540664 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23093567488 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23093567488 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23093567488 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23093567488 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 311296278528 available bytes; 97.85% used; 445063373 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84381065216 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84381065216 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 128245309440 available bytes; 98.23% used; 225808628 free inodes.

server3 `/tmp`: 84381065216 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84381065216 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105673904128 available bytes; 94.10% used; 114349572 free inodes.

server4 `/home`: 105673904128 available bytes; 94.10% used; 114349572 free inodes.

server4 `/data`: 229441945600 available bytes; 96.83% used; 224929226 free inodes.

server4 `/tmp`: 105673904128 available bytes; 94.10% used; 114349572 free inodes.

server4 `/var/tmp`: 105673904128 available bytes; 94.10% used; 114349572 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
