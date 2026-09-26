# V2R cluster inventory

2026-09-26T05:46:38.526191+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318781165568 available bytes; 82.22% used; 112476275 free inodes.

server1 `/home`: 318781165568 available bytes; 82.22% used; 112476275 free inodes.

server1 `/tmp`: 318781165568 available bytes; 82.22% used; 112476275 free inodes.

server1 `/var/tmp`: 318781165568 available bytes; 82.22% used; 112476275 free inodes.

server1 `/mnt/raid5`: 239031754752 available bytes; 98.90% used; 337540064 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22744276992 available bytes; 98.73% used; 110405661 free inodes.

server2 `/home`: 22744276992 available bytes; 98.73% used; 110405661 free inodes.

server2 `/tmp`: 22744276992 available bytes; 98.73% used; 110405661 free inodes.

server2 `/var/tmp`: 22744276992 available bytes; 98.73% used; 110405661 free inodes.

server2 `/mnt/raid5`: 275450540032 available bytes; 98.10% used; 445034023 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83203194880 available bytes; 95.36% used; 114148967 free inodes.

server3 `/home`: 83203194880 available bytes; 95.36% used; 114148967 free inodes.

server3 `/data`: 124277129216 available bytes; 98.28% used; 225823972 free inodes.

server3 `/tmp`: 83203194880 available bytes; 95.36% used; 114148967 free inodes.

server3 `/var/tmp`: 83203194880 available bytes; 95.36% used; 114148967 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094473216 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094473216 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106984497152 available bytes; 98.52% used; 224929128 free inodes.

server4 `/tmp`: 106094473216 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094473216 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
