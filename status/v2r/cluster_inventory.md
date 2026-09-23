# V2R cluster inventory

2026-09-23T20:44:26.867029+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325735424000 available bytes; 81.83% used; 112501744 free inodes.

server1 `/home`: 325735424000 available bytes; 81.83% used; 112501744 free inodes.

server1 `/tmp`: 325735424000 available bytes; 81.83% used; 112501744 free inodes.

server1 `/var/tmp`: 325735424000 available bytes; 81.83% used; 112501744 free inodes.

server1 `/mnt/raid5`: 1388249223168 available bytes; 93.63% used; 337740735 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 41132732416 available bytes; 97.71% used; 110432775 free inodes.

server2 `/home`: 41132732416 available bytes; 97.71% used; 110432775 free inodes.

server2 `/tmp`: 41132732416 available bytes; 97.71% used; 110432775 free inodes.

server2 `/var/tmp`: 41132732416 available bytes; 97.71% used; 110432775 free inodes.

server2 `/mnt/raid5`: 539922997248 available bytes; 96.27% used; 445209927 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293129637888 available bytes; 83.64% used; 114216730 free inodes.

server3 `/home`: 293129637888 available bytes; 83.64% used; 114216730 free inodes.

server3 `/data`: 52574834688 available bytes; 99.27% used; 225843084 free inodes.

server3 `/tmp`: 293129637888 available bytes; 83.64% used; 114216730 free inodes.

server3 `/var/tmp`: 293129637888 available bytes; 83.64% used; 114216730 free inodes.
| server4 | True | ['1', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106514694144 available bytes; 94.06% used; 114356126 free inodes.

server4 `/home`: 106514694144 available bytes; 94.06% used; 114356126 free inodes.

server4 `/data`: 300658368512 available bytes; 95.84% used; 225460103 free inodes.

server4 `/tmp`: 106514694144 available bytes; 94.06% used; 114356126 free inodes.

server4 `/var/tmp`: 106514694144 available bytes; 94.06% used; 114356126 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
