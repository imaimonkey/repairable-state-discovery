# V2R cluster inventory

2026-09-25T03:38:08.130091+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318939926528 available bytes; 82.21% used; 112480351 free inodes.

server1 `/home`: 318939926528 available bytes; 82.21% used; 112480351 free inodes.

server1 `/tmp`: 318939926528 available bytes; 82.21% used; 112480351 free inodes.

server1 `/var/tmp`: 318939926528 available bytes; 82.21% used; 112480351 free inodes.

server1 `/mnt/raid5`: 416066080768 available bytes; 98.09% used; 337597973 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22982840320 available bytes; 98.72% used; 110410448 free inodes.

server2 `/home`: 22982840320 available bytes; 98.72% used; 110410448 free inodes.

server2 `/tmp`: 22982840320 available bytes; 98.72% used; 110410448 free inodes.

server2 `/var/tmp`: 22982840320 available bytes; 98.72% used; 110410448 free inodes.

server2 `/mnt/raid5`: 464113070080 available bytes; 96.79% used; 445111524 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341403648 available bytes; 95.29% used; 114156067 free inodes.

server3 `/home`: 84341403648 available bytes; 95.29% used; 114156067 free inodes.

server3 `/data`: 144462544896 available bytes; 98.00% used; 225817383 free inodes.

server3 `/tmp`: 84341403648 available bytes; 95.29% used; 114156067 free inodes.

server3 `/var/tmp`: 84341403648 available bytes; 95.29% used; 114156067 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105683628032 available bytes; 94.10% used; 114350896 free inodes.

server4 `/home`: 105683628032 available bytes; 94.10% used; 114350896 free inodes.

server4 `/data`: 39765954560 available bytes; 99.45% used; 224965845 free inodes.

server4 `/tmp`: 105683628032 available bytes; 94.10% used; 114350896 free inodes.

server4 `/var/tmp`: 105683628032 available bytes; 94.10% used; 114350896 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
