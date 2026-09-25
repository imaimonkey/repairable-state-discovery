# V2R cluster inventory

2026-09-25T06:54:55.015460+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318871601152 available bytes; 82.21% used; 112480374 free inodes.

server1 `/home`: 318871601152 available bytes; 82.21% used; 112480374 free inodes.

server1 `/tmp`: 318871601152 available bytes; 82.21% used; 112480374 free inodes.

server1 `/var/tmp`: 318871601152 available bytes; 82.21% used; 112480374 free inodes.

server1 `/mnt/raid5`: 399724351488 available bytes; 98.17% used; 337560511 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22878474240 available bytes; 98.72% used; 110410526 free inodes.

server2 `/home`: 22878474240 available bytes; 98.72% used; 110410526 free inodes.

server2 `/tmp`: 22878474240 available bytes; 98.72% used; 110410526 free inodes.

server2 `/var/tmp`: 22878474240 available bytes; 98.72% used; 110410526 free inodes.

server2 `/mnt/raid5`: 338019520512 available bytes; 97.66% used; 445098581 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 84447608832 available bytes; 95.29% used; 114156040 free inodes.

server3 `/home`: 84447608832 available bytes; 95.29% used; 114156040 free inodes.

server3 `/data`: 142451105792 available bytes; 98.03% used; 225813297 free inodes.

server3 `/tmp`: 84447608832 available bytes; 95.29% used; 114156040 free inodes.

server3 `/var/tmp`: 84447608832 available bytes; 95.29% used; 114156040 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638928384 available bytes; 94.10% used; 114350362 free inodes.

server4 `/home`: 105638928384 available bytes; 94.10% used; 114350362 free inodes.

server4 `/data`: 249505505280 available bytes; 96.55% used; 225017526 free inodes.

server4 `/tmp`: 105638928384 available bytes; 94.10% used; 114350362 free inodes.

server4 `/var/tmp`: 105638928384 available bytes; 94.10% used; 114350362 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
