# V2R cluster inventory

2026-09-23T21:01:15.325981+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325723725824 available bytes; 81.83% used; 112501611 free inodes.

server1 `/home`: 325723725824 available bytes; 81.83% used; 112501611 free inodes.

server1 `/tmp`: 325723725824 available bytes; 81.83% used; 112501611 free inodes.

server1 `/var/tmp`: 325723725824 available bytes; 81.83% used; 112501611 free inodes.

server1 `/mnt/raid5`: 1388140433408 available bytes; 93.63% used; 337739997 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41123192832 available bytes; 97.71% used; 110432719 free inodes.

server2 `/home`: 41123192832 available bytes; 97.71% used; 110432719 free inodes.

server2 `/tmp`: 41123192832 available bytes; 97.71% used; 110432719 free inodes.

server2 `/var/tmp`: 41123192832 available bytes; 97.71% used; 110432719 free inodes.

server2 `/mnt/raid5`: 539410219008 available bytes; 96.27% used; 445209993 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293463740416 available bytes; 83.62% used; 114237011 free inodes.

server3 `/home`: 293463740416 available bytes; 83.62% used; 114237011 free inodes.

server3 `/data`: 52325191680 available bytes; 99.28% used; 225849785 free inodes.

server3 `/tmp`: 293463740416 available bytes; 83.62% used; 114237011 free inodes.

server3 `/var/tmp`: 293463740416 available bytes; 83.62% used; 114237011 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106499440640 available bytes; 94.06% used; 114356062 free inodes.

server4 `/home`: 106499440640 available bytes; 94.06% used; 114356062 free inodes.

server4 `/data`: 300564348928 available bytes; 95.85% used; 225456809 free inodes.

server4 `/tmp`: 106499440640 available bytes; 94.06% used; 114356062 free inodes.

server4 `/var/tmp`: 106499440640 available bytes; 94.06% used; 114356062 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
