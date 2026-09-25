# V2R cluster inventory

2026-09-25T08:22:13.534326+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318826250240 available bytes; 82.21% used; 112480360 free inodes.

server1 `/home`: 318826250240 available bytes; 82.21% used; 112480360 free inodes.

server1 `/tmp`: 318826250240 available bytes; 82.21% used; 112480360 free inodes.

server1 `/var/tmp`: 318826250240 available bytes; 82.21% used; 112480360 free inodes.

server1 `/mnt/raid5`: 367325270016 available bytes; 98.31% used; 337557191 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22833295360 available bytes; 98.73% used; 110410480 free inodes.

server2 `/home`: 22833295360 available bytes; 98.73% used; 110410480 free inodes.

server2 `/tmp`: 22833295360 available bytes; 98.73% used; 110410480 free inodes.

server2 `/var/tmp`: 22833295360 available bytes; 98.73% used; 110410480 free inodes.

server2 `/mnt/raid5`: 333536960512 available bytes; 97.70% used; 445094729 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84438966272 available bytes; 95.29% used; 114156051 free inodes.

server3 `/home`: 84438966272 available bytes; 95.29% used; 114156051 free inodes.

server3 `/data`: 142382555136 available bytes; 98.03% used; 225811822 free inodes.

server3 `/tmp`: 84438966272 available bytes; 95.29% used; 114156051 free inodes.

server3 `/var/tmp`: 84438966272 available bytes; 95.29% used; 114156051 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105624875008 available bytes; 94.11% used; 114350334 free inodes.

server4 `/home`: 105624875008 available bytes; 94.11% used; 114350334 free inodes.

server4 `/data`: 246947196928 available bytes; 96.59% used; 225006121 free inodes.

server4 `/tmp`: 105624875008 available bytes; 94.11% used; 114350334 free inodes.

server4 `/var/tmp`: 105624875008 available bytes; 94.11% used; 114350334 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
