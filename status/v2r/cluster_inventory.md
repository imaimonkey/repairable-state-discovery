# V2R cluster inventory

2026-09-26T03:26:48.957334+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318416269312 available bytes; 82.24% used; 112476260 free inodes.

server1 `/home`: 318416269312 available bytes; 82.24% used; 112476260 free inodes.

server1 `/tmp`: 318416269312 available bytes; 82.24% used; 112476260 free inodes.

server1 `/var/tmp`: 318416269312 available bytes; 82.24% used; 112476260 free inodes.

server1 `/mnt/raid5`: 331027685376 available bytes; 98.48% used; 337545840 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22933782528 available bytes; 98.72% used; 110406212 free inodes.

server2 `/home`: 22933782528 available bytes; 98.72% used; 110406212 free inodes.

server2 `/tmp`: 22933782528 available bytes; 98.72% used; 110406212 free inodes.

server2 `/var/tmp`: 22933782528 available bytes; 98.72% used; 110406212 free inodes.

server2 `/mnt/raid5`: 287347146752 available bytes; 98.01% used; 445052791 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84309090304 available bytes; 95.30% used; 114152362 free inodes.

server3 `/home`: 84309090304 available bytes; 95.30% used; 114152362 free inodes.

server3 `/data`: 125428490240 available bytes; 98.27% used; 225830669 free inodes.

server3 `/tmp`: 84309090304 available bytes; 95.30% used; 114152362 free inodes.

server3 `/var/tmp`: 84309090304 available bytes; 95.30% used; 114152362 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105842364416 available bytes; 94.09% used; 114346959 free inodes.

server4 `/home`: 105842364416 available bytes; 94.09% used; 114346959 free inodes.

server4 `/data`: 108954869760 available bytes; 98.49% used; 224914809 free inodes.

server4 `/tmp`: 105842364416 available bytes; 94.09% used; 114346959 free inodes.

server4 `/var/tmp`: 105842364416 available bytes; 94.09% used; 114346959 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
