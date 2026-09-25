# V2R cluster inventory

2026-09-25T03:59:06.797488+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318930583552 available bytes; 82.21% used; 112480368 free inodes.

server1 `/home`: 318930583552 available bytes; 82.21% used; 112480368 free inodes.

server1 `/tmp`: 318930583552 available bytes; 82.21% used; 112480368 free inodes.

server1 `/var/tmp`: 318930583552 available bytes; 82.21% used; 112480368 free inodes.

server1 `/mnt/raid5`: 395057549312 available bytes; 98.19% used; 337595433 free inodes.
| server2 | True | ['4'] | [] | reference_compatible=False |

server2 `/`: 22964920320 available bytes; 98.72% used; 110410446 free inodes.

server2 `/home`: 22964920320 available bytes; 98.72% used; 110410446 free inodes.

server2 `/tmp`: 22964920320 available bytes; 98.72% used; 110410446 free inodes.

server2 `/var/tmp`: 22964920320 available bytes; 98.72% used; 110410446 free inodes.

server2 `/mnt/raid5`: 464020643840 available bytes; 96.79% used; 445111142 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84341678080 available bytes; 95.29% used; 114156070 free inodes.

server3 `/home`: 84341678080 available bytes; 95.29% used; 114156070 free inodes.

server3 `/data`: 144119799808 available bytes; 98.01% used; 225816800 free inodes.

server3 `/tmp`: 84341678080 available bytes; 95.29% used; 114156070 free inodes.

server3 `/var/tmp`: 84341678080 available bytes; 95.29% used; 114156070 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105682898944 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105682898944 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 36948791296 available bytes; 99.49% used; 224964726 free inodes.

server4 `/tmp`: 105682898944 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105682898944 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
