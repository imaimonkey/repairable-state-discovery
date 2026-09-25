# V2R cluster inventory

2026-09-25T11:07:29.617827+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319063171072 available bytes; 82.20% used; 112478863 free inodes.

server1 `/home`: 319063171072 available bytes; 82.20% used; 112478863 free inodes.

server1 `/tmp`: 319063171072 available bytes; 82.20% used; 112478863 free inodes.

server1 `/var/tmp`: 319063171072 available bytes; 82.20% used; 112478863 free inodes.

server1 `/mnt/raid5`: 364806803456 available bytes; 98.33% used; 337555117 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22906699776 available bytes; 98.72% used; 110409994 free inodes.

server2 `/home`: 22906699776 available bytes; 98.72% used; 110409994 free inodes.

server2 `/tmp`: 22906699776 available bytes; 98.72% used; 110409994 free inodes.

server2 `/var/tmp`: 22906699776 available bytes; 98.72% used; 110409994 free inodes.

server2 `/mnt/raid5`: 328871706624 available bytes; 97.73% used; 445088676 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84139671552 available bytes; 95.30% used; 114155495 free inodes.

server3 `/home`: 84139671552 available bytes; 95.30% used; 114155495 free inodes.

server3 `/data`: 142003572736 available bytes; 98.04% used; 225815079 free inodes.

server3 `/tmp`: 84139671552 available bytes; 95.30% used; 114155495 free inodes.

server3 `/var/tmp`: 84139671552 available bytes; 95.30% used; 114155495 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105612263424 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105612263424 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238644543488 available bytes; 96.70% used; 224982887 free inodes.

server4 `/tmp`: 105612263424 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105612263424 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
