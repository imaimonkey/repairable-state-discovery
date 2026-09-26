# V2R cluster inventory

2026-09-26T21:09:37.672632+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315481956352 available bytes; 82.40% used; 112445689 free inodes.

server1 `/home`: 315481956352 available bytes; 82.40% used; 112445689 free inodes.

server1 `/tmp`: 315481956352 available bytes; 82.40% used; 112445689 free inodes.

server1 `/var/tmp`: 315481956352 available bytes; 82.40% used; 112445689 free inodes.

server1 `/mnt/raid5`: 645854875648 available bytes; 97.04% used; 337467123 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17938812928 available bytes; 99.00% used; 110367527 free inodes.

server2 `/home`: 17938812928 available bytes; 99.00% used; 110367527 free inodes.

server2 `/tmp`: 17938812928 available bytes; 99.00% used; 110367527 free inodes.

server2 `/var/tmp`: 17938812928 available bytes; 99.00% used; 110367527 free inodes.

server2 `/mnt/raid5`: 599285604352 available bytes; 95.86% used; 444963578 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81266692096 available bytes; 95.47% used; 114065308 free inodes.

server3 `/home`: 81266692096 available bytes; 95.47% used; 114065308 free inodes.

server3 `/data`: 1351145586688 available bytes; 81.33% used; 225831940 free inodes.

server3 `/tmp`: 81266692096 available bytes; 95.47% used; 114065308 free inodes.

server3 `/var/tmp`: 81266692096 available bytes; 95.47% used; 114065308 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105918029824 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105918029824 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409919942656 available bytes; 94.33% used; 224823841 free inodes.

server4 `/tmp`: 105918029824 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105918029824 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
