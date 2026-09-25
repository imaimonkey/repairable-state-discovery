# V2R cluster inventory

2026-09-25T10:53:44.772433+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319063351296 available bytes; 82.20% used; 112478880 free inodes.

server1 `/home`: 319063351296 available bytes; 82.20% used; 112478880 free inodes.

server1 `/tmp`: 319063351296 available bytes; 82.20% used; 112478880 free inodes.

server1 `/var/tmp`: 319063351296 available bytes; 82.20% used; 112478880 free inodes.

server1 `/mnt/raid5`: 364804800512 available bytes; 98.33% used; 337555219 free inodes.
| server2 | True | ['1', '2', '3', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22912819200 available bytes; 98.72% used; 110409990 free inodes.

server2 `/home`: 22912819200 available bytes; 98.72% used; 110409990 free inodes.

server2 `/tmp`: 22912819200 available bytes; 98.72% used; 110409990 free inodes.

server2 `/var/tmp`: 22912819200 available bytes; 98.72% used; 110409990 free inodes.

server2 `/mnt/raid5`: 328230748160 available bytes; 97.73% used; 445089485 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84420087808 available bytes; 95.29% used; 114156041 free inodes.

server3 `/home`: 84420087808 available bytes; 95.29% used; 114156041 free inodes.

server3 `/data`: 142005727232 available bytes; 98.04% used; 225815336 free inodes.

server3 `/tmp`: 84420087808 available bytes; 95.29% used; 114156041 free inodes.

server3 `/var/tmp`: 84420087808 available bytes; 95.29% used; 114156041 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105612668928 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105612668928 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238495444992 available bytes; 96.70% used; 224985056 free inodes.

server4 `/tmp`: 105612668928 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105612668928 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
