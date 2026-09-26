# V2R cluster inventory

2026-09-26T03:28:20.561889+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318415925248 available bytes; 82.24% used; 112476258 free inodes.

server1 `/home`: 318415925248 available bytes; 82.24% used; 112476258 free inodes.

server1 `/tmp`: 318415925248 available bytes; 82.24% used; 112476258 free inodes.

server1 `/var/tmp`: 318415925248 available bytes; 82.24% used; 112476258 free inodes.

server1 `/mnt/raid5`: 310378967040 available bytes; 98.58% used; 337545834 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22932959232 available bytes; 98.72% used; 110406210 free inodes.

server2 `/home`: 22932959232 available bytes; 98.72% used; 110406210 free inodes.

server2 `/tmp`: 22932959232 available bytes; 98.72% used; 110406210 free inodes.

server2 `/var/tmp`: 22932959232 available bytes; 98.72% used; 110406210 free inodes.

server2 `/mnt/raid5`: 287293751296 available bytes; 98.01% used; 445052622 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84308451328 available bytes; 95.30% used; 114152360 free inodes.

server3 `/home`: 84308451328 available bytes; 95.30% used; 114152360 free inodes.

server3 `/data`: 125427277824 available bytes; 98.27% used; 225830652 free inodes.

server3 `/tmp`: 84308451328 available bytes; 95.30% used; 114152360 free inodes.

server3 `/var/tmp`: 84308451328 available bytes; 95.30% used; 114152360 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105842311168 available bytes; 94.09% used; 114346959 free inodes.

server4 `/home`: 105842311168 available bytes; 94.09% used; 114346959 free inodes.

server4 `/data`: 108953587712 available bytes; 98.49% used; 224914804 free inodes.

server4 `/tmp`: 105842311168 available bytes; 94.09% used; 114346959 free inodes.

server4 `/var/tmp`: 105842311168 available bytes; 94.09% used; 114346959 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
