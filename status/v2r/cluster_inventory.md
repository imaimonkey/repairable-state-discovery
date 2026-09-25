# V2R cluster inventory

2026-09-25T21:16:12.073033+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318704230400 available bytes; 82.22% used; 112476315 free inodes.

server1 `/home`: 318704230400 available bytes; 82.22% used; 112476315 free inodes.

server1 `/tmp`: 318704230400 available bytes; 82.22% used; 112476315 free inodes.

server1 `/var/tmp`: 318704230400 available bytes; 82.22% used; 112476315 free inodes.

server1 `/mnt/raid5`: 368330797056 available bytes; 98.31% used; 337539403 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22888714240 available bytes; 98.72% used; 110405686 free inodes.

server2 `/home`: 22888714240 available bytes; 98.72% used; 110405686 free inodes.

server2 `/tmp`: 22888714240 available bytes; 98.72% used; 110405686 free inodes.

server2 `/var/tmp`: 22888714240 available bytes; 98.72% used; 110405686 free inodes.

server2 `/mnt/raid5`: 301942427648 available bytes; 97.91% used; 445055372 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84367949824 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84367949824 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 125902798848 available bytes; 98.26% used; 225807215 free inodes.

server3 `/tmp`: 84367949824 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84367949824 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105389449216 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105389449216 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 217865388032 available bytes; 96.99% used; 224920435 free inodes.

server4 `/tmp`: 105389449216 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105389449216 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
