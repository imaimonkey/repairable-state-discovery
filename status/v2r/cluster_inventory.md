# V2R cluster inventory

2026-09-25T01:42:18.217385+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319075745792 available bytes; 82.20% used; 112480769 free inodes.

server1 `/home`: 319075745792 available bytes; 82.20% used; 112480769 free inodes.

server1 `/tmp`: 319075745792 available bytes; 82.20% used; 112480769 free inodes.

server1 `/var/tmp`: 319075745792 available bytes; 82.20% used; 112480769 free inodes.

server1 `/mnt/raid5`: 416459071488 available bytes; 98.09% used; 337611529 free inodes.
| server2 | True | ['2', '3', '6'] | [] | reference_compatible=False |

server2 `/`: 23042859008 available bytes; 98.71% used; 110410778 free inodes.

server2 `/home`: 23042859008 available bytes; 98.71% used; 110410778 free inodes.

server2 `/tmp`: 23042859008 available bytes; 98.71% used; 110410778 free inodes.

server2 `/var/tmp`: 23042859008 available bytes; 98.71% used; 110410778 free inodes.

server2 `/mnt/raid5`: 490729742336 available bytes; 96.61% used; 445161016 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84353024000 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84353024000 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 146478764032 available bytes; 97.98% used; 225812065 free inodes.

server3 `/tmp`: 84353024000 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84353024000 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105770147840 available bytes; 94.10% used; 114348287 free inodes.

server4 `/home`: 105770147840 available bytes; 94.10% used; 114348287 free inodes.

server4 `/data`: 53308608512 available bytes; 99.26% used; 225030617 free inodes.

server4 `/tmp`: 105770147840 available bytes; 94.10% used; 114348287 free inodes.

server4 `/var/tmp`: 105770147840 available bytes; 94.10% used; 114348287 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
