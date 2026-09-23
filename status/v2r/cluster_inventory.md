# V2R cluster inventory

2026-09-23T21:42:49.669536+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325712449536 available bytes; 81.83% used; 112501339 free inodes.

server1 `/home`: 325712449536 available bytes; 81.83% used; 112501339 free inodes.

server1 `/tmp`: 325712449536 available bytes; 81.83% used; 112501339 free inodes.

server1 `/var/tmp`: 325712449536 available bytes; 81.83% used; 112501339 free inodes.

server1 `/mnt/raid5`: 1388127346688 available bytes; 93.63% used; 337739923 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41115566080 available bytes; 97.71% used; 110432665 free inodes.

server2 `/home`: 41115566080 available bytes; 97.71% used; 110432665 free inodes.

server2 `/tmp`: 41115566080 available bytes; 97.71% used; 110432665 free inodes.

server2 `/var/tmp`: 41115566080 available bytes; 97.71% used; 110432665 free inodes.

server2 `/mnt/raid5`: 538130640896 available bytes; 96.28% used; 445208345 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292631916544 available bytes; 83.67% used; 114187274 free inodes.

server3 `/home`: 292631916544 available bytes; 83.67% used; 114187274 free inodes.

server3 `/data`: 82485444608 available bytes; 98.86% used; 225848531 free inodes.

server3 `/tmp`: 292631916544 available bytes; 83.67% used; 114187274 free inodes.

server3 `/var/tmp`: 292631916544 available bytes; 83.67% used; 114187274 free inodes.
| server4 | True | ['0', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106473123840 available bytes; 94.06% used; 114355972 free inodes.

server4 `/home`: 106473123840 available bytes; 94.06% used; 114355972 free inodes.

server4 `/data`: 300252463104 available bytes; 95.85% used; 225448387 free inodes.

server4 `/tmp`: 106473123840 available bytes; 94.06% used; 114355972 free inodes.

server4 `/var/tmp`: 106473123840 available bytes; 94.06% used; 114355972 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
