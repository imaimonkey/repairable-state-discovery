# V2R cluster inventory

2026-09-23T22:30:09.299365+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325695447040 available bytes; 81.83% used; 112501389 free inodes.

server1 `/home`: 325695447040 available bytes; 81.83% used; 112501389 free inodes.

server1 `/tmp`: 325695447040 available bytes; 81.83% used; 112501389 free inodes.

server1 `/var/tmp`: 325695447040 available bytes; 81.83% used; 112501389 free inodes.

server1 `/mnt/raid5`: 1388095856640 available bytes; 93.63% used; 337739842 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41082679296 available bytes; 97.71% used; 110432629 free inodes.

server2 `/home`: 41082679296 available bytes; 97.71% used; 110432629 free inodes.

server2 `/tmp`: 41082679296 available bytes; 97.71% used; 110432629 free inodes.

server2 `/var/tmp`: 41082679296 available bytes; 97.71% used; 110432629 free inodes.

server2 `/mnt/raid5`: 536658120704 available bytes; 96.29% used; 445206740 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293041704960 available bytes; 83.65% used; 114223439 free inodes.

server3 `/home`: 293041704960 available bytes; 83.65% used; 114223439 free inodes.

server3 `/data`: 82432241664 available bytes; 98.86% used; 225847370 free inodes.

server3 `/tmp`: 293041704960 available bytes; 83.65% used; 114223439 free inodes.

server3 `/var/tmp`: 293041704960 available bytes; 83.65% used; 114223439 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106381512704 available bytes; 94.06% used; 114354531 free inodes.

server4 `/home`: 106381512704 available bytes; 94.06% used; 114354531 free inodes.

server4 `/data`: 300077076480 available bytes; 95.85% used; 225437159 free inodes.

server4 `/tmp`: 106381512704 available bytes; 94.06% used; 114354531 free inodes.

server4 `/var/tmp`: 106381512704 available bytes; 94.06% used; 114354531 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
