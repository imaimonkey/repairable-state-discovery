# V2R cluster inventory

2026-09-25T11:05:57.928551+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319063371776 available bytes; 82.20% used; 112478860 free inodes.

server1 `/home`: 319063371776 available bytes; 82.20% used; 112478860 free inodes.

server1 `/tmp`: 319063371776 available bytes; 82.20% used; 112478860 free inodes.

server1 `/var/tmp`: 319063371776 available bytes; 82.20% used; 112478860 free inodes.

server1 `/mnt/raid5`: 369176674304 available bytes; 98.31% used; 337555196 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22906478592 available bytes; 98.72% used; 110409992 free inodes.

server2 `/home`: 22906478592 available bytes; 98.72% used; 110409992 free inodes.

server2 `/tmp`: 22906478592 available bytes; 98.72% used; 110409992 free inodes.

server2 `/var/tmp`: 22906478592 available bytes; 98.72% used; 110409992 free inodes.

server2 `/mnt/raid5`: 328927145984 available bytes; 97.73% used; 445088874 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84139995136 available bytes; 95.30% used; 114155494 free inodes.

server3 `/home`: 84139995136 available bytes; 95.30% used; 114155494 free inodes.

server3 `/data`: 142004719616 available bytes; 98.04% used; 225815096 free inodes.

server3 `/tmp`: 84139995136 available bytes; 95.30% used; 114155494 free inodes.

server3 `/var/tmp`: 84139995136 available bytes; 95.30% used; 114155494 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105612308480 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105612308480 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238649528320 available bytes; 96.70% used; 224983089 free inodes.

server4 `/tmp`: 105612308480 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105612308480 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
