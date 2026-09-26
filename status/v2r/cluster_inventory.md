# V2R cluster inventory

2026-09-26T12:40:50.368829+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318161981440 available bytes; 82.25% used; 112474497 free inodes.

server1 `/home`: 318161981440 available bytes; 82.25% used; 112474497 free inodes.

server1 `/tmp`: 318161981440 available bytes; 82.25% used; 112474497 free inodes.

server1 `/var/tmp`: 318161981440 available bytes; 82.25% used; 112474497 free inodes.

server1 `/mnt/raid5`: 679658270720 available bytes; 96.88% used; 337537816 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 15518597120 available bytes; 99.13% used; 110381968 free inodes.

server2 `/home`: 15518597120 available bytes; 99.13% used; 110381968 free inodes.

server2 `/tmp`: 15518597120 available bytes; 99.13% used; 110381968 free inodes.

server2 `/var/tmp`: 15518597120 available bytes; 99.13% used; 110381968 free inodes.

server2 `/mnt/raid5`: 652916023296 available bytes; 95.49% used; 444978844 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82648973312 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82648973312 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123397804032 available bytes; 98.29% used; 225823466 free inodes.

server3 `/tmp`: 82648973312 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82648973312 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105899479040 available bytes; 94.09% used; 114347942 free inodes.

server4 `/home`: 105899479040 available bytes; 94.09% used; 114347942 free inodes.

server4 `/data`: 88529174528 available bytes; 98.78% used; 224878821 free inodes.

server4 `/tmp`: 105899479040 available bytes; 94.09% used; 114347942 free inodes.

server4 `/var/tmp`: 105899479040 available bytes; 94.09% used; 114347942 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
