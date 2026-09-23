# V2R cluster inventory

2026-09-23T21:21:14.554516+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325720289280 available bytes; 81.83% used; 112501430 free inodes.

server1 `/home`: 325720289280 available bytes; 81.83% used; 112501430 free inodes.

server1 `/tmp`: 325720289280 available bytes; 81.83% used; 112501430 free inodes.

server1 `/var/tmp`: 325720289280 available bytes; 81.83% used; 112501430 free inodes.

server1 `/mnt/raid5`: 1367487111168 available bytes; 93.73% used; 337739962 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41111519232 available bytes; 97.71% used; 110432689 free inodes.

server2 `/home`: 41111519232 available bytes; 97.71% used; 110432689 free inodes.

server2 `/tmp`: 41111519232 available bytes; 97.71% used; 110432689 free inodes.

server2 `/var/tmp`: 41111519232 available bytes; 97.71% used; 110432689 free inodes.

server2 `/mnt/raid5`: 538802814976 available bytes; 96.28% used; 445209115 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292953673728 available bytes; 83.65% used; 114208566 free inodes.

server3 `/home`: 292953673728 available bytes; 83.65% used; 114208566 free inodes.

server3 `/data`: 52295254016 available bytes; 99.28% used; 225848974 free inodes.

server3 `/tmp`: 292953673728 available bytes; 83.65% used; 114208566 free inodes.

server3 `/var/tmp`: 292953673728 available bytes; 83.65% used; 114208566 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106487095296 available bytes; 94.06% used; 114356022 free inodes.

server4 `/home`: 106487095296 available bytes; 94.06% used; 114356022 free inodes.

server4 `/data`: 300396765184 available bytes; 95.85% used; 225452709 free inodes.

server4 `/tmp`: 106487095296 available bytes; 94.06% used; 114356022 free inodes.

server4 `/var/tmp`: 106487095296 available bytes; 94.06% used; 114356022 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
