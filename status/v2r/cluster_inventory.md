# V2R cluster inventory

2026-09-23T20:20:00.813767+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325740560384 available bytes; 81.83% used; 112501846 free inodes.

server1 `/home`: 325740560384 available bytes; 81.83% used; 112501846 free inodes.

server1 `/tmp`: 325740560384 available bytes; 81.83% used; 112501846 free inodes.

server1 `/var/tmp`: 325740560384 available bytes; 81.83% used; 112501846 free inodes.

server1 `/mnt/raid5`: 1388298477568 available bytes; 93.63% used; 337741054 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41269272576 available bytes; 97.70% used; 110434862 free inodes.

server2 `/home`: 41269272576 available bytes; 97.70% used; 110434862 free inodes.

server2 `/tmp`: 41269272576 available bytes; 97.70% used; 110434862 free inodes.

server2 `/var/tmp`: 41269272576 available bytes; 97.70% used; 110434862 free inodes.

server2 `/mnt/raid5`: 541241847808 available bytes; 96.26% used; 445210952 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293454270464 available bytes; 83.62% used; 114234944 free inodes.

server3 `/home`: 293454270464 available bytes; 83.62% used; 114234944 free inodes.

server3 `/data`: 52606349312 available bytes; 99.27% used; 225843883 free inodes.

server3 `/tmp`: 293454270464 available bytes; 83.62% used; 114234944 free inodes.

server3 `/var/tmp`: 293454270464 available bytes; 83.62% used; 114234944 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106528030720 available bytes; 94.06% used; 114356224 free inodes.

server4 `/home`: 106528030720 available bytes; 94.06% used; 114356224 free inodes.

server4 `/data`: 7315456 available bytes; 100.00% used; 225457631 free inodes.

server4 `/tmp`: 106528030720 available bytes; 94.06% used; 114356224 free inodes.

server4 `/var/tmp`: 106528030720 available bytes; 94.06% used; 114356224 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
