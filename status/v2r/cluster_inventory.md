# V2R cluster inventory

2026-09-26T03:19:11.156480+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318416916480 available bytes; 82.24% used; 112476258 free inodes.

server1 `/home`: 318416916480 available bytes; 82.24% used; 112476258 free inodes.

server1 `/tmp`: 318416916480 available bytes; 82.24% used; 112476258 free inodes.

server1 `/var/tmp`: 318416916480 available bytes; 82.24% used; 112476258 free inodes.

server1 `/mnt/raid5`: 331039760384 available bytes; 98.48% used; 337545860 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22933839872 available bytes; 98.72% used; 110406210 free inodes.

server2 `/home`: 22933839872 available bytes; 98.72% used; 110406210 free inodes.

server2 `/tmp`: 22933839872 available bytes; 98.72% used; 110406210 free inodes.

server2 `/var/tmp`: 22933839872 available bytes; 98.72% used; 110406210 free inodes.

server2 `/mnt/raid5`: 287550750720 available bytes; 98.01% used; 445052723 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84309037056 available bytes; 95.30% used; 114152362 free inodes.

server3 `/home`: 84309037056 available bytes; 95.30% used; 114152362 free inodes.

server3 `/data`: 125432877056 available bytes; 98.27% used; 225830794 free inodes.

server3 `/tmp`: 84309037056 available bytes; 95.30% used; 114152362 free inodes.

server3 `/var/tmp`: 84309037056 available bytes; 95.30% used; 114152362 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105918144512 available bytes; 94.09% used; 114347133 free inodes.

server4 `/home`: 105918144512 available bytes; 94.09% used; 114347133 free inodes.

server4 `/data`: 108981997568 available bytes; 98.49% used; 224914832 free inodes.

server4 `/tmp`: 105918144512 available bytes; 94.09% used; 114347133 free inodes.

server4 `/var/tmp`: 105918144512 available bytes; 94.09% used; 114347133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
