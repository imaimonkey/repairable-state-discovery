# V2R cluster inventory

2026-09-23T23:01:22.643440+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325743087616 available bytes; 81.83% used; 112501691 free inodes.

server1 `/home`: 325743087616 available bytes; 81.83% used; 112501691 free inodes.

server1 `/tmp`: 325743087616 available bytes; 81.83% used; 112501691 free inodes.

server1 `/var/tmp`: 325743087616 available bytes; 81.83% used; 112501691 free inodes.

server1 `/mnt/raid5`: 1387997491200 available bytes; 93.63% used; 337739796 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41060642816 available bytes; 97.71% used; 110432611 free inodes.

server2 `/home`: 41060642816 available bytes; 97.71% used; 110432611 free inodes.

server2 `/tmp`: 41060642816 available bytes; 97.71% used; 110432611 free inodes.

server2 `/var/tmp`: 41060642816 available bytes; 97.71% used; 110432611 free inodes.

server2 `/mnt/raid5`: 535358291968 available bytes; 96.30% used; 445206069 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292830490624 available bytes; 83.66% used; 114213555 free inodes.

server3 `/home`: 292830490624 available bytes; 83.66% used; 114213555 free inodes.

server3 `/data`: 82346856448 available bytes; 98.86% used; 225846636 free inodes.

server3 `/tmp`: 292830490624 available bytes; 83.66% used; 114213555 free inodes.

server3 `/var/tmp`: 292830490624 available bytes; 83.66% used; 114213555 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106294087680 available bytes; 94.07% used; 114353403 free inodes.

server4 `/home`: 106294087680 available bytes; 94.07% used; 114353403 free inodes.

server4 `/data`: 300073500672 available bytes; 95.85% used; 225431834 free inodes.

server4 `/tmp`: 106294087680 available bytes; 94.07% used; 114353403 free inodes.

server4 `/var/tmp`: 106294087680 available bytes; 94.07% used; 114353403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
