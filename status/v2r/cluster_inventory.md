# V2R cluster inventory

2026-09-24T04:16:47.622743+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324708896768 available bytes; 81.89% used; 112493363 free inodes.

server1 `/home`: 324708896768 available bytes; 81.89% used; 112493363 free inodes.

server1 `/tmp`: 324708896768 available bytes; 81.89% used; 112493363 free inodes.

server1 `/var/tmp`: 324708896768 available bytes; 81.89% used; 112493363 free inodes.

server1 `/mnt/raid5`: 431144267776 available bytes; 98.02% used; 337724739 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40796745728 available bytes; 97.72% used; 110430748 free inodes.

server2 `/home`: 40796745728 available bytes; 97.72% used; 110430748 free inodes.

server2 `/tmp`: 40796745728 available bytes; 97.72% used; 110430748 free inodes.

server2 `/var/tmp`: 40796745728 available bytes; 97.72% used; 110430748 free inodes.

server2 `/mnt/raid5`: 525781094400 available bytes; 96.37% used; 445196274 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292422479872 available bytes; 83.68% used; 114200761 free inodes.

server3 `/home`: 292422479872 available bytes; 83.68% used; 114200761 free inodes.

server3 `/data`: 31714344960 available bytes; 99.56% used; 225841733 free inodes.

server3 `/tmp`: 292422479872 available bytes; 83.68% used; 114200761 free inodes.

server3 `/var/tmp`: 292422479872 available bytes; 83.68% used; 114200761 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105790435328 available bytes; 94.10% used; 114349453 free inodes.

server4 `/home`: 105790435328 available bytes; 94.10% used; 114349453 free inodes.

server4 `/data`: 256707485696 available bytes; 96.45% used; 225381796 free inodes.

server4 `/tmp`: 105790435328 available bytes; 94.10% used; 114349453 free inodes.

server4 `/var/tmp`: 105790435328 available bytes; 94.10% used; 114349453 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
