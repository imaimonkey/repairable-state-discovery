# V2R cluster inventory

2026-09-24T18:12:20.958729+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324006883328 available bytes; 81.92% used; 112481437 free inodes.

server1 `/home`: 324006883328 available bytes; 81.92% used; 112481437 free inodes.

server1 `/tmp`: 324006883328 available bytes; 81.92% used; 112481437 free inodes.

server1 `/var/tmp`: 324006883328 available bytes; 81.92% used; 112481437 free inodes.

server1 `/mnt/raid5`: 416360181760 available bytes; 98.09% used; 337641459 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54505504768 available bytes; 96.96% used; 110412079 free inodes.

server2 `/home`: 54505504768 available bytes; 96.96% used; 110412079 free inodes.

server2 `/tmp`: 54505504768 available bytes; 96.96% used; 110412079 free inodes.

server2 `/var/tmp`: 54505504768 available bytes; 96.96% used; 110412079 free inodes.

server2 `/mnt/raid5`: 497257758720 available bytes; 96.56% used; 445160944 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84408147968 available bytes; 95.29% used; 114156129 free inodes.

server3 `/home`: 84408147968 available bytes; 95.29% used; 114156129 free inodes.

server3 `/data`: 153096261632 available bytes; 97.88% used; 225800864 free inodes.

server3 `/tmp`: 84408147968 available bytes; 95.29% used; 114156129 free inodes.

server3 `/var/tmp`: 84408147968 available bytes; 95.29% used; 114156129 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105663119360 available bytes; 94.10% used; 114348526 free inodes.

server4 `/home`: 105663119360 available bytes; 94.10% used; 114348526 free inodes.

server4 `/data`: 90078687232 available bytes; 98.76% used; 225268102 free inodes.

server4 `/tmp`: 105663119360 available bytes; 94.10% used; 114348526 free inodes.

server4 `/var/tmp`: 105663119360 available bytes; 94.10% used; 114348526 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
