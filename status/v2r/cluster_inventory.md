# V2R cluster inventory

2026-09-25T07:13:16.345553+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318873145344 available bytes; 82.21% used; 112480373 free inodes.

server1 `/home`: 318873145344 available bytes; 82.21% used; 112480373 free inodes.

server1 `/tmp`: 318873145344 available bytes; 82.21% used; 112480373 free inodes.

server1 `/var/tmp`: 318873145344 available bytes; 82.21% used; 112480373 free inodes.

server1 `/mnt/raid5`: 379056689152 available bytes; 98.26% used; 337558538 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22868901888 available bytes; 98.72% used; 110410502 free inodes.

server2 `/home`: 22868901888 available bytes; 98.72% used; 110410502 free inodes.

server2 `/tmp`: 22868901888 available bytes; 98.72% used; 110410502 free inodes.

server2 `/var/tmp`: 22868901888 available bytes; 98.72% used; 110410502 free inodes.

server2 `/mnt/raid5`: 329917968384 available bytes; 97.72% used; 445098117 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84448407552 available bytes; 95.29% used; 114156033 free inodes.

server3 `/home`: 84448407552 available bytes; 95.29% used; 114156033 free inodes.

server3 `/data`: 142456340480 available bytes; 98.03% used; 225813012 free inodes.

server3 `/tmp`: 84448407552 available bytes; 95.29% used; 114156033 free inodes.

server3 `/var/tmp`: 84448407552 available bytes; 95.29% used; 114156033 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638400000 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638400000 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249488224256 available bytes; 96.55% used; 225016213 free inodes.

server4 `/tmp`: 105638400000 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638400000 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
