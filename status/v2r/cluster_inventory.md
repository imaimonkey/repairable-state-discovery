# V2R cluster inventory

2026-09-24T14:47:29.718479+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324050722816 available bytes; 81.92% used; 112481473 free inodes.

server1 `/home`: 324050722816 available bytes; 81.92% used; 112481473 free inodes.

server1 `/tmp`: 324050722816 available bytes; 81.92% used; 112481473 free inodes.

server1 `/var/tmp`: 324050722816 available bytes; 81.92% used; 112481473 free inodes.

server1 `/mnt/raid5`: 416854458368 available bytes; 98.09% used; 337666180 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57438117888 available bytes; 96.80% used; 110427933 free inodes.

server2 `/home`: 57438117888 available bytes; 96.80% used; 110427933 free inodes.

server2 `/tmp`: 57438117888 available bytes; 96.80% used; 110427933 free inodes.

server2 `/var/tmp`: 57438117888 available bytes; 96.80% used; 110427933 free inodes.

server2 `/mnt/raid5`: 503947153408 available bytes; 96.52% used; 445167423 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84842192896 available bytes; 95.27% used; 114182153 free inodes.

server3 `/home`: 84842192896 available bytes; 95.27% used; 114182153 free inodes.

server3 `/data`: 160699703296 available bytes; 97.78% used; 225807797 free inodes.

server3 `/tmp`: 84842192896 available bytes; 95.27% used; 114182153 free inodes.

server3 `/var/tmp`: 84842192896 available bytes; 95.27% used; 114182153 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105758285824 available bytes; 94.10% used; 114348683 free inodes.

server4 `/home`: 105758285824 available bytes; 94.10% used; 114348683 free inodes.

server4 `/data`: 69173342208 available bytes; 99.04% used; 225256990 free inodes.

server4 `/tmp`: 105758285824 available bytes; 94.10% used; 114348683 free inodes.

server4 `/var/tmp`: 105758285824 available bytes; 94.10% used; 114348683 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
