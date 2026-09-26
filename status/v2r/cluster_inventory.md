# V2R cluster inventory

2026-09-26T03:39:01.709332+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318417231872 available bytes; 82.24% used; 112476267 free inodes.

server1 `/home`: 318417231872 available bytes; 82.24% used; 112476267 free inodes.

server1 `/tmp`: 318417231872 available bytes; 82.24% used; 112476267 free inodes.

server1 `/var/tmp`: 318417231872 available bytes; 82.24% used; 112476267 free inodes.

server1 `/mnt/raid5`: 331001036800 available bytes; 98.48% used; 337545765 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22938230784 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22938230784 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22938230784 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22938230784 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 286979780608 available bytes; 98.02% used; 445052259 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84309831680 available bytes; 95.30% used; 114152360 free inodes.

server3 `/home`: 84309831680 available bytes; 95.30% used; 114152360 free inodes.

server3 `/data`: 125362696192 available bytes; 98.27% used; 225830438 free inodes.

server3 `/tmp`: 84309831680 available bytes; 95.30% used; 114152360 free inodes.

server3 `/var/tmp`: 84309831680 available bytes; 95.30% used; 114152360 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105766404096 available bytes; 94.10% used; 114346784 free inodes.

server4 `/home`: 105766404096 available bytes; 94.10% used; 114346784 free inodes.

server4 `/data`: 108880437248 available bytes; 98.50% used; 224914722 free inodes.

server4 `/tmp`: 105766404096 available bytes; 94.10% used; 114346784 free inodes.

server4 `/var/tmp`: 105766404096 available bytes; 94.10% used; 114346784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
