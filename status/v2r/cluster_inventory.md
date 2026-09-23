# V2R cluster inventory

2026-09-23T20:35:16.849706+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325733912576 available bytes; 81.83% used; 112501763 free inodes.

server1 `/home`: 325733912576 available bytes; 81.83% used; 112501763 free inodes.

server1 `/tmp`: 325733912576 available bytes; 81.83% used; 112501763 free inodes.

server1 `/var/tmp`: 325733912576 available bytes; 81.83% used; 112501763 free inodes.

server1 `/mnt/raid5`: 1388262219776 available bytes; 93.63% used; 337740921 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 41139470336 available bytes; 97.70% used; 110432796 free inodes.

server2 `/home`: 41139470336 available bytes; 97.70% used; 110432796 free inodes.

server2 `/tmp`: 41139470336 available bytes; 97.70% used; 110432796 free inodes.

server2 `/var/tmp`: 41139470336 available bytes; 97.70% used; 110432796 free inodes.

server2 `/mnt/raid5`: 540203798528 available bytes; 96.27% used; 445210401 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292915417088 available bytes; 83.65% used; 114207425 free inodes.

server3 `/home`: 292915417088 available bytes; 83.65% used; 114207425 free inodes.

server3 `/data`: 52586774528 available bytes; 99.27% used; 225843258 free inodes.

server3 `/tmp`: 292915417088 available bytes; 83.65% used; 114207425 free inodes.

server3 `/var/tmp`: 292915417088 available bytes; 83.65% used; 114207425 free inodes.
| server4 | True | ['1', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106524876800 available bytes; 94.06% used; 114356146 free inodes.

server4 `/home`: 106524876800 available bytes; 94.06% used; 114356146 free inodes.

server4 `/data`: 300726591488 available bytes; 95.84% used; 225461446 free inodes.

server4 `/tmp`: 106524876800 available bytes; 94.06% used; 114356146 free inodes.

server4 `/var/tmp`: 106524876800 available bytes; 94.06% used; 114356146 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
