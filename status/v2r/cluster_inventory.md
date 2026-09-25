# V2R cluster inventory

2026-09-25T16:10:20.382287+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318673039360 available bytes; 82.22% used; 112476332 free inodes.

server1 `/home`: 318673039360 available bytes; 82.22% used; 112476332 free inodes.

server1 `/tmp`: 318673039360 available bytes; 82.22% used; 112476332 free inodes.

server1 `/var/tmp`: 318673039360 available bytes; 82.22% used; 112476332 free inodes.

server1 `/mnt/raid5`: 363910098944 available bytes; 98.33% used; 337545098 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23115481088 available bytes; 98.71% used; 110407944 free inodes.

server2 `/home`: 23115481088 available bytes; 98.71% used; 110407944 free inodes.

server2 `/tmp`: 23115481088 available bytes; 98.71% used; 110407944 free inodes.

server2 `/var/tmp`: 23115481088 available bytes; 98.71% used; 110407944 free inodes.

server2 `/mnt/raid5`: 318921764864 available bytes; 97.80% used; 445070987 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84401872896 available bytes; 95.29% used; 114152674 free inodes.

server3 `/home`: 84401872896 available bytes; 95.29% used; 114152674 free inodes.

server3 `/data`: 134936526848 available bytes; 98.14% used; 225806291 free inodes.

server3 `/tmp`: 84401872896 available bytes; 95.29% used; 114152674 free inodes.

server3 `/var/tmp`: 84401872896 available bytes; 95.29% used; 114152674 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636683776 available bytes; 94.11% used; 114349648 free inodes.

server4 `/home`: 105636683776 available bytes; 94.11% used; 114349648 free inodes.

server4 `/data`: 230248271872 available bytes; 96.82% used; 224934650 free inodes.

server4 `/tmp`: 105636683776 available bytes; 94.11% used; 114349648 free inodes.

server4 `/var/tmp`: 105636683776 available bytes; 94.11% used; 114349648 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
