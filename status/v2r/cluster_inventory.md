# V2R cluster inventory

2026-09-27T14:37:53.961794+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304748888064 available bytes; 83.00% used; 112401379 free inodes.

server1 `/home`: 304748888064 available bytes; 83.00% used; 112401379 free inodes.

server1 `/tmp`: 304748888064 available bytes; 83.00% used; 112401379 free inodes.

server1 `/var/tmp`: 304748888064 available bytes; 83.00% used; 112401379 free inodes.

server1 `/mnt/raid5`: 630114668544 available bytes; 97.11% used; 337424054 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 13406232576 available bytes; 99.25% used; 110351795 free inodes.

server2 `/home`: 13406232576 available bytes; 99.25% used; 110351795 free inodes.

server2 `/tmp`: 13406232576 available bytes; 99.25% used; 110351795 free inodes.

server2 `/var/tmp`: 13406232576 available bytes; 99.25% used; 110351795 free inodes.

server2 `/mnt/raid5`: 526607851520 available bytes; 96.36% used; 444722510 free inodes.
| server3 | True | ['0', '1'] | [] | reference_compatible=True |

server3 `/`: 78559055872 available bytes; 95.62% used; 114062784 free inodes.

server3 `/home`: 78559055872 available bytes; 95.62% used; 114062784 free inodes.

server3 `/data`: 1328708804608 available bytes; 81.64% used; 225756759 free inodes.

server3 `/tmp`: 78559055872 available bytes; 95.62% used; 114062784 free inodes.

server3 `/var/tmp`: 78559055872 available bytes; 95.62% used; 114062784 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 109778644992 available bytes; 93.87% used; 114372751 free inodes.

server4 `/home`: 109778644992 available bytes; 93.87% used; 114372751 free inodes.

server4 `/data`: 350473551872 available bytes; 95.16% used; 224727368 free inodes.

server4 `/tmp`: 109778644992 available bytes; 93.87% used; 114372751 free inodes.

server4 `/var/tmp`: 109778644992 available bytes; 93.87% used; 114372751 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
