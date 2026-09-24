# V2R cluster inventory

2026-09-24T06:55:16.624134+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324483985408 available bytes; 81.90% used; 112491417 free inodes.

server1 `/home`: 324483985408 available bytes; 81.90% used; 112491417 free inodes.

server1 `/tmp`: 324483985408 available bytes; 81.90% used; 112491417 free inodes.

server1 `/var/tmp`: 324483985408 available bytes; 81.90% used; 112491417 free inodes.

server1 `/mnt/raid5`: 517423591424 available bytes; 97.63% used; 337722846 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57864384512 available bytes; 96.77% used; 110431181 free inodes.

server2 `/home`: 57864384512 available bytes; 96.77% used; 110431181 free inodes.

server2 `/tmp`: 57864384512 available bytes; 96.77% used; 110431181 free inodes.

server2 `/var/tmp`: 57864384512 available bytes; 96.77% used; 110431181 free inodes.

server2 `/mnt/raid5`: 519476580352 available bytes; 96.41% used; 445191266 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126773096448 available bytes; 92.93% used; 114175140 free inodes.

server3 `/home`: 126773096448 available bytes; 92.93% used; 114175140 free inodes.

server3 `/data`: 139263455232 available bytes; 98.08% used; 225834851 free inodes.

server3 `/tmp`: 126773096448 available bytes; 92.93% used; 114175140 free inodes.

server3 `/var/tmp`: 126773096448 available bytes; 92.93% used; 114175140 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105799090176 available bytes; 94.10% used; 114349219 free inodes.

server4 `/home`: 105799090176 available bytes; 94.10% used; 114349219 free inodes.

server4 `/data`: 307148529664 available bytes; 95.76% used; 225367931 free inodes.

server4 `/tmp`: 105799090176 available bytes; 94.10% used; 114349219 free inodes.

server4 `/var/tmp`: 105799090176 available bytes; 94.10% used; 114349219 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
