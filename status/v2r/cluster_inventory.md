# V2R cluster inventory

2026-09-26T03:31:23.745949+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318417072128 available bytes; 82.24% used; 112476258 free inodes.

server1 `/home`: 318417072128 available bytes; 82.24% used; 112476258 free inodes.

server1 `/tmp`: 318417072128 available bytes; 82.24% used; 112476258 free inodes.

server1 `/var/tmp`: 318417072128 available bytes; 82.24% used; 112476258 free inodes.

server1 `/mnt/raid5`: 331017084928 available bytes; 98.48% used; 337545816 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22932295680 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22932295680 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22932295680 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22932295680 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 287193186304 available bytes; 98.02% used; 445052498 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84307943424 available bytes; 95.30% used; 114152360 free inodes.

server3 `/home`: 84307943424 available bytes; 95.30% used; 114152360 free inodes.

server3 `/data`: 125425491968 available bytes; 98.27% used; 225830602 free inodes.

server3 `/tmp`: 84307943424 available bytes; 95.30% used; 114152360 free inodes.

server3 `/var/tmp`: 84307943424 available bytes; 95.30% used; 114152360 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105800220672 available bytes; 94.10% used; 114346872 free inodes.

server4 `/home`: 105800220672 available bytes; 94.10% used; 114346872 free inodes.

server4 `/data`: 108927111168 available bytes; 98.49% used; 224914757 free inodes.

server4 `/tmp`: 105800220672 available bytes; 94.10% used; 114346872 free inodes.

server4 `/var/tmp`: 105800220672 available bytes; 94.10% used; 114346872 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
