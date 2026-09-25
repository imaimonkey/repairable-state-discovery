# V2R cluster inventory

2026-09-25T15:24:27.493429+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319043719168 available bytes; 82.20% used; 112476401 free inodes.

server1 `/home`: 319043719168 available bytes; 82.20% used; 112476401 free inodes.

server1 `/tmp`: 319043719168 available bytes; 82.20% used; 112476401 free inodes.

server1 `/var/tmp`: 319043719168 available bytes; 82.20% used; 112476401 free inodes.

server1 `/mnt/raid5`: 363987927040 available bytes; 98.33% used; 337545329 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23114526720 available bytes; 98.71% used; 110407942 free inodes.

server2 `/home`: 23114526720 available bytes; 98.71% used; 110407942 free inodes.

server2 `/tmp`: 23114526720 available bytes; 98.71% used; 110407942 free inodes.

server2 `/var/tmp`: 23114526720 available bytes; 98.71% used; 110407942 free inodes.

server2 `/mnt/raid5`: 320113553408 available bytes; 97.79% used; 445072986 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84424019968 available bytes; 95.29% used; 114153457 free inodes.

server3 `/home`: 84424019968 available bytes; 95.29% used; 114153457 free inodes.

server3 `/data`: 142174031872 available bytes; 98.04% used; 225807833 free inodes.

server3 `/tmp`: 84424019968 available bytes; 95.29% used; 114153457 free inodes.

server3 `/var/tmp`: 84424019968 available bytes; 95.29% used; 114153457 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638010880 available bytes; 94.11% used; 114349678 free inodes.

server4 `/home`: 105638010880 available bytes; 94.11% used; 114349678 free inodes.

server4 `/data`: 231360753664 available bytes; 96.80% used; 224944117 free inodes.

server4 `/tmp`: 105638010880 available bytes; 94.11% used; 114349678 free inodes.

server4 `/var/tmp`: 105638010880 available bytes; 94.11% used; 114349678 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
