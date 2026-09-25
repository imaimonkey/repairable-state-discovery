# V2R cluster inventory

2026-09-25T21:26:54.033844+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318702202880 available bytes; 82.22% used; 112476325 free inodes.

server1 `/home`: 318702202880 available bytes; 82.22% used; 112476325 free inodes.

server1 `/tmp`: 318702202880 available bytes; 82.22% used; 112476325 free inodes.

server1 `/var/tmp`: 318702202880 available bytes; 82.22% used; 112476325 free inodes.

server1 `/mnt/raid5`: 347218984960 available bytes; 98.41% used; 337539334 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22905880576 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22905880576 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22905880576 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22905880576 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 301367926784 available bytes; 97.92% used; 445055128 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84363841536 available bytes; 95.29% used; 114152618 free inodes.

server3 `/home`: 84363841536 available bytes; 95.29% used; 114152618 free inodes.

server3 `/data`: 125899919360 available bytes; 98.26% used; 225807044 free inodes.

server3 `/tmp`: 84363841536 available bytes; 95.29% used; 114152618 free inodes.

server3 `/var/tmp`: 84363841536 available bytes; 95.29% used; 114152618 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105389117440 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105389117440 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 217454895104 available bytes; 96.99% used; 224920126 free inodes.

server4 `/tmp`: 105389117440 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105389117440 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
