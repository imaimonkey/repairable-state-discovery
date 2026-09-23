# V2R cluster inventory

2026-09-23T20:45:58.371092+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325735886848 available bytes; 81.83% used; 112501746 free inodes.

server1 `/home`: 325735886848 available bytes; 81.83% used; 112501746 free inodes.

server1 `/tmp`: 325735886848 available bytes; 81.83% used; 112501746 free inodes.

server1 `/var/tmp`: 325735886848 available bytes; 81.83% used; 112501746 free inodes.

server1 `/mnt/raid5`: 1388192182272 available bytes; 93.63% used; 337740058 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 41132048384 available bytes; 97.71% used; 110432769 free inodes.

server2 `/home`: 41132048384 available bytes; 97.71% used; 110432769 free inodes.

server2 `/tmp`: 41132048384 available bytes; 97.71% used; 110432769 free inodes.

server2 `/var/tmp`: 41132048384 available bytes; 97.71% used; 110432769 free inodes.

server2 `/mnt/raid5`: 539884687360 available bytes; 96.27% used; 445210196 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293471870976 available bytes; 83.62% used; 114238478 free inodes.

server3 `/home`: 293471870976 available bytes; 83.62% used; 114238478 free inodes.

server3 `/data`: 52573257728 available bytes; 99.27% used; 225843061 free inodes.

server3 `/tmp`: 293471870976 available bytes; 83.62% used; 114238478 free inodes.

server3 `/var/tmp`: 293471870976 available bytes; 83.62% used; 114238478 free inodes.
| server4 | True | ['1', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106514362368 available bytes; 94.06% used; 114356125 free inodes.

server4 `/home`: 106514362368 available bytes; 94.06% used; 114356125 free inodes.

server4 `/data`: 300643934208 available bytes; 95.84% used; 225459771 free inodes.

server4 `/tmp`: 106514362368 available bytes; 94.06% used; 114356125 free inodes.

server4 `/var/tmp`: 106514362368 available bytes; 94.06% used; 114356125 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
