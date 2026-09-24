# V2R cluster inventory

2026-09-24T16:11:34.468792+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324026892288 available bytes; 81.92% used; 112481455 free inodes.

server1 `/home`: 324026892288 available bytes; 81.92% used; 112481455 free inodes.

server1 `/tmp`: 324026892288 available bytes; 81.92% used; 112481455 free inodes.

server1 `/var/tmp`: 324026892288 available bytes; 81.92% used; 112481455 free inodes.

server1 `/mnt/raid5`: 416613871616 available bytes; 98.09% used; 337655535 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57347260416 available bytes; 96.80% used; 110427087 free inodes.

server2 `/home`: 57347260416 available bytes; 96.80% used; 110427087 free inodes.

server2 `/tmp`: 57347260416 available bytes; 96.80% used; 110427087 free inodes.

server2 `/var/tmp`: 57347260416 available bytes; 96.80% used; 110427087 free inodes.

server2 `/mnt/raid5`: 500966223872 available bytes; 96.54% used; 445164459 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84323790848 available bytes; 95.29% used; 114153901 free inodes.

server3 `/home`: 84323790848 available bytes; 95.29% used; 114153901 free inodes.

server3 `/data`: 160010235904 available bytes; 97.79% used; 225805655 free inodes.

server3 `/tmp`: 84323790848 available bytes; 95.29% used; 114153901 free inodes.

server3 `/var/tmp`: 84323790848 available bytes; 95.29% used; 114153901 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105697849344 available bytes; 94.10% used; 114348610 free inodes.

server4 `/home`: 105697849344 available bytes; 94.10% used; 114348610 free inodes.

server4 `/data`: 89323417600 available bytes; 98.77% used; 225256137 free inodes.

server4 `/tmp`: 105697849344 available bytes; 94.10% used; 114348610 free inodes.

server4 `/var/tmp`: 105697849344 available bytes; 94.10% used; 114348610 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
