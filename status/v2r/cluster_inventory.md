# V2R cluster inventory

2026-09-26T03:51:14.069871+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318415761408 available bytes; 82.24% used; 112476261 free inodes.

server1 `/home`: 318415761408 available bytes; 82.24% used; 112476261 free inodes.

server1 `/tmp`: 318415761408 available bytes; 82.24% used; 112476261 free inodes.

server1 `/var/tmp`: 318415761408 available bytes; 82.24% used; 112476261 free inodes.

server1 `/mnt/raid5`: 330980327424 available bytes; 98.48% used; 337545711 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22934450176 available bytes; 98.72% used; 110406194 free inodes.

server2 `/home`: 22934450176 available bytes; 98.72% used; 110406194 free inodes.

server2 `/tmp`: 22934450176 available bytes; 98.72% used; 110406194 free inodes.

server2 `/var/tmp`: 22934450176 available bytes; 98.72% used; 110406194 free inodes.

server2 `/mnt/raid5`: 285556244480 available bytes; 98.03% used; 445051752 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84308144128 available bytes; 95.30% used; 114152336 free inodes.

server3 `/home`: 84308144128 available bytes; 95.30% used; 114152336 free inodes.

server3 `/data`: 124625911808 available bytes; 98.28% used; 225820567 free inodes.

server3 `/tmp`: 84308144128 available bytes; 95.30% used; 114152336 free inodes.

server3 `/var/tmp`: 84308144128 available bytes; 95.30% used; 114152336 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105732448256 available bytes; 94.10% used; 114346692 free inodes.

server4 `/home`: 105732448256 available bytes; 94.10% used; 114346692 free inodes.

server4 `/data`: 109838733312 available bytes; 98.48% used; 224929561 free inodes.

server4 `/tmp`: 105732448256 available bytes; 94.10% used; 114346692 free inodes.

server4 `/var/tmp`: 105732448256 available bytes; 94.10% used; 114346692 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
