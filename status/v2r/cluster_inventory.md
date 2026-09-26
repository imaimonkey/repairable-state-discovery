# V2R cluster inventory

2026-09-26T04:03:26.565609+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318416359424 available bytes; 82.24% used; 112476268 free inodes.

server1 `/home`: 318416359424 available bytes; 82.24% used; 112476268 free inodes.

server1 `/tmp`: 318416359424 available bytes; 82.24% used; 112476268 free inodes.

server1 `/var/tmp`: 318416359424 available bytes; 82.24% used; 112476268 free inodes.

server1 `/mnt/raid5`: 330580905984 available bytes; 98.48% used; 337545596 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22931091456 available bytes; 98.72% used; 110406198 free inodes.

server2 `/home`: 22931091456 available bytes; 98.72% used; 110406198 free inodes.

server2 `/tmp`: 22931091456 available bytes; 98.72% used; 110406198 free inodes.

server2 `/var/tmp`: 22931091456 available bytes; 98.72% used; 110406198 free inodes.

server2 `/mnt/raid5`: 286256054272 available bytes; 98.02% used; 445051387 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83982704640 available bytes; 95.31% used; 114143619 free inodes.

server3 `/home`: 83982704640 available bytes; 95.31% used; 114143619 free inodes.

server3 `/data`: 124587061248 available bytes; 98.28% used; 225819984 free inodes.

server3 `/tmp`: 83982704640 available bytes; 95.31% used; 114143619 free inodes.

server3 `/var/tmp`: 83982704640 available bytes; 95.31% used; 114143619 free inodes.
| server4 | True | ['2', '3', '4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106003275776 available bytes; 94.08% used; 114348222 free inodes.

server4 `/home`: 106003275776 available bytes; 94.08% used; 114348222 free inodes.

server4 `/data`: 109678260224 available bytes; 98.48% used; 224929433 free inodes.

server4 `/tmp`: 106003275776 available bytes; 94.08% used; 114348222 free inodes.

server4 `/var/tmp`: 106003275776 available bytes; 94.08% used; 114348222 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
