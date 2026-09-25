# V2R cluster inventory

2026-09-25T14:23:14.119023+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319156011008 available bytes; 82.20% used; 112476975 free inodes.

server1 `/home`: 319156011008 available bytes; 82.20% used; 112476975 free inodes.

server1 `/tmp`: 319156011008 available bytes; 82.20% used; 112476975 free inodes.

server1 `/var/tmp`: 319156011008 available bytes; 82.20% used; 112476975 free inodes.

server1 `/mnt/raid5`: 364068859904 available bytes; 98.33% used; 337547384 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4721713152 available bytes; 99.74% used; 110407465 free inodes.

server2 `/home`: 4721713152 available bytes; 99.74% used; 110407465 free inodes.

server2 `/tmp`: 4721713152 available bytes; 99.74% used; 110407465 free inodes.

server2 `/var/tmp`: 4721713152 available bytes; 99.74% used; 110407465 free inodes.

server2 `/mnt/raid5`: 321629663232 available bytes; 97.78% used; 445075610 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84272742400 available bytes; 95.30% used; 114154464 free inodes.

server3 `/home`: 84272742400 available bytes; 95.30% used; 114154464 free inodes.

server3 `/data`: 142210342912 available bytes; 98.03% used; 225808827 free inodes.

server3 `/tmp`: 84272742400 available bytes; 95.30% used; 114154464 free inodes.

server3 `/var/tmp`: 84272742400 available bytes; 95.30% used; 114154464 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654525952 available bytes; 94.10% used; 114349711 free inodes.

server4 `/home`: 105654525952 available bytes; 94.10% used; 114349711 free inodes.

server4 `/data`: 231449919488 available bytes; 96.80% used; 224946706 free inodes.

server4 `/tmp`: 105654525952 available bytes; 94.10% used; 114349711 free inodes.

server4 `/var/tmp`: 105654525952 available bytes; 94.10% used; 114349711 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
