# V2R cluster inventory

2026-09-25T06:19:17.871944+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318880567296 available bytes; 82.21% used; 112480349 free inodes.

server1 `/home`: 318880567296 available bytes; 82.21% used; 112480349 free inodes.

server1 `/tmp`: 318880567296 available bytes; 82.21% used; 112480349 free inodes.

server1 `/var/tmp`: 318880567296 available bytes; 82.21% used; 112480349 free inodes.

server1 `/mnt/raid5`: 401463218176 available bytes; 98.16% used; 337562338 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22892756992 available bytes; 98.72% used; 110410516 free inodes.

server2 `/home`: 22892756992 available bytes; 98.72% used; 110410516 free inodes.

server2 `/tmp`: 22892756992 available bytes; 98.72% used; 110410516 free inodes.

server2 `/var/tmp`: 22892756992 available bytes; 98.72% used; 110410516 free inodes.

server2 `/mnt/raid5`: 372932030464 available bytes; 97.42% used; 445099942 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84315996160 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84315996160 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142536716288 available bytes; 98.03% used; 225813990 free inodes.

server3 `/tmp`: 84315996160 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84315996160 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105648562176 available bytes; 94.10% used; 114350390 free inodes.

server4 `/home`: 105648562176 available bytes; 94.10% used; 114350390 free inodes.

server4 `/data`: 254611361792 available bytes; 96.48% used; 225022593 free inodes.

server4 `/tmp`: 105648562176 available bytes; 94.10% used; 114350390 free inodes.

server4 `/var/tmp`: 105648562176 available bytes; 94.10% used; 114350390 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
