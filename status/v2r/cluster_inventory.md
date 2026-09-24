# V2R cluster inventory

2026-09-24T06:54:54.290083+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324484263936 available bytes; 81.90% used; 112491421 free inodes.

server1 `/home`: 324484263936 available bytes; 81.90% used; 112491421 free inodes.

server1 `/tmp`: 324484263936 available bytes; 81.90% used; 112491421 free inodes.

server1 `/var/tmp`: 324484263936 available bytes; 81.90% used; 112491421 free inodes.

server1 `/mnt/raid5`: 517423591424 available bytes; 97.63% used; 337722846 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57864626176 available bytes; 96.77% used; 110431181 free inodes.

server2 `/home`: 57864626176 available bytes; 96.77% used; 110431181 free inodes.

server2 `/tmp`: 57864626176 available bytes; 96.77% used; 110431181 free inodes.

server2 `/var/tmp`: 57864626176 available bytes; 96.77% used; 110431181 free inodes.

server2 `/mnt/raid5`: 519486455808 available bytes; 96.41% used; 445191293 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126773444608 available bytes; 92.93% used; 114175140 free inodes.

server3 `/home`: 126773444608 available bytes; 92.93% used; 114175140 free inodes.

server3 `/data`: 139264581632 available bytes; 98.08% used; 225834866 free inodes.

server3 `/tmp`: 126773444608 available bytes; 92.93% used; 114175140 free inodes.

server3 `/var/tmp`: 126773444608 available bytes; 92.93% used; 114175140 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105804234752 available bytes; 94.10% used; 114349240 free inodes.

server4 `/home`: 105804234752 available bytes; 94.10% used; 114349240 free inodes.

server4 `/data`: 307403567104 available bytes; 95.75% used; 225367943 free inodes.

server4 `/tmp`: 105804234752 available bytes; 94.10% used; 114349240 free inodes.

server4 `/var/tmp`: 105804234752 available bytes; 94.10% used; 114349240 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
