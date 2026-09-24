# V2R cluster inventory

2026-09-24T05:55:45.078217+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324534013952 available bytes; 81.90% used; 112492001 free inodes.

server1 `/home`: 324534013952 available bytes; 81.90% used; 112492001 free inodes.

server1 `/tmp`: 324534013952 available bytes; 81.90% used; 112492001 free inodes.

server1 `/var/tmp`: 324534013952 available bytes; 81.90% used; 112492001 free inodes.

server1 `/mnt/raid5`: 517606359040 available bytes; 97.63% used; 337723860 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57905455104 available bytes; 96.77% used; 110431308 free inodes.

server2 `/home`: 57905455104 available bytes; 96.77% used; 110431308 free inodes.

server2 `/tmp`: 57905455104 available bytes; 96.77% used; 110431308 free inodes.

server2 `/var/tmp`: 57905455104 available bytes; 96.77% used; 110431308 free inodes.

server2 `/mnt/raid5`: 521312641024 available bytes; 96.40% used; 445193078 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127190171648 available bytes; 92.90% used; 114198212 free inodes.

server3 `/home`: 127190171648 available bytes; 92.90% used; 114198212 free inodes.

server3 `/data`: 185866477568 available bytes; 97.43% used; 225838569 free inodes.

server3 `/tmp`: 127190171648 available bytes; 92.90% used; 114198212 free inodes.

server3 `/var/tmp`: 127190171648 available bytes; 92.90% used; 114198212 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105815773184 available bytes; 94.10% used; 114349341 free inodes.

server4 `/home`: 105815773184 available bytes; 94.10% used; 114349341 free inodes.

server4 `/data`: 252146634752 available bytes; 96.52% used; 225357907 free inodes.

server4 `/tmp`: 105815773184 available bytes; 94.10% used; 114349341 free inodes.

server4 `/var/tmp`: 105815773184 available bytes; 94.10% used; 114349341 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
