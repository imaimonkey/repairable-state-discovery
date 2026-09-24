# V2R cluster inventory

2026-09-24T19:17:02.961281+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323991883776 available bytes; 81.93% used; 112481460 free inodes.

server1 `/home`: 323991883776 available bytes; 81.93% used; 112481460 free inodes.

server1 `/tmp`: 323991883776 available bytes; 81.93% used; 112481460 free inodes.

server1 `/var/tmp`: 323991883776 available bytes; 81.93% used; 112481460 free inodes.

server1 `/mnt/raid5`: 415643938816 available bytes; 98.09% used; 337633885 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54463311872 available bytes; 96.96% used; 110411914 free inodes.

server2 `/home`: 54463311872 available bytes; 96.96% used; 110411914 free inodes.

server2 `/tmp`: 54463311872 available bytes; 96.96% used; 110411914 free inodes.

server2 `/var/tmp`: 54463311872 available bytes; 96.96% used; 110411914 free inodes.

server2 `/mnt/raid5`: 495287906304 available bytes; 96.58% used; 445159199 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84405571584 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84405571584 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152385826816 available bytes; 97.89% used; 225799698 free inodes.

server3 `/tmp`: 84405571584 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84405571584 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105660375040 available bytes; 94.10% used; 114348467 free inodes.

server4 `/home`: 105660375040 available bytes; 94.10% used; 114348467 free inodes.

server4 `/data`: 89904529408 available bytes; 98.76% used; 225267163 free inodes.

server4 `/tmp`: 105660375040 available bytes; 94.10% used; 114348467 free inodes.

server4 `/var/tmp`: 105660375040 available bytes; 94.10% used; 114348467 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
