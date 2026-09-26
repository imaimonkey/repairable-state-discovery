# V2R cluster inventory

2026-09-26T05:55:50.517897+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318781562880 available bytes; 82.22% used; 112476288 free inodes.

server1 `/home`: 318781562880 available bytes; 82.22% used; 112476288 free inodes.

server1 `/tmp`: 318781562880 available bytes; 82.22% used; 112476288 free inodes.

server1 `/var/tmp`: 318781562880 available bytes; 82.22% used; 112476288 free inodes.

server1 `/mnt/raid5`: 232756015104 available bytes; 98.93% used; 337539982 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22738440192 available bytes; 98.73% used; 110405659 free inodes.

server2 `/home`: 22738440192 available bytes; 98.73% used; 110405659 free inodes.

server2 `/tmp`: 22738440192 available bytes; 98.73% used; 110405659 free inodes.

server2 `/var/tmp`: 22738440192 available bytes; 98.73% used; 110405659 free inodes.

server2 `/mnt/raid5`: 274176745472 available bytes; 98.11% used; 445033700 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82889932800 available bytes; 95.37% used; 114140591 free inodes.

server3 `/home`: 82889932800 available bytes; 95.37% used; 114140591 free inodes.

server3 `/data`: 124003061760 available bytes; 98.29% used; 225822868 free inodes.

server3 `/tmp`: 82889932800 available bytes; 95.37% used; 114140591 free inodes.

server3 `/var/tmp`: 82889932800 available bytes; 95.37% used; 114140591 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094215168 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094215168 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106987757568 available bytes; 98.52% used; 224929124 free inodes.

server4 `/tmp`: 106094215168 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094215168 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
