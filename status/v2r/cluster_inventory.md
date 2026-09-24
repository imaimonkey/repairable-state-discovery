# V2R cluster inventory

2026-09-24T05:22:45.808861+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324560445440 available bytes; 81.89% used; 112492454 free inodes.

server1 `/home`: 324560445440 available bytes; 81.89% used; 112492454 free inodes.

server1 `/tmp`: 324560445440 available bytes; 81.89% used; 112492454 free inodes.

server1 `/var/tmp`: 324560445440 available bytes; 81.89% used; 112492454 free inodes.

server1 `/mnt/raid5`: 509532831744 available bytes; 97.66% used; 337724504 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40738861056 available bytes; 97.73% used; 110430322 free inodes.

server2 `/home`: 40738861056 available bytes; 97.73% used; 110430322 free inodes.

server2 `/tmp`: 40738861056 available bytes; 97.73% used; 110430322 free inodes.

server2 `/var/tmp`: 40738861056 available bytes; 97.73% used; 110430322 free inodes.

server2 `/mnt/raid5`: 522609631232 available bytes; 96.39% used; 445194015 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 291991965696 available bytes; 83.71% used; 114175930 free inodes.

server3 `/home`: 291991965696 available bytes; 83.71% used; 114175930 free inodes.

server3 `/data`: 21147332608 available bytes; 99.71% used; 225839792 free inodes.

server3 `/tmp`: 291991965696 available bytes; 83.71% used; 114175930 free inodes.

server3 `/var/tmp`: 291991965696 available bytes; 83.71% used; 114175930 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105817395200 available bytes; 94.10% used; 114349367 free inodes.

server4 `/home`: 105817395200 available bytes; 94.10% used; 114349367 free inodes.

server4 `/data`: 252561940480 available bytes; 96.51% used; 225366568 free inodes.

server4 `/tmp`: 105817395200 available bytes; 94.10% used; 114349367 free inodes.

server4 `/var/tmp`: 105817395200 available bytes; 94.10% used; 114349367 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
