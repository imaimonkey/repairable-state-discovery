# V2R cluster inventory

2026-09-26T03:34:27.004782+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318416392192 available bytes; 82.24% used; 112476264 free inodes.

server1 `/home`: 318416392192 available bytes; 82.24% used; 112476264 free inodes.

server1 `/tmp`: 318416392192 available bytes; 82.24% used; 112476264 free inodes.

server1 `/var/tmp`: 318416392192 available bytes; 82.24% used; 112476264 free inodes.

server1 `/mnt/raid5`: 331011555328 available bytes; 98.48% used; 337545802 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22940258304 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22940258304 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22940258304 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22940258304 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 287106805760 available bytes; 98.02% used; 445052424 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 84310814720 available bytes; 95.30% used; 114152375 free inodes.

server3 `/home`: 84310814720 available bytes; 95.30% used; 114152375 free inodes.

server3 `/data`: 125362745344 available bytes; 98.27% used; 225830523 free inodes.

server3 `/tmp`: 84310814720 available bytes; 95.30% used; 114152375 free inodes.

server3 `/var/tmp`: 84310814720 available bytes; 95.30% used; 114152375 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105800126464 available bytes; 94.10% used; 114346872 free inodes.

server4 `/home`: 105800126464 available bytes; 94.10% used; 114346872 free inodes.

server4 `/data`: 108924272640 available bytes; 98.49% used; 224914756 free inodes.

server4 `/tmp`: 105800126464 available bytes; 94.10% used; 114346872 free inodes.

server4 `/var/tmp`: 105800126464 available bytes; 94.10% used; 114346872 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
