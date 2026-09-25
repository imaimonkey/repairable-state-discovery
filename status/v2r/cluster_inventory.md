# V2R cluster inventory

2026-09-25T15:59:36.967366+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318677794816 available bytes; 82.22% used; 112476506 free inodes.

server1 `/home`: 318677794816 available bytes; 82.22% used; 112476506 free inodes.

server1 `/tmp`: 318677794816 available bytes; 82.22% used; 112476506 free inodes.

server1 `/var/tmp`: 318677794816 available bytes; 82.22% used; 112476506 free inodes.

server1 `/mnt/raid5`: 365287415808 available bytes; 98.32% used; 337545301 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23117815808 available bytes; 98.71% used; 110407948 free inodes.

server2 `/home`: 23117815808 available bytes; 98.71% used; 110407948 free inodes.

server2 `/tmp`: 23117815808 available bytes; 98.71% used; 110407948 free inodes.

server2 `/var/tmp`: 23117815808 available bytes; 98.71% used; 110407948 free inodes.

server2 `/mnt/raid5`: 319269945344 available bytes; 97.79% used; 445071608 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84406378496 available bytes; 95.29% used; 114152682 free inodes.

server3 `/home`: 84406378496 available bytes; 95.29% used; 114152682 free inodes.

server3 `/data`: 140110336000 available bytes; 98.06% used; 225806569 free inodes.

server3 `/tmp`: 84406378496 available bytes; 95.29% used; 114152682 free inodes.

server3 `/var/tmp`: 84406378496 available bytes; 95.29% used; 114152682 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637056512 available bytes; 94.11% used; 114349664 free inodes.

server4 `/home`: 105637056512 available bytes; 94.11% used; 114349664 free inodes.

server4 `/data`: 231291305984 available bytes; 96.80% used; 224943337 free inodes.

server4 `/tmp`: 105637056512 available bytes; 94.11% used; 114349664 free inodes.

server4 `/var/tmp`: 105637056512 available bytes; 94.11% used; 114349664 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
