# V2R cluster inventory

2026-09-24T16:53:23.737109+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324023611392 available bytes; 81.92% used; 112481444 free inodes.

server1 `/home`: 324023611392 available bytes; 81.92% used; 112481444 free inodes.

server1 `/tmp`: 324023611392 available bytes; 81.92% used; 112481444 free inodes.

server1 `/var/tmp`: 324023611392 available bytes; 81.92% used; 112481444 free inodes.

server1 `/mnt/raid5`: 416521031680 available bytes; 98.09% used; 337650657 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57072357376 available bytes; 96.82% used; 110418090 free inodes.

server2 `/home`: 57072357376 available bytes; 96.82% used; 110418090 free inodes.

server2 `/tmp`: 57072357376 available bytes; 96.82% used; 110418090 free inodes.

server2 `/var/tmp`: 57072357376 available bytes; 96.82% used; 110418090 free inodes.

server2 `/mnt/raid5`: 500235579392 available bytes; 96.54% used; 445163843 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84417605632 available bytes; 95.29% used; 114156154 free inodes.

server3 `/home`: 84417605632 available bytes; 95.29% used; 114156154 free inodes.

server3 `/data`: 159191879680 available bytes; 97.80% used; 225787523 free inodes.

server3 `/tmp`: 84417605632 available bytes; 95.29% used; 114156154 free inodes.

server3 `/var/tmp`: 84417605632 available bytes; 95.29% used; 114156154 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105682735104 available bytes; 94.10% used; 114348574 free inodes.

server4 `/home`: 105682735104 available bytes; 94.10% used; 114348574 free inodes.

server4 `/data`: 89189830656 available bytes; 98.77% used; 225255144 free inodes.

server4 `/tmp`: 105682735104 available bytes; 94.10% used; 114348574 free inodes.

server4 `/var/tmp`: 105682735104 available bytes; 94.10% used; 114348574 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
