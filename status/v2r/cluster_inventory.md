# V2R cluster inventory

2026-09-25T03:29:54.709550+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318939877376 available bytes; 82.21% used; 112480369 free inodes.

server1 `/home`: 318939877376 available bytes; 82.21% used; 112480369 free inodes.

server1 `/tmp`: 318939877376 available bytes; 82.21% used; 112480369 free inodes.

server1 `/var/tmp`: 318939877376 available bytes; 82.21% used; 112480369 free inodes.

server1 `/mnt/raid5`: 416084832256 available bytes; 98.09% used; 337598948 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22980423680 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 22980423680 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 22980423680 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 22980423680 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 464927285248 available bytes; 96.79% used; 445112032 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84342824960 available bytes; 95.29% used; 114156069 free inodes.

server3 `/home`: 84342824960 available bytes; 95.29% used; 114156069 free inodes.

server3 `/data`: 144525418496 available bytes; 98.00% used; 225809900 free inodes.

server3 `/tmp`: 84342824960 available bytes; 95.29% used; 114156069 free inodes.

server3 `/var/tmp`: 84342824960 available bytes; 95.29% used; 114156069 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105692295168 available bytes; 94.10% used; 114350898 free inodes.

server4 `/home`: 105692295168 available bytes; 94.10% used; 114350898 free inodes.

server4 `/data`: 45396873216 available bytes; 99.37% used; 224966458 free inodes.

server4 `/tmp`: 105692295168 available bytes; 94.10% used; 114350898 free inodes.

server4 `/var/tmp`: 105692295168 available bytes; 94.10% used; 114350898 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
