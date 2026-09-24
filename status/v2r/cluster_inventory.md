# V2R cluster inventory

2026-09-24T14:59:54.047941+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324045225984 available bytes; 81.92% used; 112481469 free inodes.

server1 `/home`: 324045225984 available bytes; 81.92% used; 112481469 free inodes.

server1 `/tmp`: 324045225984 available bytes; 81.92% used; 112481469 free inodes.

server1 `/var/tmp`: 324045225984 available bytes; 81.92% used; 112481469 free inodes.

server1 `/mnt/raid5`: 416840331264 available bytes; 98.09% used; 337664733 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57427783680 available bytes; 96.80% used; 110427807 free inodes.

server2 `/home`: 57427783680 available bytes; 96.80% used; 110427807 free inodes.

server2 `/tmp`: 57427783680 available bytes; 96.80% used; 110427807 free inodes.

server2 `/var/tmp`: 57427783680 available bytes; 96.80% used; 110427807 free inodes.

server2 `/mnt/raid5`: 503601717248 available bytes; 96.52% used; 445166913 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84828733440 available bytes; 95.27% used; 114182234 free inodes.

server3 `/home`: 84828733440 available bytes; 95.27% used; 114182234 free inodes.

server3 `/data`: 160607105024 available bytes; 97.78% used; 225807552 free inodes.

server3 `/tmp`: 84828733440 available bytes; 95.27% used; 114182234 free inodes.

server3 `/var/tmp`: 84828733440 available bytes; 95.27% used; 114182234 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105719623680 available bytes; 94.10% used; 114348664 free inodes.

server4 `/home`: 105719623680 available bytes; 94.10% used; 114348664 free inodes.

server4 `/data`: 69131698176 available bytes; 99.04% used; 225256967 free inodes.

server4 `/tmp`: 105719623680 available bytes; 94.10% used; 114348664 free inodes.

server4 `/var/tmp`: 105719623680 available bytes; 94.10% used; 114348664 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
