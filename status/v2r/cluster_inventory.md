# V2R cluster inventory

2026-09-25T04:07:21.846204+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318929981440 available bytes; 82.21% used; 112480374 free inodes.

server1 `/home`: 318929981440 available bytes; 82.21% used; 112480374 free inodes.

server1 `/tmp`: 318929981440 available bytes; 82.21% used; 112480374 free inodes.

server1 `/var/tmp`: 318929981440 available bytes; 82.21% used; 112480374 free inodes.

server1 `/mnt/raid5`: 395036020736 available bytes; 98.19% used; 337594451 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22963666944 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 22963666944 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 22963666944 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 22963666944 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 463203733504 available bytes; 96.80% used; 445110752 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341547008 available bytes; 95.29% used; 114156072 free inodes.

server3 `/home`: 84341547008 available bytes; 95.29% used; 114156072 free inodes.

server3 `/data`: 143981490176 available bytes; 98.01% used; 225816612 free inodes.

server3 `/tmp`: 84341547008 available bytes; 95.29% used; 114156072 free inodes.

server3 `/var/tmp`: 84341547008 available bytes; 95.29% used; 114156072 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674268672 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105674268672 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 35309477888 available bytes; 99.51% used; 224964149 free inodes.

server4 `/tmp`: 105674268672 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105674268672 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
