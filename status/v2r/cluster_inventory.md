# V2R cluster inventory

2026-09-24T03:59:26.057310+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324724740096 available bytes; 81.88% used; 112493594 free inodes.

server1 `/home`: 324724740096 available bytes; 81.88% used; 112493594 free inodes.

server1 `/tmp`: 324724740096 available bytes; 81.88% used; 112493594 free inodes.

server1 `/var/tmp`: 324724740096 available bytes; 81.88% used; 112493594 free inodes.

server1 `/mnt/raid5`: 416638242816 available bytes; 98.09% used; 337724784 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40812449792 available bytes; 97.72% used; 110430880 free inodes.

server2 `/home`: 40812449792 available bytes; 97.72% used; 110430880 free inodes.

server2 `/tmp`: 40812449792 available bytes; 97.72% used; 110430880 free inodes.

server2 `/var/tmp`: 40812449792 available bytes; 97.72% used; 110430880 free inodes.

server2 `/mnt/raid5`: 526334681088 available bytes; 96.36% used; 445197035 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292360355840 available bytes; 83.69% used; 114200897 free inodes.

server3 `/home`: 292360355840 available bytes; 83.69% used; 114200897 free inodes.

server3 `/data`: 33873842176 available bytes; 99.53% used; 225842423 free inodes.

server3 `/tmp`: 292360355840 available bytes; 83.69% used; 114200897 free inodes.

server3 `/var/tmp`: 292360355840 available bytes; 83.69% used; 114200897 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105791504384 available bytes; 94.10% used; 114349519 free inodes.

server4 `/home`: 105791504384 available bytes; 94.10% used; 114349519 free inodes.

server4 `/data`: 258349187072 available bytes; 96.43% used; 225382421 free inodes.

server4 `/tmp`: 105791504384 available bytes; 94.10% used; 114349519 free inodes.

server4 `/var/tmp`: 105791504384 available bytes; 94.10% used; 114349519 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
