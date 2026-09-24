# V2R cluster inventory

2026-09-24T19:00:06.297287+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323995959296 available bytes; 81.93% used; 112481461 free inodes.

server1 `/home`: 323995959296 available bytes; 81.93% used; 112481461 free inodes.

server1 `/tmp`: 323995959296 available bytes; 81.93% used; 112481461 free inodes.

server1 `/var/tmp`: 323995959296 available bytes; 81.93% used; 112481461 free inodes.

server1 `/mnt/raid5`: 416257609728 available bytes; 98.09% used; 337635888 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54471053312 available bytes; 96.96% used; 110411935 free inodes.

server2 `/home`: 54471053312 available bytes; 96.96% used; 110411935 free inodes.

server2 `/tmp`: 54471053312 available bytes; 96.96% used; 110411935 free inodes.

server2 `/var/tmp`: 54471053312 available bytes; 96.96% used; 110411935 free inodes.

server2 `/mnt/raid5`: 495793631232 available bytes; 96.57% used; 445159634 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84409839616 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84409839616 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152540770304 available bytes; 97.89% used; 225800005 free inodes.

server3 `/tmp`: 84409839616 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84409839616 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105660956672 available bytes; 94.10% used; 114348475 free inodes.

server4 `/home`: 105660956672 available bytes; 94.10% used; 114348475 free inodes.

server4 `/data`: 89930706944 available bytes; 98.76% used; 225267371 free inodes.

server4 `/tmp`: 105660956672 available bytes; 94.10% used; 114348475 free inodes.

server4 `/var/tmp`: 105660956672 available bytes; 94.10% used; 114348475 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
