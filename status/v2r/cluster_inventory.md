# V2R cluster inventory

2026-09-23T18:58:54.957496+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['6', '7'] | [] | reference_compatible=False |

server2 `/`: 41341231104 available bytes; 97.69% used; 110435448 free inodes.

server2 `/home`: 41341231104 available bytes; 97.69% used; 110435448 free inodes.

server2 `/tmp`: 41341231104 available bytes; 97.69% used; 110435448 free inodes.

server2 `/var/tmp`: 41341231104 available bytes; 97.69% used; 110435448 free inodes.

server2 `/mnt/raid5`: 544103968768 available bytes; 96.24% used; 445213594 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293880098816 available bytes; 83.60% used; 114251060 free inodes.

server3 `/home`: 293880098816 available bytes; 83.60% used; 114251060 free inodes.

server3 `/data`: 52810792960 available bytes; 99.27% used; 225846503 free inodes.

server3 `/tmp`: 293880098816 available bytes; 83.60% used; 114251060 free inodes.

server3 `/var/tmp`: 293880098816 available bytes; 83.60% used; 114251060 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110497976320 available bytes; 93.83% used; 114372663 free inodes.

server4 `/home`: 110497976320 available bytes; 93.83% used; 114372663 free inodes.

server4 `/data`: 15069184 available bytes; 100.00% used; 225458130 free inodes.

server4 `/tmp`: 110497976320 available bytes; 93.83% used; 114372663 free inodes.

server4 `/var/tmp`: 110497976320 available bytes; 93.83% used; 114372663 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
