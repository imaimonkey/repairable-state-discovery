# V2R cluster inventory

2026-09-25T04:05:14.823724+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318930452480 available bytes; 82.21% used; 112480380 free inodes.

server1 `/home`: 318930452480 available bytes; 82.21% used; 112480380 free inodes.

server1 `/tmp`: 318930452480 available bytes; 82.21% used; 112480380 free inodes.

server1 `/var/tmp`: 318930452480 available bytes; 82.21% used; 112480380 free inodes.

server1 `/mnt/raid5`: 395039072256 available bytes; 98.19% used; 337594691 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22963630080 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 22963630080 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 22963630080 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 22963630080 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 463810428928 available bytes; 96.80% used; 445110955 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84341948416 available bytes; 95.29% used; 114156074 free inodes.

server3 `/home`: 84341948416 available bytes; 95.29% used; 114156074 free inodes.

server3 `/data`: 144015740928 available bytes; 98.01% used; 225816653 free inodes.

server3 `/tmp`: 84341948416 available bytes; 95.29% used; 114156074 free inodes.

server3 `/var/tmp`: 84341948416 available bytes; 95.29% used; 114156074 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105682718720 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105682718720 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 35308195840 available bytes; 99.51% used; 224964245 free inodes.

server4 `/tmp`: 105682718720 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105682718720 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
