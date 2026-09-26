# V2R cluster inventory

2026-09-26T05:15:09.833847+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318398509056 available bytes; 82.24% used; 112476279 free inodes.

server1 `/home`: 318398509056 available bytes; 82.24% used; 112476279 free inodes.

server1 `/tmp`: 318398509056 available bytes; 82.24% used; 112476279 free inodes.

server1 `/var/tmp`: 318398509056 available bytes; 82.24% used; 112476279 free inodes.

server1 `/mnt/raid5`: 309554864128 available bytes; 98.58% used; 337542909 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22927331328 available bytes; 98.72% used; 110406199 free inodes.

server2 `/home`: 22927331328 available bytes; 98.72% used; 110406199 free inodes.

server2 `/tmp`: 22927331328 available bytes; 98.72% used; 110406199 free inodes.

server2 `/var/tmp`: 22927331328 available bytes; 98.72% used; 110406199 free inodes.

server2 `/mnt/raid5`: 263461568512 available bytes; 98.18% used; 445049006 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84084850688 available bytes; 95.31% used; 114166095 free inodes.

server3 `/home`: 84084850688 available bytes; 95.31% used; 114166095 free inodes.

server3 `/data`: 124562022400 available bytes; 98.28% used; 225825161 free inodes.

server3 `/tmp`: 84084850688 available bytes; 95.31% used; 114166095 free inodes.

server3 `/var/tmp`: 84084850688 available bytes; 95.31% used; 114166095 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106095362048 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106095362048 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 106995793920 available bytes; 98.52% used; 224929206 free inodes.

server4 `/tmp`: 106095362048 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106095362048 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
