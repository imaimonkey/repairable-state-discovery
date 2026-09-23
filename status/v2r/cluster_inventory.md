# V2R cluster inventory

2026-09-23T21:30:30.171094+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325718257664 available bytes; 81.83% used; 112501427 free inodes.

server1 `/home`: 325718257664 available bytes; 81.83% used; 112501427 free inodes.

server1 `/tmp`: 325718257664 available bytes; 81.83% used; 112501427 free inodes.

server1 `/var/tmp`: 325718257664 available bytes; 81.83% used; 112501427 free inodes.

server1 `/mnt/raid5`: 1388140482560 available bytes; 93.63% used; 337739956 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41128529920 available bytes; 97.71% used; 110432694 free inodes.

server2 `/home`: 41128529920 available bytes; 97.71% used; 110432694 free inodes.

server2 `/tmp`: 41128529920 available bytes; 97.71% used; 110432694 free inodes.

server2 `/var/tmp`: 41128529920 available bytes; 97.71% used; 110432694 free inodes.

server2 `/mnt/raid5`: 538495438848 available bytes; 96.28% used; 445208589 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293246513152 available bytes; 83.64% used; 114229091 free inodes.

server3 `/home`: 293246513152 available bytes; 83.64% used; 114229091 free inodes.

server3 `/data`: 52277735424 available bytes; 99.28% used; 225848796 free inodes.

server3 `/tmp`: 293246513152 available bytes; 83.64% used; 114229091 free inodes.

server3 `/var/tmp`: 293246513152 available bytes; 83.64% used; 114229091 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106480726016 available bytes; 94.06% used; 114356001 free inodes.

server4 `/home`: 106480726016 available bytes; 94.06% used; 114356001 free inodes.

server4 `/data`: 300321349632 available bytes; 95.85% used; 225450825 free inodes.

server4 `/tmp`: 106480726016 available bytes; 94.06% used; 114356001 free inodes.

server4 `/var/tmp`: 106480726016 available bytes; 94.06% used; 114356001 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
