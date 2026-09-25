# V2R cluster inventory

2026-09-25T04:46:55.674181+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318912344064 available bytes; 82.21% used; 112480349 free inodes.

server1 `/home`: 318912344064 available bytes; 82.21% used; 112480349 free inodes.

server1 `/tmp`: 318912344064 available bytes; 82.21% used; 112480349 free inodes.

server1 `/var/tmp`: 318912344064 available bytes; 82.21% used; 112480349 free inodes.

server1 `/mnt/raid5`: 408683798528 available bytes; 98.13% used; 337589644 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22947606528 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22947606528 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22947606528 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22947606528 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 462516666368 available bytes; 96.80% used; 445109429 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84339716096 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84339716096 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 143247110144 available bytes; 98.02% used; 225815830 free inodes.

server3 `/tmp`: 84339716096 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84339716096 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105663811584 available bytes; 94.10% used; 114350589 free inodes.

server4 `/home`: 105663811584 available bytes; 94.10% used; 114350589 free inodes.

server4 `/data`: 29565169664 available bytes; 99.59% used; 224962018 free inodes.

server4 `/tmp`: 105663811584 available bytes; 94.10% used; 114350589 free inodes.

server4 `/var/tmp`: 105663811584 available bytes; 94.10% used; 114350589 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
