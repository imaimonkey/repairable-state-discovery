# V2R cluster inventory

2026-09-24T02:33:44.941533+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325382250496 available bytes; 81.85% used; 112498838 free inodes.

server1 `/home`: 325382250496 available bytes; 81.85% used; 112498838 free inodes.

server1 `/tmp`: 325382250496 available bytes; 81.85% used; 112498838 free inodes.

server1 `/var/tmp`: 325382250496 available bytes; 81.85% used; 112498838 free inodes.

server1 `/mnt/raid5`: 631861972992 available bytes; 97.10% used; 337733259 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40889847808 available bytes; 97.72% used; 110431512 free inodes.

server2 `/home`: 40889847808 available bytes; 97.72% used; 110431512 free inodes.

server2 `/tmp`: 40889847808 available bytes; 97.72% used; 110431512 free inodes.

server2 `/var/tmp`: 40889847808 available bytes; 97.72% used; 110431512 free inodes.

server2 `/mnt/raid5`: 528892579840 available bytes; 96.35% used; 445199517 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 291857063936 available bytes; 83.71% used; 114163140 free inodes.

server3 `/home`: 291857063936 available bytes; 83.71% used; 114163140 free inodes.

server3 `/data`: 39750705152 available bytes; 99.45% used; 225846297 free inodes.

server3 `/tmp`: 291857063936 available bytes; 83.71% used; 114163140 free inodes.

server3 `/var/tmp`: 291857063936 available bytes; 83.71% used; 114163140 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106003599360 available bytes; 94.08% used; 114349842 free inodes.

server4 `/home`: 106003599360 available bytes; 94.08% used; 114349842 free inodes.

server4 `/data`: 289730498560 available bytes; 96.00% used; 225387448 free inodes.

server4 `/tmp`: 106003599360 available bytes; 94.08% used; 114349842 free inodes.

server4 `/var/tmp`: 106003599360 available bytes; 94.08% used; 114349842 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
