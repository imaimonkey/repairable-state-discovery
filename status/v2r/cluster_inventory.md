# V2R cluster inventory

2026-09-25T22:41:46.017544+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318693068800 available bytes; 82.22% used; 112476293 free inodes.

server1 `/home`: 318693068800 available bytes; 82.22% used; 112476293 free inodes.

server1 `/tmp`: 318693068800 available bytes; 82.22% used; 112476293 free inodes.

server1 `/var/tmp`: 318693068800 available bytes; 82.22% used; 112476293 free inodes.

server1 `/mnt/raid5`: 360217092096 available bytes; 98.35% used; 337538879 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22952325120 available bytes; 98.72% used; 110406232 free inodes.

server2 `/home`: 22952325120 available bytes; 98.72% used; 110406232 free inodes.

server2 `/tmp`: 22952325120 available bytes; 98.72% used; 110406232 free inodes.

server2 `/var/tmp`: 22952325120 available bytes; 98.72% used; 110406232 free inodes.

server2 `/mnt/raid5`: 298094153728 available bytes; 97.94% used; 445052683 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351647744 available bytes; 95.29% used; 114152434 free inodes.

server3 `/home`: 84351647744 available bytes; 95.29% used; 114152434 free inodes.

server3 `/data`: 124825948160 available bytes; 98.27% used; 225805752 free inodes.

server3 `/tmp`: 84351647744 available bytes; 95.29% used; 114152434 free inodes.

server3 `/var/tmp`: 84351647744 available bytes; 95.29% used; 114152434 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105235689472 available bytes; 94.13% used; 114346964 free inodes.

server4 `/home`: 105235689472 available bytes; 94.13% used; 114346964 free inodes.

server4 `/data`: 192231780352 available bytes; 97.34% used; 224917688 free inodes.

server4 `/tmp`: 105235689472 available bytes; 94.13% used; 114346964 free inodes.

server4 `/var/tmp`: 105235689472 available bytes; 94.13% used; 114346964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
