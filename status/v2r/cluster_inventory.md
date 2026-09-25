# V2R cluster inventory

2026-09-25T07:36:47.017909+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318872625152 available bytes; 82.21% used; 112480374 free inodes.

server1 `/home`: 318872625152 available bytes; 82.21% used; 112480374 free inodes.

server1 `/tmp`: 318872625152 available bytes; 82.21% used; 112480374 free inodes.

server1 `/var/tmp`: 318872625152 available bytes; 82.21% used; 112480374 free inodes.

server1 `/mnt/raid5`: 365218660352 available bytes; 98.32% used; 337558375 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22859530240 available bytes; 98.72% used; 110410514 free inodes.

server2 `/home`: 22859530240 available bytes; 98.72% used; 110410514 free inodes.

server2 `/tmp`: 22859530240 available bytes; 98.72% used; 110410514 free inodes.

server2 `/var/tmp`: 22859530240 available bytes; 98.72% used; 110410514 free inodes.

server2 `/mnt/raid5`: 334958395392 available bytes; 97.69% used; 445096624 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84437405696 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84437405696 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142395506688 available bytes; 98.03% used; 225812593 free inodes.

server3 `/tmp`: 84437405696 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84437405696 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637646336 available bytes; 94.11% used; 114350351 free inodes.

server4 `/home`: 105637646336 available bytes; 94.11% used; 114350351 free inodes.

server4 `/data`: 249076027392 available bytes; 96.56% used; 225013346 free inodes.

server4 `/tmp`: 105637646336 available bytes; 94.11% used; 114350351 free inodes.

server4 `/var/tmp`: 105637646336 available bytes; 94.11% used; 114350351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
