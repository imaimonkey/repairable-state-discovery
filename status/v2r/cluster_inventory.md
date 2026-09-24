# V2R cluster inventory

2026-09-24T13:10:56.939723+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324028850176 available bytes; 81.92% used; 112481542 free inodes.

server1 `/home`: 324028850176 available bytes; 81.92% used; 112481542 free inodes.

server1 `/tmp`: 324028850176 available bytes; 81.92% used; 112481542 free inodes.

server1 `/var/tmp`: 324028850176 available bytes; 81.92% used; 112481542 free inodes.

server1 `/mnt/raid5`: 417067503616 available bytes; 98.09% used; 337677447 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57546788864 available bytes; 96.79% used; 110428933 free inodes.

server2 `/home`: 57546788864 available bytes; 96.79% used; 110428933 free inodes.

server2 `/tmp`: 57546788864 available bytes; 96.79% used; 110428933 free inodes.

server2 `/var/tmp`: 57546788864 available bytes; 96.79% used; 110428933 free inodes.

server2 `/mnt/raid5`: 507226906624 available bytes; 96.50% used; 445170538 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85059293184 available bytes; 95.25% used; 114186341 free inodes.

server3 `/home`: 85059293184 available bytes; 95.25% used; 114186341 free inodes.

server3 `/data`: 161483378688 available bytes; 97.77% used; 225809711 free inodes.

server3 `/tmp`: 85059293184 available bytes; 95.25% used; 114186341 free inodes.

server3 `/var/tmp`: 85059293184 available bytes; 95.25% used; 114186341 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105770500096 available bytes; 94.10% used; 114348753 free inodes.

server4 `/home`: 105770500096 available bytes; 94.10% used; 114348753 free inodes.

server4 `/data`: 90038329344 available bytes; 98.76% used; 225257179 free inodes.

server4 `/tmp`: 105770500096 available bytes; 94.10% used; 114348753 free inodes.

server4 `/var/tmp`: 105770500096 available bytes; 94.10% used; 114348753 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
