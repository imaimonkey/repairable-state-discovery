# V2R cluster inventory

2026-09-23T23:39:53.741607+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325613047808 available bytes; 81.84% used; 112501213 free inodes.

server1 `/home`: 325613047808 available bytes; 81.84% used; 112501213 free inodes.

server1 `/tmp`: 325613047808 available bytes; 81.84% used; 112501213 free inodes.

server1 `/var/tmp`: 325613047808 available bytes; 81.84% used; 112501213 free inodes.

server1 `/mnt/raid5`: 1352060698624 available bytes; 93.80% used; 337735811 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41035059200 available bytes; 97.71% used; 110432534 free inodes.

server2 `/home`: 41035059200 available bytes; 97.71% used; 110432534 free inodes.

server2 `/tmp`: 41035059200 available bytes; 97.71% used; 110432534 free inodes.

server2 `/var/tmp`: 41035059200 available bytes; 97.71% used; 110432534 free inodes.

server2 `/mnt/raid5`: 534142803968 available bytes; 96.31% used; 445204859 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292529508352 available bytes; 83.68% used; 114192616 free inodes.

server3 `/home`: 292529508352 available bytes; 83.68% used; 114192616 free inodes.

server3 `/data`: 82306867200 available bytes; 98.86% used; 225845580 free inodes.

server3 `/tmp`: 292529508352 available bytes; 83.68% used; 114192616 free inodes.

server3 `/var/tmp`: 292529508352 available bytes; 83.68% used; 114192616 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106198994944 available bytes; 94.07% used; 114352011 free inodes.

server4 `/home`: 106198994944 available bytes; 94.07% used; 114352011 free inodes.

server4 `/data`: 293003145216 available bytes; 95.95% used; 225420944 free inodes.

server4 `/tmp`: 106198994944 available bytes; 94.07% used; 114352011 free inodes.

server4 `/var/tmp`: 106198994944 available bytes; 94.07% used; 114352011 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
