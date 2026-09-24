# V2R cluster inventory

2026-09-24T02:00:04.903853+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325446410240 available bytes; 81.84% used; 112499304 free inodes.

server1 `/home`: 325446410240 available bytes; 81.84% used; 112499304 free inodes.

server1 `/tmp`: 325446410240 available bytes; 81.84% used; 112499304 free inodes.

server1 `/var/tmp`: 325446410240 available bytes; 81.84% used; 112499304 free inodes.

server1 `/mnt/raid5`: 774087704576 available bytes; 96.45% used; 337733649 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40920604672 available bytes; 97.72% used; 110431761 free inodes.

server2 `/home`: 40920604672 available bytes; 97.72% used; 110431761 free inodes.

server2 `/tmp`: 40920604672 available bytes; 97.72% used; 110431761 free inodes.

server2 `/var/tmp`: 40920604672 available bytes; 97.72% used; 110431761 free inodes.

server2 `/mnt/raid5`: 529944838144 available bytes; 96.34% used; 445200453 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292713361408 available bytes; 83.67% used; 114210973 free inodes.

server3 `/home`: 292713361408 available bytes; 83.67% used; 114210973 free inodes.

server3 `/data`: 60363059200 available bytes; 99.17% used; 225841689 free inodes.

server3 `/tmp`: 292713361408 available bytes; 83.67% used; 114210973 free inodes.

server3 `/var/tmp`: 292713361408 available bytes; 83.67% used; 114210973 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105938305024 available bytes; 94.09% used; 114348463 free inodes.

server4 `/home`: 105938305024 available bytes; 94.09% used; 114348463 free inodes.

server4 `/data`: 289776586752 available bytes; 96.00% used; 225388486 free inodes.

server4 `/tmp`: 105938305024 available bytes; 94.09% used; 114348463 free inodes.

server4 `/var/tmp`: 105938305024 available bytes; 94.09% used; 114348463 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
