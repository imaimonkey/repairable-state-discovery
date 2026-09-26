# V2R cluster inventory

2026-09-26T00:52:38.598385+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318649929728 available bytes; 82.22% used; 112476302 free inodes.

server1 `/home`: 318649929728 available bytes; 82.22% used; 112476302 free inodes.

server1 `/tmp`: 318649929728 available bytes; 82.22% used; 112476302 free inodes.

server1 `/var/tmp`: 318649929728 available bytes; 82.22% used; 112476302 free inodes.

server1 `/mnt/raid5`: 345577807872 available bytes; 98.41% used; 337546725 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22931787776 available bytes; 98.72% used; 110406210 free inodes.

server2 `/home`: 22931787776 available bytes; 98.72% used; 110406210 free inodes.

server2 `/tmp`: 22931787776 available bytes; 98.72% used; 110406210 free inodes.

server2 `/var/tmp`: 22931787776 available bytes; 98.72% used; 110406210 free inodes.

server2 `/mnt/raid5`: 294433648640 available bytes; 97.97% used; 445057016 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340518912 available bytes; 95.29% used; 114152440 free inodes.

server3 `/home`: 84340518912 available bytes; 95.29% used; 114152440 free inodes.

server3 `/data`: 124939067392 available bytes; 98.27% used; 225818672 free inodes.

server3 `/tmp`: 84340518912 available bytes; 95.29% used; 114152440 free inodes.

server3 `/var/tmp`: 84340518912 available bytes; 95.29% used; 114152440 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105349148672 available bytes; 94.12% used; 114347253 free inodes.

server4 `/home`: 105349148672 available bytes; 94.12% used; 114347253 free inodes.

server4 `/data`: 148680196096 available bytes; 97.95% used; 224917376 free inodes.

server4 `/tmp`: 105349148672 available bytes; 94.12% used; 114347253 free inodes.

server4 `/var/tmp`: 105349148672 available bytes; 94.12% used; 114347253 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
