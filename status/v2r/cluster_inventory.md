# V2R cluster inventory

2026-09-26T01:29:50.705609+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318649384960 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318649384960 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318649384960 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318649384960 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 345502162944 available bytes; 98.42% used; 337546557 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22929756160 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22929756160 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22929756160 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22929756160 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 290737655808 available bytes; 97.99% used; 445055984 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84336156672 available bytes; 95.29% used; 114152426 free inodes.

server3 `/home`: 84336156672 available bytes; 95.29% used; 114152426 free inodes.

server3 `/data`: 124870664192 available bytes; 98.27% used; 225818035 free inodes.

server3 `/tmp`: 84336156672 available bytes; 95.29% used; 114152426 free inodes.

server3 `/var/tmp`: 84336156672 available bytes; 95.29% used; 114152426 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105264136192 available bytes; 94.13% used; 114347079 free inodes.

server4 `/home`: 105264136192 available bytes; 94.13% used; 114347079 free inodes.

server4 `/data`: 139229753344 available bytes; 98.08% used; 224917293 free inodes.

server4 `/tmp`: 105264136192 available bytes; 94.13% used; 114347079 free inodes.

server4 `/var/tmp`: 105264136192 available bytes; 94.13% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
