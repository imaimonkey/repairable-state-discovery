# V2R cluster inventory

2026-09-24T16:05:15.409401+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324028006400 available bytes; 81.92% used; 112481448 free inodes.

server1 `/home`: 324028006400 available bytes; 81.92% used; 112481448 free inodes.

server1 `/tmp`: 324028006400 available bytes; 81.92% used; 112481448 free inodes.

server1 `/var/tmp`: 324028006400 available bytes; 81.92% used; 112481448 free inodes.

server1 `/mnt/raid5`: 416626860032 available bytes; 98.09% used; 337656264 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57352650752 available bytes; 96.80% used; 110427153 free inodes.

server2 `/home`: 57352650752 available bytes; 96.80% used; 110427153 free inodes.

server2 `/tmp`: 57352650752 available bytes; 96.80% used; 110427153 free inodes.

server2 `/var/tmp`: 57352650752 available bytes; 96.80% used; 110427153 free inodes.

server2 `/mnt/raid5`: 501708087296 available bytes; 96.53% used; 445164923 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84851142656 available bytes; 95.26% used; 114183388 free inodes.

server3 `/home`: 84851142656 available bytes; 95.26% used; 114183388 free inodes.

server3 `/data`: 160048533504 available bytes; 97.79% used; 225805816 free inodes.

server3 `/tmp`: 84851142656 available bytes; 95.26% used; 114183388 free inodes.

server3 `/var/tmp`: 84851142656 available bytes; 95.26% used; 114183388 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105698086912 available bytes; 94.10% used; 114348610 free inodes.

server4 `/home`: 105698086912 available bytes; 94.10% used; 114348610 free inodes.

server4 `/data`: 89333657600 available bytes; 98.77% used; 225256245 free inodes.

server4 `/tmp`: 105698086912 available bytes; 94.10% used; 114348610 free inodes.

server4 `/var/tmp`: 105698086912 available bytes; 94.10% used; 114348610 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
