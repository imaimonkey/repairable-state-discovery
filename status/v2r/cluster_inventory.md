# V2R cluster inventory

2026-09-23T22:10:09.651164+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325706555392 available bytes; 81.83% used; 112501409 free inodes.

server1 `/home`: 325706555392 available bytes; 81.83% used; 112501409 free inodes.

server1 `/tmp`: 325706555392 available bytes; 81.83% used; 112501409 free inodes.

server1 `/var/tmp`: 325706555392 available bytes; 81.83% used; 112501409 free inodes.

server1 `/mnt/raid5`: 1388113494016 available bytes; 93.63% used; 337739878 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41095794688 available bytes; 97.71% used; 110432653 free inodes.

server2 `/home`: 41095794688 available bytes; 97.71% used; 110432653 free inodes.

server2 `/tmp`: 41095794688 available bytes; 97.71% used; 110432653 free inodes.

server2 `/var/tmp`: 41095794688 available bytes; 97.71% used; 110432653 free inodes.

server2 `/mnt/raid5`: 537277980672 available bytes; 96.29% used; 445207489 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292728205312 available bytes; 83.66% used; 114201604 free inodes.

server3 `/home`: 292728205312 available bytes; 83.66% used; 114201604 free inodes.

server3 `/data`: 82446794752 available bytes; 98.86% used; 225847696 free inodes.

server3 `/tmp`: 292728205312 available bytes; 83.66% used; 114201604 free inodes.

server3 `/var/tmp`: 292728205312 available bytes; 83.66% used; 114201604 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106426920960 available bytes; 94.06% used; 114355255 free inodes.

server4 `/home`: 106426920960 available bytes; 94.06% used; 114355255 free inodes.

server4 `/data`: 300167737344 available bytes; 95.85% used; 225442373 free inodes.

server4 `/tmp`: 106426920960 available bytes; 94.06% used; 114355255 free inodes.

server4 `/var/tmp`: 106426920960 available bytes; 94.06% used; 114355255 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
