# V2R cluster inventory

2026-09-24T01:24:35.893874+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325466472448 available bytes; 81.84% used; 112499746 free inodes.

server1 `/home`: 325466472448 available bytes; 81.84% used; 112499746 free inodes.

server1 `/tmp`: 325466472448 available bytes; 81.84% used; 112499746 free inodes.

server1 `/var/tmp`: 325466472448 available bytes; 81.84% used; 112499746 free inodes.

server1 `/mnt/raid5`: 920181805056 available bytes; 95.78% used; 337734034 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40951238656 available bytes; 97.72% used; 110432037 free inodes.

server2 `/home`: 40951238656 available bytes; 97.72% used; 110432037 free inodes.

server2 `/tmp`: 40951238656 available bytes; 97.72% used; 110432037 free inodes.

server2 `/var/tmp`: 40951238656 available bytes; 97.72% used; 110432037 free inodes.

server2 `/mnt/raid5`: 531119779840 available bytes; 96.33% used; 445201698 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292346789888 available bytes; 83.69% used; 114187454 free inodes.

server3 `/home`: 292346789888 available bytes; 83.69% used; 114187454 free inodes.

server3 `/data`: 82050498560 available bytes; 98.87% used; 225842386 free inodes.

server3 `/tmp`: 292346789888 available bytes; 83.69% used; 114187454 free inodes.

server3 `/var/tmp`: 292346789888 available bytes; 83.69% used; 114187454 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105973567488 available bytes; 94.09% used; 114348928 free inodes.

server4 `/home`: 105973567488 available bytes; 94.09% used; 114348928 free inodes.

server4 `/data`: 290823856128 available bytes; 95.98% used; 225396988 free inodes.

server4 `/tmp`: 105973567488 available bytes; 94.09% used; 114348928 free inodes.

server4 `/var/tmp`: 105973567488 available bytes; 94.09% used; 114348928 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
