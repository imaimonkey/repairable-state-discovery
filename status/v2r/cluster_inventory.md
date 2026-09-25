# V2R cluster inventory

2026-09-25T10:40:00.013592+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318990716928 available bytes; 82.20% used; 112479395 free inodes.

server1 `/home`: 318990716928 available bytes; 82.20% used; 112479395 free inodes.

server1 `/tmp`: 318990716928 available bytes; 82.20% used; 112479395 free inodes.

server1 `/var/tmp`: 318990716928 available bytes; 82.20% used; 112479395 free inodes.

server1 `/mnt/raid5`: 364835012608 available bytes; 98.33% used; 337555275 free inodes.
| server2 | True | ['0', '2', '3', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22825951232 available bytes; 98.73% used; 110410498 free inodes.

server2 `/home`: 22825951232 available bytes; 98.73% used; 110410498 free inodes.

server2 `/tmp`: 22825951232 available bytes; 98.73% used; 110410498 free inodes.

server2 `/var/tmp`: 22825951232 available bytes; 98.73% used; 110410498 free inodes.

server2 `/mnt/raid5`: 315929145344 available bytes; 97.82% used; 445089784 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84418187264 available bytes; 95.29% used; 114156033 free inodes.

server3 `/home`: 84418187264 available bytes; 95.29% used; 114156033 free inodes.

server3 `/data`: 142007496704 available bytes; 98.04% used; 225815576 free inodes.

server3 `/tmp`: 84418187264 available bytes; 95.29% used; 114156033 free inodes.

server3 `/var/tmp`: 84418187264 available bytes; 95.29% used; 114156033 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105613053952 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105613053952 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238510473216 available bytes; 96.70% used; 224986169 free inodes.

server4 `/tmp`: 105613053952 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105613053952 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
