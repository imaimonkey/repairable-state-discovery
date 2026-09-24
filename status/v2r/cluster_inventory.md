# V2R cluster inventory

2026-09-24T02:27:29.262265+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325388099584 available bytes; 81.85% used; 112498901 free inodes.

server1 `/home`: 325388099584 available bytes; 81.85% used; 112498901 free inodes.

server1 `/tmp`: 325388099584 available bytes; 81.85% used; 112498901 free inodes.

server1 `/var/tmp`: 325388099584 available bytes; 81.85% used; 112498901 free inodes.

server1 `/mnt/raid5`: 658572926976 available bytes; 96.98% used; 337733233 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40892071936 available bytes; 97.72% used; 110431558 free inodes.

server2 `/home`: 40892071936 available bytes; 97.72% used; 110431558 free inodes.

server2 `/tmp`: 40892071936 available bytes; 97.72% used; 110431558 free inodes.

server2 `/var/tmp`: 40892071936 available bytes; 97.72% used; 110431558 free inodes.

server2 `/mnt/raid5`: 528565043200 available bytes; 96.35% used; 445199704 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 291857477632 available bytes; 83.71% used; 114163142 free inodes.

server3 `/home`: 291857477632 available bytes; 83.71% used; 114163142 free inodes.

server3 `/data`: 39714447360 available bytes; 99.45% used; 225845145 free inodes.

server3 `/tmp`: 291857477632 available bytes; 83.71% used; 114163142 free inodes.

server3 `/var/tmp`: 291857477632 available bytes; 83.71% used; 114163142 free inodes.
| server4 | True | ['3', '4', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106012254208 available bytes; 94.08% used; 114349855 free inodes.

server4 `/home`: 106012254208 available bytes; 94.08% used; 114349855 free inodes.

server4 `/data`: 289736216576 available bytes; 96.00% used; 225387568 free inodes.

server4 `/tmp`: 106012254208 available bytes; 94.08% used; 114349855 free inodes.

server4 `/var/tmp`: 106012254208 available bytes; 94.08% used; 114349855 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
