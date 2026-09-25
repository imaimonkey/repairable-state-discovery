# V2R cluster inventory

2026-09-25T14:07:57.933424+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319151841280 available bytes; 82.20% used; 112476971 free inodes.

server1 `/home`: 319151841280 available bytes; 82.20% used; 112476971 free inodes.

server1 `/tmp`: 319151841280 available bytes; 82.20% used; 112476971 free inodes.

server1 `/var/tmp`: 319151841280 available bytes; 82.20% used; 112476971 free inodes.

server1 `/mnt/raid5`: 369482461184 available bytes; 98.31% used; 337547528 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4731924480 available bytes; 99.74% used; 110407468 free inodes.

server2 `/home`: 4731924480 available bytes; 99.74% used; 110407468 free inodes.

server2 `/tmp`: 4731924480 available bytes; 99.74% used; 110407468 free inodes.

server2 `/var/tmp`: 4731924480 available bytes; 99.74% used; 110407468 free inodes.

server2 `/mnt/raid5`: 322068230144 available bytes; 97.77% used; 445076197 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84281102336 available bytes; 95.30% used; 114154464 free inodes.

server3 `/home`: 84281102336 available bytes; 95.30% used; 114154464 free inodes.

server3 `/data`: 142222102528 available bytes; 98.03% used; 225809064 free inodes.

server3 `/tmp`: 84281102336 available bytes; 95.30% used; 114154464 free inodes.

server3 `/var/tmp`: 84281102336 available bytes; 95.30% used; 114154464 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654951936 available bytes; 94.10% used; 114349708 free inodes.

server4 `/home`: 105654951936 available bytes; 94.10% used; 114349708 free inodes.

server4 `/data`: 231457832960 available bytes; 96.80% used; 224947787 free inodes.

server4 `/tmp`: 105654951936 available bytes; 94.10% used; 114349708 free inodes.

server4 `/var/tmp`: 105654951936 available bytes; 94.10% used; 114349708 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
