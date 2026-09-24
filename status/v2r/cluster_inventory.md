# V2R cluster inventory

2026-09-24T19:47:53.035083+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323988381696 available bytes; 81.93% used; 112481463 free inodes.

server1 `/home`: 323988381696 available bytes; 81.93% used; 112481463 free inodes.

server1 `/tmp`: 323988381696 available bytes; 81.93% used; 112481463 free inodes.

server1 `/var/tmp`: 323988381696 available bytes; 81.93% used; 112481463 free inodes.

server1 `/mnt/raid5`: 415578574848 available bytes; 98.09% used; 337630288 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 44744278016 available bytes; 97.50% used; 110411669 free inodes.

server2 `/home`: 44744278016 available bytes; 97.50% used; 110411669 free inodes.

server2 `/tmp`: 44744278016 available bytes; 97.50% used; 110411669 free inodes.

server2 `/var/tmp`: 44744278016 available bytes; 97.50% used; 110411669 free inodes.

server2 `/mnt/raid5`: 494318161920 available bytes; 96.58% used; 445158142 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84399357952 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84399357952 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152101314560 available bytes; 97.90% used; 225799167 free inodes.

server3 `/tmp`: 84399357952 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84399357952 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105642192896 available bytes; 94.10% used; 114348430 free inodes.

server4 `/home`: 105642192896 available bytes; 94.10% used; 114348430 free inodes.

server4 `/data`: 89841561600 available bytes; 98.76% used; 225266462 free inodes.

server4 `/tmp`: 105642192896 available bytes; 94.10% used; 114348430 free inodes.

server4 `/var/tmp`: 105642192896 available bytes; 94.10% used; 114348430 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
