# V2R cluster inventory

2026-09-25T06:30:40.545645+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318879739904 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318879739904 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318879739904 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318879739904 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 399811293184 available bytes; 98.17% used; 337561443 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22890635264 available bytes; 98.72% used; 110410534 free inodes.

server2 `/home`: 22890635264 available bytes; 98.72% used; 110410534 free inodes.

server2 `/tmp`: 22890635264 available bytes; 98.72% used; 110410534 free inodes.

server2 `/var/tmp`: 22890635264 available bytes; 98.72% used; 110410534 free inodes.

server2 `/mnt/raid5`: 370522914816 available bytes; 97.44% used; 445099507 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84448518144 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84448518144 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142534144000 available bytes; 98.03% used; 225813770 free inodes.

server3 `/tmp`: 84448518144 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84448518144 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648193536 available bytes; 94.10% used; 114350390 free inodes.

server4 `/home`: 105648193536 available bytes; 94.10% used; 114350390 free inodes.

server4 `/data`: 253483364352 available bytes; 96.50% used; 225020632 free inodes.

server4 `/tmp`: 105648193536 available bytes; 94.10% used; 114350390 free inodes.

server4 `/var/tmp`: 105648193536 available bytes; 94.10% used; 114350390 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
