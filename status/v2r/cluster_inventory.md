# V2R cluster inventory

2026-09-24T14:45:56.962158+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324050776064 available bytes; 81.92% used; 112481473 free inodes.

server1 `/home`: 324050776064 available bytes; 81.92% used; 112481473 free inodes.

server1 `/tmp`: 324050776064 available bytes; 81.92% used; 112481473 free inodes.

server1 `/var/tmp`: 324050776064 available bytes; 81.92% used; 112481473 free inodes.

server1 `/mnt/raid5`: 416856711168 available bytes; 98.09% used; 337666353 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57439289344 available bytes; 96.80% used; 110427949 free inodes.

server2 `/home`: 57439289344 available bytes; 96.80% used; 110427949 free inodes.

server2 `/tmp`: 57439289344 available bytes; 96.80% used; 110427949 free inodes.

server2 `/var/tmp`: 57439289344 available bytes; 96.80% used; 110427949 free inodes.

server2 `/mnt/raid5`: 503469051904 available bytes; 96.52% used; 445167600 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84846505984 available bytes; 95.27% used; 114183440 free inodes.

server3 `/home`: 84846505984 available bytes; 95.27% used; 114183440 free inodes.

server3 `/data`: 160716320768 available bytes; 97.78% used; 225807822 free inodes.

server3 `/tmp`: 84846505984 available bytes; 95.27% used; 114183440 free inodes.

server3 `/var/tmp`: 84846505984 available bytes; 95.27% used; 114183440 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105758330880 available bytes; 94.10% used; 114348683 free inodes.

server4 `/home`: 105758330880 available bytes; 94.10% used; 114348683 free inodes.

server4 `/data`: 69176279040 available bytes; 99.04% used; 225257002 free inodes.

server4 `/tmp`: 105758330880 available bytes; 94.10% used; 114348683 free inodes.

server4 `/var/tmp`: 105758330880 available bytes; 94.10% used; 114348683 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
