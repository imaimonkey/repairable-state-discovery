# V2R cluster inventory

2026-09-24T07:52:51.143234+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324418588672 available bytes; 81.90% used; 112490829 free inodes.

server1 `/home`: 324418588672 available bytes; 81.90% used; 112490829 free inodes.

server1 `/tmp`: 324418588672 available bytes; 81.90% used; 112490829 free inodes.

server1 `/var/tmp`: 324418588672 available bytes; 81.90% used; 112490829 free inodes.

server1 `/mnt/raid5`: 509706129408 available bytes; 97.66% used; 337722410 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57830518784 available bytes; 96.77% used; 110431092 free inodes.

server2 `/home`: 57830518784 available bytes; 96.77% used; 110431092 free inodes.

server2 `/tmp`: 57830518784 available bytes; 96.77% used; 110431092 free inodes.

server2 `/var/tmp`: 57830518784 available bytes; 96.77% used; 110431092 free inodes.

server2 `/mnt/raid5`: 517590343680 available bytes; 96.42% used; 445180807 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 95506952192 available bytes; 94.67% used; 114200197 free inodes.

server3 `/home`: 95506952192 available bytes; 94.67% used; 114200197 free inodes.

server3 `/data`: 157250777088 available bytes; 97.83% used; 225839143 free inodes.

server3 `/tmp`: 95506952192 available bytes; 94.67% used; 114200197 free inodes.

server3 `/var/tmp`: 95506952192 available bytes; 94.67% used; 114200197 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779683328 available bytes; 94.10% used; 114349172 free inodes.

server4 `/home`: 105779683328 available bytes; 94.10% used; 114349172 free inodes.

server4 `/data`: 284241514496 available bytes; 96.07% used; 225366101 free inodes.

server4 `/tmp`: 105779683328 available bytes; 94.10% used; 114349172 free inodes.

server4 `/var/tmp`: 105779683328 available bytes; 94.10% used; 114349172 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
