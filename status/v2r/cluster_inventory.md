# V2R cluster inventory

2026-09-27T01:41:30.109303+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315143421952 available bytes; 82.42% used; 112443376 free inodes.

server1 `/home`: 315143421952 available bytes; 82.42% used; 112443376 free inodes.

server1 `/tmp`: 315143421952 available bytes; 82.42% used; 112443376 free inodes.

server1 `/var/tmp`: 315143421952 available bytes; 82.42% used; 112443376 free inodes.

server1 `/mnt/raid5`: 637514637312 available bytes; 97.08% used; 337405520 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17627267072 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17627267072 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17627267072 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17627267072 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 582365196288 available bytes; 95.98% used; 444886071 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78862876672 available bytes; 95.60% used; 114064252 free inodes.

server3 `/home`: 78862876672 available bytes; 95.60% used; 114064252 free inodes.

server3 `/data`: 1341937569792 available bytes; 81.45% used; 225763151 free inodes.

server3 `/tmp`: 78862876672 available bytes; 95.60% used; 114064252 free inodes.

server3 `/var/tmp`: 78862876672 available bytes; 95.60% used; 114064252 free inodes.
| server4 | True | ['0', '1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105869176832 available bytes; 94.09% used; 114347846 free inodes.

server4 `/home`: 105869176832 available bytes; 94.09% used; 114347846 free inodes.

server4 `/data`: 406927781888 available bytes; 94.38% used; 224782920 free inodes.

server4 `/tmp`: 105869176832 available bytes; 94.09% used; 114347846 free inodes.

server4 `/var/tmp`: 105869176832 available bytes; 94.09% used; 114347846 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
