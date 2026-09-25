# V2R cluster inventory

2026-09-25T22:09:41.046002+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318693638144 available bytes; 82.22% used; 112476301 free inodes.

server1 `/home`: 318693638144 available bytes; 82.22% used; 112476301 free inodes.

server1 `/tmp`: 318693638144 available bytes; 82.22% used; 112476301 free inodes.

server1 `/var/tmp`: 318693638144 available bytes; 82.22% used; 112476301 free inodes.

server1 `/mnt/raid5`: 360288129024 available bytes; 98.35% used; 337539040 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22949224448 available bytes; 98.72% used; 110406246 free inodes.

server2 `/home`: 22949224448 available bytes; 98.72% used; 110406246 free inodes.

server2 `/tmp`: 22949224448 available bytes; 98.72% used; 110406246 free inodes.

server2 `/var/tmp`: 22949224448 available bytes; 98.72% used; 110406246 free inodes.

server2 `/mnt/raid5`: 299915292672 available bytes; 97.93% used; 445053808 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84359028736 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84359028736 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 125874364416 available bytes; 98.26% used; 225806324 free inodes.

server3 `/tmp`: 84359028736 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84359028736 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105312260096 available bytes; 94.12% used; 114347146 free inodes.

server4 `/home`: 105312260096 available bytes; 94.12% used; 114347146 free inodes.

server4 `/data`: 208744976384 available bytes; 97.12% used; 224919046 free inodes.

server4 `/tmp`: 105312260096 available bytes; 94.12% used; 114347146 free inodes.

server4 `/var/tmp`: 105312260096 available bytes; 94.12% used; 114347146 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
