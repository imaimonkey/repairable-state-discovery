# V2R cluster inventory

2026-09-24T20:43:30.941648+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323980521472 available bytes; 81.93% used; 112481433 free inodes.

server1 `/home`: 323980521472 available bytes; 81.93% used; 112481433 free inodes.

server1 `/tmp`: 323980521472 available bytes; 81.93% used; 112481433 free inodes.

server1 `/var/tmp`: 323980521472 available bytes; 81.93% used; 112481433 free inodes.

server1 `/mnt/raid5`: 415601070080 available bytes; 98.09% used; 337632890 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30151741440 available bytes; 98.32% used; 110411380 free inodes.

server2 `/home`: 30151741440 available bytes; 98.32% used; 110411380 free inodes.

server2 `/tmp`: 30151741440 available bytes; 98.32% used; 110411380 free inodes.

server2 `/var/tmp`: 30151741440 available bytes; 98.32% used; 110411380 free inodes.

server2 `/mnt/raid5`: 491849940992 available bytes; 96.60% used; 445156523 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84395220992 available bytes; 95.29% used; 114156102 free inodes.

server3 `/home`: 84395220992 available bytes; 95.29% used; 114156102 free inodes.

server3 `/data`: 151233638400 available bytes; 97.91% used; 225804103 free inodes.

server3 `/tmp`: 84395220992 available bytes; 95.29% used; 114156102 free inodes.

server3 `/var/tmp`: 84395220992 available bytes; 95.29% used; 114156102 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639755776 available bytes; 94.10% used; 114348378 free inodes.

server4 `/home`: 105639755776 available bytes; 94.10% used; 114348378 free inodes.

server4 `/data`: 82707906560 available bytes; 98.86% used; 225256664 free inodes.

server4 `/tmp`: 105639755776 available bytes; 94.10% used; 114348378 free inodes.

server4 `/var/tmp`: 105639755776 available bytes; 94.10% used; 114348378 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
