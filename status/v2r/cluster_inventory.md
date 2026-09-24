# V2R cluster inventory

2026-09-24T04:04:07.418837+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324719656960 available bytes; 81.89% used; 112493497 free inodes.

server1 `/home`: 324719656960 available bytes; 81.89% used; 112493497 free inodes.

server1 `/tmp`: 324719656960 available bytes; 81.89% used; 112493497 free inodes.

server1 `/var/tmp`: 324719656960 available bytes; 81.89% used; 112493497 free inodes.

server1 `/mnt/raid5`: 416633544704 available bytes; 98.09% used; 337724763 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40805318656 available bytes; 97.72% used; 110430846 free inodes.

server2 `/home`: 40805318656 available bytes; 97.72% used; 110430846 free inodes.

server2 `/tmp`: 40805318656 available bytes; 97.72% used; 110430846 free inodes.

server2 `/var/tmp`: 40805318656 available bytes; 97.72% used; 110430846 free inodes.

server2 `/mnt/raid5`: 526154207232 available bytes; 96.36% used; 445196671 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291935117312 available bytes; 83.71% used; 114175157 free inodes.

server3 `/home`: 291935117312 available bytes; 83.71% used; 114175157 free inodes.

server3 `/data`: 31742447616 available bytes; 99.56% used; 225841982 free inodes.

server3 `/tmp`: 291935117312 available bytes; 83.71% used; 114175157 free inodes.

server3 `/var/tmp`: 291935117312 available bytes; 83.71% used; 114175157 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105791193088 available bytes; 94.10% used; 114349500 free inodes.

server4 `/home`: 105791193088 available bytes; 94.10% used; 114349500 free inodes.

server4 `/data`: 256728424448 available bytes; 96.45% used; 225381892 free inodes.

server4 `/tmp`: 105791193088 available bytes; 94.10% used; 114349500 free inodes.

server4 `/var/tmp`: 105791193088 available bytes; 94.10% used; 114349500 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
