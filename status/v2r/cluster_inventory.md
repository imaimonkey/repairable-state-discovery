# V2R cluster inventory

2026-09-25T10:35:24.784941+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319000084480 available bytes; 82.20% used; 112479392 free inodes.

server1 `/home`: 319000084480 available bytes; 82.20% used; 112479392 free inodes.

server1 `/tmp`: 319000084480 available bytes; 82.20% used; 112479392 free inodes.

server1 `/var/tmp`: 319000084480 available bytes; 82.20% used; 112479392 free inodes.

server1 `/mnt/raid5`: 371202789376 available bytes; 98.30% used; 337555370 free inodes.
| server2 | True | ['0', '3', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22824599552 available bytes; 98.73% used; 110410494 free inodes.

server2 `/home`: 22824599552 available bytes; 98.73% used; 110410494 free inodes.

server2 `/tmp`: 22824599552 available bytes; 98.73% used; 110410494 free inodes.

server2 `/var/tmp`: 22824599552 available bytes; 98.73% used; 110410494 free inodes.

server2 `/mnt/raid5`: 316059680768 available bytes; 97.82% used; 445089792 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84418723840 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84418723840 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142010482688 available bytes; 98.04% used; 225815653 free inodes.

server3 `/tmp`: 84418723840 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84418723840 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105613209600 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105613209600 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238517694464 available bytes; 96.70% used; 224986602 free inodes.

server4 `/tmp`: 105613209600 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105613209600 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
