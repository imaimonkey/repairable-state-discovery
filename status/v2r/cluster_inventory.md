# V2R cluster inventory

2026-09-24T07:45:05.227798+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324438364160 available bytes; 81.90% used; 112490921 free inodes.

server1 `/home`: 324438364160 available bytes; 81.90% used; 112490921 free inodes.

server1 `/tmp`: 324438364160 available bytes; 81.90% used; 112490921 free inodes.

server1 `/var/tmp`: 324438364160 available bytes; 81.90% used; 112490921 free inodes.

server1 `/mnt/raid5`: 508412301312 available bytes; 97.67% used; 337722769 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57839558656 available bytes; 96.77% used; 110431118 free inodes.

server2 `/home`: 57839558656 available bytes; 96.77% used; 110431118 free inodes.

server2 `/tmp`: 57839558656 available bytes; 96.77% used; 110431118 free inodes.

server2 `/var/tmp`: 57839558656 available bytes; 96.77% used; 110431118 free inodes.

server2 `/mnt/raid5`: 517845282816 available bytes; 96.42% used; 445181286 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127151448064 available bytes; 92.90% used; 114199801 free inodes.

server3 `/home`: 127151448064 available bytes; 92.90% used; 114199801 free inodes.

server3 `/data`: 138671149056 available bytes; 98.08% used; 225833433 free inodes.

server3 `/tmp`: 127151448064 available bytes; 92.90% used; 114199801 free inodes.

server3 `/var/tmp`: 127151448064 available bytes; 92.90% used; 114199801 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780051968 available bytes; 94.10% used; 114349177 free inodes.

server4 `/home`: 105780051968 available bytes; 94.10% used; 114349177 free inodes.

server4 `/data`: 285678673920 available bytes; 96.05% used; 225366733 free inodes.

server4 `/tmp`: 105780051968 available bytes; 94.10% used; 114349177 free inodes.

server4 `/var/tmp`: 105780051968 available bytes; 94.10% used; 114349177 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
