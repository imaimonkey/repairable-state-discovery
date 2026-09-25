# V2R cluster inventory

2026-09-25T01:31:33.204958+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319077097472 available bytes; 82.20% used; 112480757 free inodes.

server1 `/home`: 319077097472 available bytes; 82.20% used; 112480757 free inodes.

server1 `/tmp`: 319077097472 available bytes; 82.20% used; 112480757 free inodes.

server1 `/var/tmp`: 319077097472 available bytes; 82.20% used; 112480757 free inodes.

server1 `/mnt/raid5`: 416478203904 available bytes; 98.09% used; 337612778 free inodes.
| server2 | True | ['2', '6'] | [] | reference_compatible=False |

server2 `/`: 23050551296 available bytes; 98.71% used; 110410766 free inodes.

server2 `/home`: 23050551296 available bytes; 98.71% used; 110410766 free inodes.

server2 `/tmp`: 23050551296 available bytes; 98.71% used; 110410766 free inodes.

server2 `/var/tmp`: 23050551296 available bytes; 98.71% used; 110410766 free inodes.

server2 `/mnt/raid5`: 491052347392 available bytes; 96.61% used; 445161328 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84355207168 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84355207168 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 146668781568 available bytes; 97.97% used; 225812273 free inodes.

server3 `/tmp`: 84355207168 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84355207168 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105778835456 available bytes; 94.10% used; 114348289 free inodes.

server4 `/home`: 105778835456 available bytes; 94.10% used; 114348289 free inodes.

server4 `/data`: 53317017600 available bytes; 99.26% used; 225030627 free inodes.

server4 `/tmp`: 105778835456 available bytes; 94.10% used; 114348289 free inodes.

server4 `/var/tmp`: 105778835456 available bytes; 94.10% used; 114348289 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
