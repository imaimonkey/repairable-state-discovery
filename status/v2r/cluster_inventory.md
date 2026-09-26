# V2R cluster inventory

2026-09-26T03:29:52.166350+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318417256448 available bytes; 82.24% used; 112476258 free inodes.

server1 `/home`: 318417256448 available bytes; 82.24% used; 112476258 free inodes.

server1 `/tmp`: 318417256448 available bytes; 82.24% used; 112476258 free inodes.

server1 `/var/tmp`: 318417256448 available bytes; 82.24% used; 112476258 free inodes.

server1 `/mnt/raid5`: 331021635584 available bytes; 98.48% used; 337545824 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22932623360 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22932623360 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22932623360 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22932623360 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 287259254784 available bytes; 98.02% used; 445052678 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84308303872 available bytes; 95.30% used; 114152360 free inodes.

server3 `/home`: 84308303872 available bytes; 95.30% used; 114152360 free inodes.

server3 `/data`: 125426225152 available bytes; 98.27% used; 225830620 free inodes.

server3 `/tmp`: 84308303872 available bytes; 95.30% used; 114152360 free inodes.

server3 `/var/tmp`: 84308303872 available bytes; 95.30% used; 114152360 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105833836544 available bytes; 94.09% used; 114346958 free inodes.

server4 `/home`: 105833836544 available bytes; 94.09% used; 114346958 free inodes.

server4 `/data`: 108926058496 available bytes; 98.49% used; 224914763 free inodes.

server4 `/tmp`: 105833836544 available bytes; 94.09% used; 114346958 free inodes.

server4 `/var/tmp`: 105833836544 available bytes; 94.09% used; 114346958 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
