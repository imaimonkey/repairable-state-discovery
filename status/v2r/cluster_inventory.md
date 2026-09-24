# V2R cluster inventory

2026-09-24T13:09:24.023567+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324029812736 available bytes; 81.92% used; 112481547 free inodes.

server1 `/home`: 324029812736 available bytes; 81.92% used; 112481547 free inodes.

server1 `/tmp`: 324029812736 available bytes; 81.92% used; 112481547 free inodes.

server1 `/var/tmp`: 324029812736 available bytes; 81.92% used; 112481547 free inodes.

server1 `/mnt/raid5`: 417066057728 available bytes; 98.09% used; 337677627 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57552912384 available bytes; 96.79% used; 110428949 free inodes.

server2 `/home`: 57552912384 available bytes; 96.79% used; 110428949 free inodes.

server2 `/tmp`: 57552912384 available bytes; 96.79% used; 110428949 free inodes.

server2 `/var/tmp`: 57552912384 available bytes; 96.79% used; 110428949 free inodes.

server2 `/mnt/raid5`: 507276587008 available bytes; 96.49% used; 445170693 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85060718592 available bytes; 95.25% used; 114186363 free inodes.

server3 `/home`: 85060718592 available bytes; 95.25% used; 114186363 free inodes.

server3 `/data`: 161492111360 available bytes; 97.77% used; 225809744 free inodes.

server3 `/tmp`: 85060718592 available bytes; 95.25% used; 114186363 free inodes.

server3 `/var/tmp`: 85060718592 available bytes; 95.25% used; 114186363 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105770614784 available bytes; 94.10% used; 114348757 free inodes.

server4 `/home`: 105770614784 available bytes; 94.10% used; 114348757 free inodes.

server4 `/data`: 90040594432 available bytes; 98.76% used; 225257183 free inodes.

server4 `/tmp`: 105770614784 available bytes; 94.10% used; 114348757 free inodes.

server4 `/var/tmp`: 105770614784 available bytes; 94.10% used; 114348757 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
