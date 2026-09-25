# V2R cluster inventory

2026-09-25T23:50:04.994762+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318672134144 available bytes; 82.22% used; 112476305 free inodes.

server1 `/home`: 318672134144 available bytes; 82.22% used; 112476305 free inodes.

server1 `/tmp`: 318672134144 available bytes; 82.22% used; 112476305 free inodes.

server1 `/var/tmp`: 318672134144 available bytes; 82.22% used; 112476305 free inodes.

server1 `/mnt/raid5`: 360068218880 available bytes; 98.35% used; 337538557 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22951604224 available bytes; 98.72% used; 110406242 free inodes.

server2 `/home`: 22951604224 available bytes; 98.72% used; 110406242 free inodes.

server2 `/tmp`: 22951604224 available bytes; 98.72% used; 110406242 free inodes.

server2 `/var/tmp`: 22951604224 available bytes; 98.72% used; 110406242 free inodes.

server2 `/mnt/raid5`: 296446484480 available bytes; 97.95% used; 445050410 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84350050304 available bytes; 95.29% used; 114152442 free inodes.

server3 `/home`: 84350050304 available bytes; 95.29% used; 114152442 free inodes.

server3 `/data`: 124799619072 available bytes; 98.28% used; 225811118 free inodes.

server3 `/tmp`: 84350050304 available bytes; 95.29% used; 114152442 free inodes.

server3 `/var/tmp`: 84350050304 available bytes; 95.29% used; 114152442 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105082519552 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082519552 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178218254336 available bytes; 97.54% used; 224917594 free inodes.

server4 `/tmp`: 105082519552 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082519552 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
