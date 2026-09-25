# V2R cluster inventory

2026-09-25T22:37:11.082544+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318692376576 available bytes; 82.22% used; 112476305 free inodes.

server1 `/home`: 318692376576 available bytes; 82.22% used; 112476305 free inodes.

server1 `/tmp`: 318692376576 available bytes; 82.22% used; 112476305 free inodes.

server1 `/var/tmp`: 318692376576 available bytes; 82.22% used; 112476305 free inodes.

server1 `/mnt/raid5`: 360229269504 available bytes; 98.35% used; 337538905 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22952185856 available bytes; 98.72% used; 110406230 free inodes.

server2 `/home`: 22952185856 available bytes; 98.72% used; 110406230 free inodes.

server2 `/tmp`: 22952185856 available bytes; 98.72% used; 110406230 free inodes.

server2 `/var/tmp`: 22952185856 available bytes; 98.72% used; 110406230 free inodes.

server2 `/mnt/raid5`: 298773622784 available bytes; 97.94% used; 445052973 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351569920 available bytes; 95.29% used; 114152426 free inodes.

server3 `/home`: 84351569920 available bytes; 95.29% used; 114152426 free inodes.

server3 `/data`: 124824956928 available bytes; 98.27% used; 225805823 free inodes.

server3 `/tmp`: 84351569920 available bytes; 95.29% used; 114152426 free inodes.

server3 `/var/tmp`: 84351569920 available bytes; 95.29% used; 114152426 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105235849216 available bytes; 94.13% used; 114346965 free inodes.

server4 `/home`: 105235849216 available bytes; 94.13% used; 114346965 free inodes.

server4 `/data`: 192241401856 available bytes; 97.34% used; 224917699 free inodes.

server4 `/tmp`: 105235849216 available bytes; 94.13% used; 114346965 free inodes.

server4 `/var/tmp`: 105235849216 available bytes; 94.13% used; 114346965 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
