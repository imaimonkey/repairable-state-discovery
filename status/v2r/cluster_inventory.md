# V2R cluster inventory

2026-09-25T07:46:55.657610+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318862745600 available bytes; 82.21% used; 112480373 free inodes.

server1 `/home`: 318862745600 available bytes; 82.21% used; 112480373 free inodes.

server1 `/tmp`: 318862745600 available bytes; 82.21% used; 112480373 free inodes.

server1 `/var/tmp`: 318862745600 available bytes; 82.21% used; 112480373 free inodes.

server1 `/mnt/raid5`: 399583850496 available bytes; 98.17% used; 337558246 free inodes.
| server2 | True | ['0'] | [] | reference_compatible=False |

server2 `/`: 22849986560 available bytes; 98.73% used; 110410475 free inodes.

server2 `/home`: 22849986560 available bytes; 98.73% used; 110410475 free inodes.

server2 `/tmp`: 22849986560 available bytes; 98.73% used; 110410475 free inodes.

server2 `/var/tmp`: 22849986560 available bytes; 98.73% used; 110410475 free inodes.

server2 `/mnt/raid5`: 334607978496 available bytes; 97.69% used; 445095814 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84439232512 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84439232512 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142394281984 available bytes; 98.03% used; 225812437 free inodes.

server3 `/tmp`: 84439232512 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84439232512 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105637359616 available bytes; 94.11% used; 114350351 free inodes.

server4 `/home`: 105637359616 available bytes; 94.11% used; 114350351 free inodes.

server4 `/data`: 249056587776 available bytes; 96.56% used; 225011780 free inodes.

server4 `/tmp`: 105637359616 available bytes; 94.11% used; 114350351 free inodes.

server4 `/var/tmp`: 105637359616 available bytes; 94.11% used; 114350351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
