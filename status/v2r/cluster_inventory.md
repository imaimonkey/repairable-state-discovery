# V2R cluster inventory

2026-09-26T03:08:30.370131+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318417219584 available bytes; 82.24% used; 112476256 free inodes.

server1 `/home`: 318417219584 available bytes; 82.24% used; 112476256 free inodes.

server1 `/tmp`: 318417219584 available bytes; 82.24% used; 112476256 free inodes.

server1 `/var/tmp`: 318417219584 available bytes; 82.24% used; 112476256 free inodes.

server1 `/mnt/raid5`: 331057704960 available bytes; 98.48% used; 337545914 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22940139520 available bytes; 98.72% used; 110406208 free inodes.

server2 `/home`: 22940139520 available bytes; 98.72% used; 110406208 free inodes.

server2 `/tmp`: 22940139520 available bytes; 98.72% used; 110406208 free inodes.

server2 `/var/tmp`: 22940139520 available bytes; 98.72% used; 110406208 free inodes.

server2 `/mnt/raid5`: 287314923520 available bytes; 98.01% used; 445053004 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84307197952 available bytes; 95.30% used; 114152356 free inodes.

server3 `/home`: 84307197952 available bytes; 95.30% used; 114152356 free inodes.

server3 `/data`: 125439987712 available bytes; 98.27% used; 225831035 free inodes.

server3 `/tmp`: 84307197952 available bytes; 95.30% used; 114152356 free inodes.

server3 `/var/tmp`: 84307197952 available bytes; 95.30% used; 114152356 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105884991488 available bytes; 94.09% used; 114347061 free inodes.

server4 `/home`: 105884991488 available bytes; 94.09% used; 114347061 free inodes.

server4 `/data`: 109636268032 available bytes; 98.48% used; 224915172 free inodes.

server4 `/tmp`: 105884991488 available bytes; 94.09% used; 114347061 free inodes.

server4 `/var/tmp`: 105884991488 available bytes; 94.09% used; 114347061 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
