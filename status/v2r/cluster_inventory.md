# V2R cluster inventory

2026-09-25T04:46:02.113772+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318913880064 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318913880064 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318913880064 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318913880064 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 408686481408 available bytes; 98.13% used; 337589748 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22947790848 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22947790848 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22947790848 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22947790848 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 462549131264 available bytes; 96.80% used; 445109476 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339941376 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84339941376 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 143254962176 available bytes; 98.02% used; 225815851 free inodes.

server3 `/tmp`: 84339941376 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84339941376 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105663852544 available bytes; 94.10% used; 114350589 free inodes.

server4 `/home`: 105663852544 available bytes; 94.10% used; 114350589 free inodes.

server4 `/data`: 31169355776 available bytes; 99.57% used; 224962089 free inodes.

server4 `/tmp`: 105663852544 available bytes; 94.10% used; 114350589 free inodes.

server4 `/var/tmp`: 105663852544 available bytes; 94.10% used; 114350589 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
