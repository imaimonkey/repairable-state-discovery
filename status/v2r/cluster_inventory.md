# V2R cluster inventory

2026-09-26T20:57:26.795040+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315489009664 available bytes; 82.40% used; 112445678 free inodes.

server1 `/home`: 315489009664 available bytes; 82.40% used; 112445678 free inodes.

server1 `/tmp`: 315489009664 available bytes; 82.40% used; 112445678 free inodes.

server1 `/var/tmp`: 315489009664 available bytes; 82.40% used; 112445678 free inodes.

server1 `/mnt/raid5`: 645853782016 available bytes; 97.04% used; 337467121 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17939394560 available bytes; 99.00% used; 110367547 free inodes.

server2 `/home`: 17939394560 available bytes; 99.00% used; 110367547 free inodes.

server2 `/tmp`: 17939394560 available bytes; 99.00% used; 110367547 free inodes.

server2 `/var/tmp`: 17939394560 available bytes; 99.00% used; 110367547 free inodes.

server2 `/mnt/raid5`: 599631990784 available bytes; 95.86% used; 444963771 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81262100480 available bytes; 95.47% used; 114065291 free inodes.

server3 `/home`: 81262100480 available bytes; 95.47% used; 114065291 free inodes.

server3 `/data`: 1351237165056 available bytes; 81.33% used; 225832505 free inodes.

server3 `/tmp`: 81262100480 available bytes; 95.47% used; 114065291 free inodes.

server3 `/var/tmp`: 81262100480 available bytes; 95.47% used; 114065291 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105918345216 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105918345216 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409923629056 available bytes; 94.33% used; 224823857 free inodes.

server4 `/tmp`: 105918345216 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105918345216 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
