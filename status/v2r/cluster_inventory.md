# V2R cluster inventory

2026-09-25T22:40:14.354468+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318693429248 available bytes; 82.22% used; 112476307 free inodes.

server1 `/home`: 318693429248 available bytes; 82.22% used; 112476307 free inodes.

server1 `/tmp`: 318693429248 available bytes; 82.22% used; 112476307 free inodes.

server1 `/var/tmp`: 318693429248 available bytes; 82.22% used; 112476307 free inodes.

server1 `/mnt/raid5`: 360225320960 available bytes; 98.35% used; 337538901 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22952501248 available bytes; 98.72% used; 110406232 free inodes.

server2 `/home`: 22952501248 available bytes; 98.72% used; 110406232 free inodes.

server2 `/tmp`: 22952501248 available bytes; 98.72% used; 110406232 free inodes.

server2 `/var/tmp`: 22952501248 available bytes; 98.72% used; 110406232 free inodes.

server2 `/mnt/raid5`: 298675146752 available bytes; 97.94% used; 445052653 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352028672 available bytes; 95.29% used; 114152428 free inodes.

server3 `/home`: 84352028672 available bytes; 95.29% used; 114152428 free inodes.

server3 `/data`: 124827672576 available bytes; 98.27% used; 225805773 free inodes.

server3 `/tmp`: 84352028672 available bytes; 95.29% used; 114152428 free inodes.

server3 `/var/tmp`: 84352028672 available bytes; 95.29% used; 114152428 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105235722240 available bytes; 94.13% used; 114346964 free inodes.

server4 `/home`: 105235722240 available bytes; 94.13% used; 114346964 free inodes.

server4 `/data`: 192232022016 available bytes; 97.34% used; 224917689 free inodes.

server4 `/tmp`: 105235722240 available bytes; 94.13% used; 114346964 free inodes.

server4 `/var/tmp`: 105235722240 available bytes; 94.13% used; 114346964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
