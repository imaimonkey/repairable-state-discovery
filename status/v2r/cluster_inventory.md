# V2R cluster inventory

2026-09-24T19:27:49.720143+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323994968064 available bytes; 81.93% used; 112481465 free inodes.

server1 `/home`: 323994968064 available bytes; 81.93% used; 112481465 free inodes.

server1 `/tmp`: 323994968064 available bytes; 81.93% used; 112481465 free inodes.

server1 `/var/tmp`: 323994968064 available bytes; 81.93% used; 112481465 free inodes.

server1 `/mnt/raid5`: 415617720320 available bytes; 98.09% used; 337632633 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54452301824 available bytes; 96.96% used; 110411894 free inodes.

server2 `/home`: 54452301824 available bytes; 96.96% used; 110411894 free inodes.

server2 `/tmp`: 54452301824 available bytes; 96.96% used; 110411894 free inodes.

server2 `/var/tmp`: 54452301824 available bytes; 96.96% used; 110411894 free inodes.

server2 `/mnt/raid5`: 494949965824 available bytes; 96.58% used; 445159009 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84405772288 available bytes; 95.29% used; 114156135 free inodes.

server3 `/home`: 84405772288 available bytes; 95.29% used; 114156135 free inodes.

server3 `/data`: 152297725952 available bytes; 97.90% used; 225799521 free inodes.

server3 `/tmp`: 84405772288 available bytes; 95.29% used; 114156135 free inodes.

server3 `/var/tmp`: 84405772288 available bytes; 95.29% used; 114156135 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105659879424 available bytes; 94.10% used; 114348452 free inodes.

server4 `/home`: 105659879424 available bytes; 94.10% used; 114348452 free inodes.

server4 `/data`: 89877704704 available bytes; 98.76% used; 225266862 free inodes.

server4 `/tmp`: 105659879424 available bytes; 94.10% used; 114348452 free inodes.

server4 `/var/tmp`: 105659879424 available bytes; 94.10% used; 114348452 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
