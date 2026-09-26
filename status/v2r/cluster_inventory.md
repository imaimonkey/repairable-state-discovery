# V2R cluster inventory

2026-09-26T15:17:46.265465+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318155403264 available bytes; 82.25% used; 112473928 free inodes.

server1 `/home`: 318155403264 available bytes; 82.25% used; 112473928 free inodes.

server1 `/tmp`: 318155403264 available bytes; 82.25% used; 112473928 free inodes.

server1 `/var/tmp`: 318155403264 available bytes; 82.25% used; 112473928 free inodes.

server1 `/mnt/raid5`: 654129733632 available bytes; 97.00% used; 337531554 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 8205160448 available bytes; 99.54% used; 110367294 free inodes.

server2 `/home`: 8205160448 available bytes; 99.54% used; 110367294 free inodes.

server2 `/tmp`: 8205160448 available bytes; 99.54% used; 110367294 free inodes.

server2 `/var/tmp`: 8205160448 available bytes; 99.54% used; 110367294 free inodes.

server2 `/mnt/raid5`: 609777971200 available bytes; 95.79% used; 444973506 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 82443218944 available bytes; 95.40% used; 114101917 free inodes.

server3 `/home`: 82443218944 available bytes; 95.40% used; 114101917 free inodes.

server3 `/data`: 1346843787264 available bytes; 81.39% used; 225809974 free inodes.

server3 `/tmp`: 82443218944 available bytes; 95.40% used; 114101917 free inodes.

server3 `/var/tmp`: 82443218944 available bytes; 95.40% used; 114101917 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105954975744 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105954975744 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410805866496 available bytes; 94.32% used; 224826057 free inodes.

server4 `/tmp`: 105954975744 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105954975744 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
