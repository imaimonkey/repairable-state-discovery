# V2R cluster inventory

2026-09-24T09:26:09.234370+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324460220416 available bytes; 81.90% used; 112489904 free inodes.

server1 `/home`: 324460220416 available bytes; 81.90% used; 112489904 free inodes.

server1 `/tmp`: 324460220416 available bytes; 81.90% used; 112489904 free inodes.

server1 `/var/tmp`: 324460220416 available bytes; 81.90% used; 112489904 free inodes.

server1 `/mnt/raid5`: 502517792768 available bytes; 97.69% used; 337713834 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57774034944 available bytes; 96.78% used; 110430826 free inodes.

server2 `/home`: 57774034944 available bytes; 96.78% used; 110430826 free inodes.

server2 `/tmp`: 57774034944 available bytes; 96.78% used; 110430826 free inodes.

server2 `/var/tmp`: 57774034944 available bytes; 96.78% used; 110430826 free inodes.

server2 `/mnt/raid5`: 514196340736 available bytes; 96.45% used; 445177799 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85850025984 available bytes; 95.21% used; 114199489 free inodes.

server3 `/home`: 85850025984 available bytes; 95.21% used; 114199489 free inodes.

server3 `/data`: 165827690496 available bytes; 97.71% used; 225820951 free inodes.

server3 `/tmp`: 85850025984 available bytes; 95.21% used; 114199489 free inodes.

server3 `/var/tmp`: 85850025984 available bytes; 95.21% used; 114199489 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105757851648 available bytes; 94.10% used; 114349047 free inodes.

server4 `/home`: 105757851648 available bytes; 94.10% used; 114349047 free inodes.

server4 `/data`: 179351719936 available bytes; 97.52% used; 225273296 free inodes.

server4 `/tmp`: 105757851648 available bytes; 94.10% used; 114349047 free inodes.

server4 `/var/tmp`: 105757851648 available bytes; 94.10% used; 114349047 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
