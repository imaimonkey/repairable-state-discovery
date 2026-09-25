# V2R cluster inventory

2026-09-25T17:06:48.749042+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318681104384 available bytes; 82.22% used; 112476355 free inodes.

server1 `/home`: 318681104384 available bytes; 82.22% used; 112476355 free inodes.

server1 `/tmp`: 318681104384 available bytes; 82.22% used; 112476355 free inodes.

server1 `/var/tmp`: 318681104384 available bytes; 82.22% used; 112476355 free inodes.

server1 `/mnt/raid5`: 367653478400 available bytes; 98.31% used; 337543742 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23100686336 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23100686336 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23100686336 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23100686336 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 316712300544 available bytes; 97.81% used; 445069002 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84395073536 available bytes; 95.29% used; 114152605 free inodes.

server3 `/home`: 84395073536 available bytes; 95.29% used; 114152605 free inodes.

server3 `/data`: 132802772992 available bytes; 98.16% used; 225811882 free inodes.

server3 `/tmp`: 84395073536 available bytes; 95.29% used; 114152605 free inodes.

server3 `/var/tmp`: 84395073536 available bytes; 95.29% used; 114152605 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105626718208 available bytes; 94.11% used; 114349641 free inodes.

server4 `/home`: 105626718208 available bytes; 94.11% used; 114349641 free inodes.

server4 `/data`: 229949607936 available bytes; 96.82% used; 224933253 free inodes.

server4 `/tmp`: 105626718208 available bytes; 94.11% used; 114349641 free inodes.

server4 `/var/tmp`: 105626718208 available bytes; 94.11% used; 114349641 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
