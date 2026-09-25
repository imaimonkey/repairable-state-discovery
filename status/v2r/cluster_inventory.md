# V2R cluster inventory

2026-09-25T07:36:12.459600+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318872780800 available bytes; 82.21% used; 112480374 free inodes.

server1 `/home`: 318872780800 available bytes; 82.21% used; 112480374 free inodes.

server1 `/tmp`: 318872780800 available bytes; 82.21% used; 112480374 free inodes.

server1 `/var/tmp`: 318872780800 available bytes; 82.21% used; 112480374 free inodes.

server1 `/mnt/raid5`: 365222891520 available bytes; 98.32% used; 337558384 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22859714560 available bytes; 98.72% used; 110410514 free inodes.

server2 `/home`: 22859714560 available bytes; 98.72% used; 110410514 free inodes.

server2 `/tmp`: 22859714560 available bytes; 98.72% used; 110410514 free inodes.

server2 `/var/tmp`: 22859714560 available bytes; 98.72% used; 110410514 free inodes.

server2 `/mnt/raid5`: 336186441728 available bytes; 97.68% used; 445096638 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84437463040 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84437463040 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142395715584 available bytes; 98.03% used; 225812613 free inodes.

server3 `/tmp`: 84437463040 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84437463040 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105637675008 available bytes; 94.11% used; 114350351 free inodes.

server4 `/home`: 105637675008 available bytes; 94.11% used; 114350351 free inodes.

server4 `/data`: 249082863616 available bytes; 96.56% used; 225013418 free inodes.

server4 `/tmp`: 105637675008 available bytes; 94.11% used; 114350351 free inodes.

server4 `/var/tmp`: 105637675008 available bytes; 94.11% used; 114350351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
