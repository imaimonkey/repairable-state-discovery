# V2R cluster inventory

2026-09-24T04:45:22.356731+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324623474688 available bytes; 81.89% used; 112492843 free inodes.

server1 `/home`: 324623474688 available bytes; 81.89% used; 112492843 free inodes.

server1 `/tmp`: 324623474688 available bytes; 81.89% used; 112492843 free inodes.

server1 `/var/tmp`: 324623474688 available bytes; 81.89% used; 112492843 free inodes.

server1 `/mnt/raid5`: 464988426240 available bytes; 97.87% used; 337724621 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40769921024 available bytes; 97.73% used; 110430474 free inodes.

server2 `/home`: 40769921024 available bytes; 97.73% used; 110430474 free inodes.

server2 `/tmp`: 40769921024 available bytes; 97.73% used; 110430474 free inodes.

server2 `/var/tmp`: 40769921024 available bytes; 97.73% used; 110430474 free inodes.

server2 `/mnt/raid5`: 524329889792 available bytes; 96.38% used; 445195560 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292401270784 available bytes; 83.68% used; 114200242 free inodes.

server3 `/home`: 292401270784 available bytes; 83.68% used; 114200242 free inodes.

server3 `/data`: 24357470208 available bytes; 99.66% used; 225840671 free inodes.

server3 `/tmp`: 292401270784 available bytes; 83.68% used; 114200242 free inodes.

server3 `/var/tmp`: 292401270784 available bytes; 83.68% used; 114200242 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105836187648 available bytes; 94.09% used; 114349396 free inodes.

server4 `/home`: 105836187648 available bytes; 94.09% used; 114349396 free inodes.

server4 `/data`: 253381718016 available bytes; 96.50% used; 225366859 free inodes.

server4 `/tmp`: 105836187648 available bytes; 94.09% used; 114349396 free inodes.

server4 `/var/tmp`: 105836187648 available bytes; 94.09% used; 114349396 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
