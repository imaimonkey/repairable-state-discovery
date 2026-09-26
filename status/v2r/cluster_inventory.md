# V2R cluster inventory

2026-09-26T03:16:08.075660+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318417555456 available bytes; 82.24% used; 112476258 free inodes.

server1 `/home`: 318417555456 available bytes; 82.24% used; 112476258 free inodes.

server1 `/tmp`: 318417555456 available bytes; 82.24% used; 112476258 free inodes.

server1 `/var/tmp`: 318417555456 available bytes; 82.24% used; 112476258 free inodes.

server1 `/mnt/raid5`: 331051233280 available bytes; 98.48% used; 337545889 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22941900800 available bytes; 98.72% used; 110406210 free inodes.

server2 `/home`: 22941900800 available bytes; 98.72% used; 110406210 free inodes.

server2 `/tmp`: 22941900800 available bytes; 98.72% used; 110406210 free inodes.

server2 `/var/tmp`: 22941900800 available bytes; 98.72% used; 110406210 free inodes.

server2 `/mnt/raid5`: 287633969152 available bytes; 98.01% used; 445052744 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84310061056 available bytes; 95.30% used; 114152357 free inodes.

server3 `/home`: 84310061056 available bytes; 95.30% used; 114152357 free inodes.

server3 `/data`: 125434507264 available bytes; 98.27% used; 225830848 free inodes.

server3 `/tmp`: 84310061056 available bytes; 95.30% used; 114152357 free inodes.

server3 `/var/tmp`: 84310061056 available bytes; 95.30% used; 114152357 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105920282624 available bytes; 94.09% used; 114347143 free inodes.

server4 `/home`: 105920282624 available bytes; 94.09% used; 114347143 free inodes.

server4 `/data`: 109005414400 available bytes; 98.49% used; 224914840 free inodes.

server4 `/tmp`: 105920282624 available bytes; 94.09% used; 114347143 free inodes.

server4 `/var/tmp`: 105920282624 available bytes; 94.09% used; 114347143 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
