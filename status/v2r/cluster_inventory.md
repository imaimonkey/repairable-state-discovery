# V2R cluster inventory

2026-09-26T14:13:46.350669+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318131724288 available bytes; 82.25% used; 112474380 free inodes.

server1 `/home`: 318131724288 available bytes; 82.25% used; 112474380 free inodes.

server1 `/tmp`: 318131724288 available bytes; 82.25% used; 112474380 free inodes.

server1 `/var/tmp`: 318131724288 available bytes; 82.25% used; 112474380 free inodes.

server1 `/mnt/raid5`: 674015264768 available bytes; 96.91% used; 337531967 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 19068502016 available bytes; 98.94% used; 110378899 free inodes.

server2 `/home`: 19068502016 available bytes; 98.94% used; 110378899 free inodes.

server2 `/tmp`: 19068502016 available bytes; 98.94% used; 110378899 free inodes.

server2 `/var/tmp`: 19068502016 available bytes; 98.94% used; 110378899 free inodes.

server2 `/mnt/raid5`: 635404505088 available bytes; 95.61% used; 444975307 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82641113088 available bytes; 95.39% used; 114110784 free inodes.

server3 `/home`: 82641113088 available bytes; 95.39% used; 114110784 free inodes.

server3 `/data`: 1346898534400 available bytes; 81.39% used; 225805407 free inodes.

server3 `/tmp`: 82641113088 available bytes; 95.39% used; 114110784 free inodes.

server3 `/var/tmp`: 82641113088 available bytes; 95.39% used; 114110784 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105889271808 available bytes; 94.09% used; 114347928 free inodes.

server4 `/home`: 105889271808 available bytes; 94.09% used; 114347928 free inodes.

server4 `/data`: 411031707648 available bytes; 94.32% used; 224826848 free inodes.

server4 `/tmp`: 105889271808 available bytes; 94.09% used; 114347928 free inodes.

server4 `/var/tmp`: 105889271808 available bytes; 94.09% used; 114347928 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
