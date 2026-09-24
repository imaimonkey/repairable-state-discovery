# V2R cluster inventory

2026-09-24T18:49:19.263940+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324006416384 available bytes; 81.92% used; 112481448 free inodes.

server1 `/home`: 324006416384 available bytes; 81.92% used; 112481448 free inodes.

server1 `/tmp`: 324006416384 available bytes; 81.92% used; 112481448 free inodes.

server1 `/var/tmp`: 324006416384 available bytes; 81.92% used; 112481448 free inodes.

server1 `/mnt/raid5`: 416277966848 available bytes; 98.09% used; 337637149 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54478131200 available bytes; 96.96% used; 110411940 free inodes.

server2 `/home`: 54478131200 available bytes; 96.96% used; 110411940 free inodes.

server2 `/tmp`: 54478131200 available bytes; 96.96% used; 110411940 free inodes.

server2 `/var/tmp`: 54478131200 available bytes; 96.96% used; 110411940 free inodes.

server2 `/mnt/raid5`: 496137871360 available bytes; 96.57% used; 445160042 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84407517184 available bytes; 95.29% used; 114156135 free inodes.

server3 `/home`: 84407517184 available bytes; 95.29% used; 114156135 free inodes.

server3 `/data`: 152700289024 available bytes; 97.89% used; 225800191 free inodes.

server3 `/tmp`: 84407517184 available bytes; 95.29% used; 114156135 free inodes.

server3 `/var/tmp`: 84407517184 available bytes; 95.29% used; 114156135 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105661489152 available bytes; 94.10% used; 114348489 free inodes.

server4 `/home`: 105661489152 available bytes; 94.10% used; 114348489 free inodes.

server4 `/data`: 90014265344 available bytes; 98.76% used; 225267597 free inodes.

server4 `/tmp`: 105661489152 available bytes; 94.10% used; 114348489 free inodes.

server4 `/var/tmp`: 105661489152 available bytes; 94.10% used; 114348489 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
