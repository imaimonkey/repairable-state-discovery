# V2R cluster inventory

2026-09-25T14:49:14.919210+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319159316480 available bytes; 82.20% used; 112476976 free inodes.

server1 `/home`: 319159316480 available bytes; 82.20% used; 112476976 free inodes.

server1 `/tmp`: 319159316480 available bytes; 82.20% used; 112476976 free inodes.

server1 `/var/tmp`: 319159316480 available bytes; 82.20% used; 112476976 free inodes.

server1 `/mnt/raid5`: 366923829248 available bytes; 98.32% used; 337546744 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 14380830720 available bytes; 99.20% used; 110407663 free inodes.

server2 `/home`: 14380830720 available bytes; 99.20% used; 110407663 free inodes.

server2 `/tmp`: 14380830720 available bytes; 99.20% used; 110407663 free inodes.

server2 `/var/tmp`: 14380830720 available bytes; 99.20% used; 110407663 free inodes.

server2 `/mnt/raid5`: 321107279872 available bytes; 97.78% used; 445074337 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84264398848 available bytes; 95.30% used; 114154466 free inodes.

server3 `/home`: 84264398848 available bytes; 95.30% used; 114154466 free inodes.

server3 `/data`: 142197862400 available bytes; 98.03% used; 225808393 free inodes.

server3 `/tmp`: 84264398848 available bytes; 95.30% used; 114154466 free inodes.

server3 `/var/tmp`: 84264398848 available bytes; 95.30% used; 114154466 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105645432832 available bytes; 94.10% used; 114349709 free inodes.

server4 `/home`: 105645432832 available bytes; 94.10% used; 114349709 free inodes.

server4 `/data`: 231424790528 available bytes; 96.80% used; 224945565 free inodes.

server4 `/tmp`: 105645432832 available bytes; 94.10% used; 114349709 free inodes.

server4 `/var/tmp`: 105645432832 available bytes; 94.10% used; 114349709 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
