# V2R cluster inventory

2026-09-25T05:08:24.573446+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318901018624 available bytes; 82.21% used; 112480297 free inodes.

server1 `/home`: 318901018624 available bytes; 82.21% used; 112480297 free inodes.

server1 `/tmp`: 318901018624 available bytes; 82.21% used; 112480297 free inodes.

server1 `/var/tmp`: 318901018624 available bytes; 82.21% used; 112480297 free inodes.

server1 `/mnt/raid5`: 408606588928 available bytes; 98.13% used; 337571027 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22928875520 available bytes; 98.72% used; 110410436 free inodes.

server2 `/home`: 22928875520 available bytes; 98.72% used; 110410436 free inodes.

server2 `/tmp`: 22928875520 available bytes; 98.72% used; 110410436 free inodes.

server2 `/var/tmp`: 22928875520 available bytes; 98.72% used; 110410436 free inodes.

server2 `/mnt/raid5`: 461844193280 available bytes; 96.81% used; 445108944 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84339654656 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84339654656 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 142817779712 available bytes; 98.03% used; 225815380 free inodes.

server3 `/tmp`: 84339654656 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84339654656 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105659125760 available bytes; 94.10% used; 114350406 free inodes.

server4 `/home`: 105659125760 available bytes; 94.10% used; 114350406 free inodes.

server4 `/data`: 27928547328 available bytes; 99.61% used; 224960729 free inodes.

server4 `/tmp`: 105659125760 available bytes; 94.10% used; 114350406 free inodes.

server4 `/var/tmp`: 105659125760 available bytes; 94.10% used; 114350406 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
