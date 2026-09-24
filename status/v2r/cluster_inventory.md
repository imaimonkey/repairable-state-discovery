# V2R cluster inventory

2026-09-24T16:06:48.008915+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324027650048 available bytes; 81.92% used; 112481452 free inodes.

server1 `/home`: 324027650048 available bytes; 81.92% used; 112481452 free inodes.

server1 `/tmp`: 324027650048 available bytes; 81.92% used; 112481452 free inodes.

server1 `/var/tmp`: 324027650048 available bytes; 81.92% used; 112481452 free inodes.

server1 `/mnt/raid5`: 416629919744 available bytes; 98.09% used; 337656091 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57351122944 available bytes; 96.80% used; 110427135 free inodes.

server2 `/home`: 57351122944 available bytes; 96.80% used; 110427135 free inodes.

server2 `/tmp`: 57351122944 available bytes; 96.80% used; 110427135 free inodes.

server2 `/var/tmp`: 57351122944 available bytes; 96.80% used; 110427135 free inodes.

server2 `/mnt/raid5`: 501654601728 available bytes; 96.53% used; 445164762 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84551024640 available bytes; 95.28% used; 114174288 free inodes.

server3 `/home`: 84551024640 available bytes; 95.28% used; 114174288 free inodes.

server3 `/data`: 160038334464 available bytes; 97.79% used; 225805743 free inodes.

server3 `/tmp`: 84551024640 available bytes; 95.28% used; 114174288 free inodes.

server3 `/var/tmp`: 84551024640 available bytes; 95.28% used; 114174288 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105698033664 available bytes; 94.10% used; 114348610 free inodes.

server4 `/home`: 105698033664 available bytes; 94.10% used; 114348610 free inodes.

server4 `/data`: 89329328128 available bytes; 98.77% used; 225256179 free inodes.

server4 `/tmp`: 105698033664 available bytes; 94.10% used; 114348610 free inodes.

server4 `/var/tmp`: 105698033664 available bytes; 94.10% used; 114348610 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
