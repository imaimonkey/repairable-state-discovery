# V2R cluster inventory

2026-09-24T03:36:46.922147+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324743614464 available bytes; 81.88% used; 112493813 free inodes.

server1 `/home`: 324743614464 available bytes; 81.88% used; 112493813 free inodes.

server1 `/tmp`: 324743614464 available bytes; 81.88% used; 112493813 free inodes.

server1 `/var/tmp`: 324743614464 available bytes; 81.88% used; 112493813 free inodes.

server1 `/mnt/raid5`: 397434703872 available bytes; 98.18% used; 337733976 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40830242816 available bytes; 97.72% used; 110431054 free inodes.

server2 `/home`: 40830242816 available bytes; 97.72% used; 110431054 free inodes.

server2 `/tmp`: 40830242816 available bytes; 97.72% used; 110431054 free inodes.

server2 `/var/tmp`: 40830242816 available bytes; 97.72% used; 110431054 free inodes.

server2 `/mnt/raid5`: 527012122624 available bytes; 96.36% used; 445197629 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292018982912 available bytes; 83.70% used; 114184047 free inodes.

server3 `/home`: 292018982912 available bytes; 83.70% used; 114184047 free inodes.

server3 `/data`: 36006395904 available bytes; 99.50% used; 225842891 free inodes.

server3 `/tmp`: 292018982912 available bytes; 83.70% used; 114184047 free inodes.

server3 `/var/tmp`: 292018982912 available bytes; 83.70% used; 114184047 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105986584576 available bytes; 94.09% used; 114349586 free inodes.

server4 `/home`: 105986584576 available bytes; 94.09% used; 114349586 free inodes.

server4 `/data`: 280447299584 available bytes; 96.12% used; 225385359 free inodes.

server4 `/tmp`: 105986584576 available bytes; 94.09% used; 114349586 free inodes.

server4 `/var/tmp`: 105986584576 available bytes; 94.09% used; 114349586 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
