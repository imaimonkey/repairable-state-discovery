# V2R cluster inventory

2026-09-26T11:16:55.954752+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318217031680 available bytes; 82.25% used; 112474824 free inodes.

server1 `/home`: 318217031680 available bytes; 82.25% used; 112474824 free inodes.

server1 `/tmp`: 318217031680 available bytes; 82.25% used; 112474824 free inodes.

server1 `/var/tmp`: 318217031680 available bytes; 82.25% used; 112474824 free inodes.

server1 `/mnt/raid5`: 218725740544 available bytes; 99.00% used; 337538133 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19843796992 available bytes; 98.89% used; 110384879 free inodes.

server2 `/home`: 19843796992 available bytes; 98.89% used; 110384879 free inodes.

server2 `/tmp`: 19843796992 available bytes; 98.89% used; 110384879 free inodes.

server2 `/var/tmp`: 19843796992 available bytes; 98.89% used; 110384879 free inodes.

server2 `/mnt/raid5`: 241292173312 available bytes; 98.33% used; 444978617 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82648674304 available bytes; 95.39% used; 114110811 free inodes.

server3 `/home`: 82648674304 available bytes; 95.39% used; 114110811 free inodes.

server3 `/data`: 123570565120 available bytes; 98.29% used; 225825726 free inodes.

server3 `/tmp`: 82648674304 available bytes; 95.39% used; 114110811 free inodes.

server3 `/var/tmp`: 82648674304 available bytes; 95.39% used; 114110811 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105925095424 available bytes; 94.09% used; 114347941 free inodes.

server4 `/home`: 105925095424 available bytes; 94.09% used; 114347941 free inodes.

server4 `/data`: 88800669696 available bytes; 98.77% used; 224880358 free inodes.

server4 `/tmp`: 105925095424 available bytes; 94.09% used; 114347941 free inodes.

server4 `/var/tmp`: 105925095424 available bytes; 94.09% used; 114347941 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
