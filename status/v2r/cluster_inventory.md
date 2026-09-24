# V2R cluster inventory

2026-09-24T01:29:13.934661+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325462171648 available bytes; 81.84% used; 112499676 free inodes.

server1 `/home`: 325462171648 available bytes; 81.84% used; 112499676 free inodes.

server1 `/tmp`: 325462171648 available bytes; 81.84% used; 112499676 free inodes.

server1 `/var/tmp`: 325462171648 available bytes; 81.84% used; 112499676 free inodes.

server1 `/mnt/raid5`: 901503610880 available bytes; 95.86% used; 337733974 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40949497856 available bytes; 97.72% used; 110432003 free inodes.

server2 `/home`: 40949497856 available bytes; 97.72% used; 110432003 free inodes.

server2 `/tmp`: 40949497856 available bytes; 97.72% used; 110432003 free inodes.

server2 `/var/tmp`: 40949497856 available bytes; 97.72% used; 110432003 free inodes.

server2 `/mnt/raid5`: 530986528768 available bytes; 96.33% used; 445201630 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292699897856 available bytes; 83.67% used; 114210371 free inodes.

server3 `/home`: 292699897856 available bytes; 83.67% used; 114210371 free inodes.

server3 `/data`: 82043179008 available bytes; 98.87% used; 225842285 free inodes.

server3 `/tmp`: 292699897856 available bytes; 83.67% used; 114210371 free inodes.

server3 `/var/tmp`: 292699897856 available bytes; 83.67% used; 114210371 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105968394240 available bytes; 94.09% used; 114348848 free inodes.

server4 `/home`: 105968394240 available bytes; 94.09% used; 114348848 free inodes.

server4 `/data`: 290807644160 available bytes; 95.98% used; 225396961 free inodes.

server4 `/tmp`: 105968394240 available bytes; 94.09% used; 114348848 free inodes.

server4 `/var/tmp`: 105968394240 available bytes; 94.09% used; 114348848 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
