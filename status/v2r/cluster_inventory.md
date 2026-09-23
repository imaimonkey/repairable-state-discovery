# V2R cluster inventory

2026-09-23T20:18:29.136853+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325741170688 available bytes; 81.83% used; 112501843 free inodes.

server1 `/home`: 325741170688 available bytes; 81.83% used; 112501843 free inodes.

server1 `/tmp`: 325741170688 available bytes; 81.83% used; 112501843 free inodes.

server1 `/var/tmp`: 325741170688 available bytes; 81.83% used; 112501843 free inodes.

server1 `/mnt/raid5`: 1388299243520 available bytes; 93.63% used; 337741069 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 41270018048 available bytes; 97.70% used; 110434868 free inodes.

server2 `/home`: 41270018048 available bytes; 97.70% used; 110434868 free inodes.

server2 `/tmp`: 41270018048 available bytes; 97.70% used; 110434868 free inodes.

server2 `/var/tmp`: 41270018048 available bytes; 97.70% used; 110434868 free inodes.

server2 `/mnt/raid5`: 541280542720 available bytes; 96.26% used; 445211007 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293458333696 available bytes; 83.62% used; 114234793 free inodes.

server3 `/home`: 293458333696 available bytes; 83.62% used; 114234793 free inodes.

server3 `/data`: 52608233472 available bytes; 99.27% used; 225843922 free inodes.

server3 `/tmp`: 293458333696 available bytes; 83.62% used; 114234793 free inodes.

server3 `/var/tmp`: 293458333696 available bytes; 83.62% used; 114234793 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106528092160 available bytes; 94.06% used; 114356223 free inodes.

server4 `/home`: 106528092160 available bytes; 94.06% used; 114356223 free inodes.

server4 `/data`: 1126400 available bytes; 100.00% used; 225457636 free inodes.

server4 `/tmp`: 106528092160 available bytes; 94.06% used; 114356223 free inodes.

server4 `/var/tmp`: 106528092160 available bytes; 94.06% used; 114356223 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
