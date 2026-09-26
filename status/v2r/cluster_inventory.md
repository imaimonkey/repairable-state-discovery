# V2R cluster inventory

2026-09-26T16:21:45.730630+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318131052544 available bytes; 82.25% used; 112473898 free inodes.

server1 `/home`: 318131052544 available bytes; 82.25% used; 112473898 free inodes.

server1 `/tmp`: 318131052544 available bytes; 82.25% used; 112473898 free inodes.

server1 `/var/tmp`: 318131052544 available bytes; 82.25% used; 112473898 free inodes.

server1 `/mnt/raid5`: 654099861504 available bytes; 97.00% used; 337531408 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 18032795648 available bytes; 98.99% used; 110367524 free inodes.

server2 `/home`: 18032795648 available bytes; 98.99% used; 110367524 free inodes.

server2 `/tmp`: 18032795648 available bytes; 98.99% used; 110367524 free inodes.

server2 `/var/tmp`: 18032795648 available bytes; 98.99% used; 110367524 free inodes.

server2 `/mnt/raid5`: 607967965184 available bytes; 95.80% used; 444971610 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81581572096 available bytes; 95.45% used; 114077154 free inodes.

server3 `/home`: 81581572096 available bytes; 95.45% used; 114077154 free inodes.

server3 `/data`: 1349377171456 available bytes; 81.35% used; 225830828 free inodes.

server3 `/tmp`: 81581572096 available bytes; 95.45% used; 114077154 free inodes.

server3 `/var/tmp`: 81581572096 available bytes; 95.45% used; 114077154 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105953693696 available bytes; 94.09% used; 114347852 free inodes.

server4 `/home`: 105953693696 available bytes; 94.09% used; 114347852 free inodes.

server4 `/data`: 410694832128 available bytes; 94.32% used; 224824702 free inodes.

server4 `/tmp`: 105953693696 available bytes; 94.09% used; 114347852 free inodes.

server4 `/var/tmp`: 105953693696 available bytes; 94.09% used; 114347852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
