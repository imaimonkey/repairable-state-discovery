# V2R cluster inventory

2026-09-26T03:10:01.868905+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318416990208 available bytes; 82.24% used; 112476258 free inodes.

server1 `/home`: 318416990208 available bytes; 82.24% used; 112476258 free inodes.

server1 `/tmp`: 318416990208 available bytes; 82.24% used; 112476258 free inodes.

server1 `/var/tmp`: 318416990208 available bytes; 82.24% used; 112476258 free inodes.

server1 `/mnt/raid5`: 331058032640 available bytes; 98.48% used; 337545916 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22939316224 available bytes; 98.72% used; 110406208 free inodes.

server2 `/home`: 22939316224 available bytes; 98.72% used; 110406208 free inodes.

server2 `/tmp`: 22939316224 available bytes; 98.72% used; 110406208 free inodes.

server2 `/var/tmp`: 22939316224 available bytes; 98.72% used; 110406208 free inodes.

server2 `/mnt/raid5`: 287822827520 available bytes; 98.01% used; 445053177 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84306825216 available bytes; 95.30% used; 114152356 free inodes.

server3 `/home`: 84306825216 available bytes; 95.30% used; 114152356 free inodes.

server3 `/data`: 125439180800 available bytes; 98.27% used; 225830981 free inodes.

server3 `/tmp`: 84306825216 available bytes; 95.30% used; 114152356 free inodes.

server3 `/var/tmp`: 84306825216 available bytes; 95.30% used; 114152356 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105927127040 available bytes; 94.09% used; 114347183 free inodes.

server4 `/home`: 105927127040 available bytes; 94.09% used; 114347183 free inodes.

server4 `/data`: 109164085248 available bytes; 98.49% used; 224914925 free inodes.

server4 `/tmp`: 105927127040 available bytes; 94.09% used; 114347183 free inodes.

server4 `/var/tmp`: 105927127040 available bytes; 94.09% used; 114347183 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
