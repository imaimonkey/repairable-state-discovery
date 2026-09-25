# V2R cluster inventory

2026-09-25T03:46:47.162378+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318937632768 available bytes; 82.21% used; 112480355 free inodes.

server1 `/home`: 318937632768 available bytes; 82.21% used; 112480355 free inodes.

server1 `/tmp`: 318937632768 available bytes; 82.21% used; 112480355 free inodes.

server1 `/var/tmp`: 318937632768 available bytes; 82.21% used; 112480355 free inodes.

server1 `/mnt/raid5`: 415747342336 available bytes; 98.09% used; 337596922 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22973997056 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22973997056 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22973997056 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22973997056 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 464376033280 available bytes; 96.79% used; 445111262 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84341407744 available bytes; 95.29% used; 114156061 free inodes.

server3 `/home`: 84341407744 available bytes; 95.29% used; 114156061 free inodes.

server3 `/data`: 144313450496 available bytes; 98.01% used; 225817117 free inodes.

server3 `/tmp`: 84341407744 available bytes; 95.29% used; 114156061 free inodes.

server3 `/var/tmp`: 84341407744 available bytes; 95.29% used; 114156061 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105683357696 available bytes; 94.10% used; 114350898 free inodes.

server4 `/home`: 105683357696 available bytes; 94.10% used; 114350898 free inodes.

server4 `/data`: 38670024704 available bytes; 99.47% used; 224965290 free inodes.

server4 `/tmp`: 105683357696 available bytes; 94.10% used; 114350898 free inodes.

server4 `/var/tmp`: 105683357696 available bytes; 94.10% used; 114350898 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
