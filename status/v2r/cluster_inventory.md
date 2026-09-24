# V2R cluster inventory

2026-09-24T19:37:04.269439+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323990388736 available bytes; 81.93% used; 112481455 free inodes.

server1 `/home`: 323990388736 available bytes; 81.93% used; 112481455 free inodes.

server1 `/tmp`: 323990388736 available bytes; 81.93% used; 112481455 free inodes.

server1 `/var/tmp`: 323990388736 available bytes; 81.93% used; 112481455 free inodes.

server1 `/mnt/raid5`: 415609466880 available bytes; 98.09% used; 337631556 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 54452318208 available bytes; 96.96% used; 110411857 free inodes.

server2 `/home`: 54452318208 available bytes; 96.96% used; 110411857 free inodes.

server2 `/tmp`: 54452318208 available bytes; 96.96% used; 110411857 free inodes.

server2 `/var/tmp`: 54452318208 available bytes; 96.96% used; 110411857 free inodes.

server2 `/mnt/raid5`: 494108839936 available bytes; 96.59% used; 445158587 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84400439296 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84400439296 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152201543680 available bytes; 97.90% used; 225799369 free inodes.

server3 `/tmp`: 84400439296 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84400439296 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105659584512 available bytes; 94.10% used; 114348452 free inodes.

server4 `/home`: 105659584512 available bytes; 94.10% used; 114348452 free inodes.

server4 `/data`: 89859362816 available bytes; 98.76% used; 225266664 free inodes.

server4 `/tmp`: 105659584512 available bytes; 94.10% used; 114348452 free inodes.

server4 `/var/tmp`: 105659584512 available bytes; 94.10% used; 114348452 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
