# V2R cluster inventory

2026-09-26T02:44:02.827321+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318418788352 available bytes; 82.24% used; 112476255 free inodes.

server1 `/home`: 318418788352 available bytes; 82.24% used; 112476255 free inodes.

server1 `/tmp`: 318418788352 available bytes; 82.24% used; 112476255 free inodes.

server1 `/var/tmp`: 318418788352 available bytes; 82.24% used; 112476255 free inodes.

server1 `/mnt/raid5`: 331124199424 available bytes; 98.48% used; 337546043 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22938140672 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22938140672 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22938140672 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22938140672 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 267929780224 available bytes; 98.15% used; 445053823 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84320436224 available bytes; 95.29% used; 114152370 free inodes.

server3 `/home`: 84320436224 available bytes; 95.29% used; 114152370 free inodes.

server3 `/data`: 124787363840 available bytes; 98.28% used; 225816755 free inodes.

server3 `/tmp`: 84320436224 available bytes; 95.29% used; 114152370 free inodes.

server3 `/var/tmp`: 84320436224 available bytes; 95.29% used; 114152370 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105919352832 available bytes; 94.09% used; 114347153 free inodes.

server4 `/home`: 105919352832 available bytes; 94.09% used; 114347153 free inodes.

server4 `/data`: 109772242944 available bytes; 98.48% used; 224915412 free inodes.

server4 `/tmp`: 105919352832 available bytes; 94.09% used; 114347153 free inodes.

server4 `/var/tmp`: 105919352832 available bytes; 94.09% used; 114347153 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
