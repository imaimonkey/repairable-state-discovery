# V2R cluster inventory

2026-09-23T23:27:34.269730+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325659656192 available bytes; 81.83% used; 112501523 free inodes.

server1 `/home`: 325659656192 available bytes; 81.83% used; 112501523 free inodes.

server1 `/tmp`: 325659656192 available bytes; 81.83% used; 112501523 free inodes.

server1 `/var/tmp`: 325659656192 available bytes; 81.83% used; 112501523 free inodes.

server1 `/mnt/raid5`: 1370773516288 available bytes; 93.71% used; 337739645 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41044561920 available bytes; 97.71% used; 110432574 free inodes.

server2 `/home`: 41044561920 available bytes; 97.71% used; 110432574 free inodes.

server2 `/tmp`: 41044561920 available bytes; 97.71% used; 110432574 free inodes.

server2 `/var/tmp`: 41044561920 available bytes; 97.71% used; 110432574 free inodes.

server2 `/mnt/raid5`: 534584881152 available bytes; 96.31% used; 445205667 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292861603840 available bytes; 83.66% used; 114212671 free inodes.

server3 `/home`: 292861603840 available bytes; 83.66% used; 114212671 free inodes.

server3 `/data`: 82314444800 available bytes; 98.86% used; 225845816 free inodes.

server3 `/tmp`: 292861603840 available bytes; 83.66% used; 114212671 free inodes.

server3 `/var/tmp`: 292861603840 available bytes; 83.66% used; 114212671 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106235056128 available bytes; 94.07% used; 114352448 free inodes.

server4 `/home`: 106235056128 available bytes; 94.07% used; 114352448 free inodes.

server4 `/data`: 293087703040 available bytes; 95.95% used; 225424612 free inodes.

server4 `/tmp`: 106235056128 available bytes; 94.07% used; 114352448 free inodes.

server4 `/var/tmp`: 106235056128 available bytes; 94.07% used; 114352448 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
