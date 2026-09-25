# V2R cluster inventory

2026-09-25T14:40:03.095968+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319160139776 available bytes; 82.20% used; 112476982 free inodes.

server1 `/home`: 319160139776 available bytes; 82.20% used; 112476982 free inodes.

server1 `/tmp`: 319160139776 available bytes; 82.20% used; 112476982 free inodes.

server1 `/var/tmp`: 319160139776 available bytes; 82.20% used; 112476982 free inodes.

server1 `/mnt/raid5`: 364586987520 available bytes; 98.33% used; 337546807 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 12798849024 available bytes; 99.29% used; 110407867 free inodes.

server2 `/home`: 12798849024 available bytes; 99.29% used; 110407867 free inodes.

server2 `/tmp`: 12798849024 available bytes; 99.29% used; 110407867 free inodes.

server2 `/var/tmp`: 12798849024 available bytes; 99.29% used; 110407867 free inodes.

server2 `/mnt/raid5`: 321225289728 available bytes; 97.78% used; 445075179 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84263395328 available bytes; 95.30% used; 114154472 free inodes.

server3 `/home`: 84263395328 available bytes; 95.30% used; 114154472 free inodes.

server3 `/data`: 142206963712 available bytes; 98.03% used; 225808529 free inodes.

server3 `/tmp`: 84263395328 available bytes; 95.30% used; 114154472 free inodes.

server3 `/var/tmp`: 84263395328 available bytes; 95.30% used; 114154472 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654079488 available bytes; 94.10% used; 114349709 free inodes.

server4 `/home`: 105654079488 available bytes; 94.10% used; 114349709 free inodes.

server4 `/data`: 231429615616 available bytes; 96.80% used; 224945960 free inodes.

server4 `/tmp`: 105654079488 available bytes; 94.10% used; 114349709 free inodes.

server4 `/var/tmp`: 105654079488 available bytes; 94.10% used; 114349709 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
