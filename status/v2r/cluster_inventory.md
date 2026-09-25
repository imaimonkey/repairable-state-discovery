# V2R cluster inventory

2026-09-25T19:16:47.045707+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318735847424 available bytes; 82.22% used; 112476343 free inodes.

server1 `/home`: 318735847424 available bytes; 82.22% used; 112476343 free inodes.

server1 `/tmp`: 318735847424 available bytes; 82.22% used; 112476343 free inodes.

server1 `/var/tmp`: 318735847424 available bytes; 82.22% used; 112476343 free inodes.

server1 `/mnt/raid5`: 370883121152 available bytes; 98.30% used; 337540844 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23103152128 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23103152128 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23103152128 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23103152128 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 312448761856 available bytes; 97.84% used; 445064748 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84382736384 available bytes; 95.29% used; 114152623 free inodes.

server3 `/home`: 84382736384 available bytes; 95.29% used; 114152623 free inodes.

server3 `/data`: 129288708096 available bytes; 98.21% used; 225808811 free inodes.

server3 `/tmp`: 84382736384 available bytes; 95.29% used; 114152623 free inodes.

server3 `/var/tmp`: 84382736384 available bytes; 95.29% used; 114152623 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105675362304 available bytes; 94.10% used; 114349590 free inodes.

server4 `/home`: 105675362304 available bytes; 94.10% used; 114349590 free inodes.

server4 `/data`: 229638975488 available bytes; 96.83% used; 224930694 free inodes.

server4 `/tmp`: 105675362304 available bytes; 94.10% used; 114349590 free inodes.

server4 `/var/tmp`: 105675362304 available bytes; 94.10% used; 114349590 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
