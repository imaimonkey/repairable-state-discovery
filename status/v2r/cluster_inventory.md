# V2R cluster inventory

2026-09-24T07:23:21.274288+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324447731712 available bytes; 81.90% used; 112491200 free inodes.

server1 `/home`: 324447731712 available bytes; 81.90% used; 112491200 free inodes.

server1 `/tmp`: 324447731712 available bytes; 81.90% used; 112491200 free inodes.

server1 `/var/tmp`: 324447731712 available bytes; 81.90% used; 112491200 free inodes.

server1 `/mnt/raid5`: 517415464960 available bytes; 97.63% used; 337722818 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57851883520 available bytes; 96.77% used; 110431119 free inodes.

server2 `/home`: 57851883520 available bytes; 96.77% used; 110431119 free inodes.

server2 `/tmp`: 57851883520 available bytes; 96.77% used; 110431119 free inodes.

server2 `/var/tmp`: 57851883520 available bytes; 96.77% used; 110431119 free inodes.

server2 `/mnt/raid5`: 518477283328 available bytes; 96.42% used; 445181003 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126793293824 available bytes; 92.92% used; 114182837 free inodes.

server3 `/home`: 126793293824 available bytes; 92.92% used; 114182837 free inodes.

server3 `/data`: 139039170560 available bytes; 98.08% used; 225834262 free inodes.

server3 `/tmp`: 126793293824 available bytes; 92.92% used; 114182837 free inodes.

server3 `/var/tmp`: 126793293824 available bytes; 92.92% used; 114182837 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780985856 available bytes; 94.10% used; 114349193 free inodes.

server4 `/home`: 105780985856 available bytes; 94.10% used; 114349193 free inodes.

server4 `/data`: 287614324736 available bytes; 96.03% used; 225366941 free inodes.

server4 `/tmp`: 105780985856 available bytes; 94.10% used; 114349193 free inodes.

server4 `/var/tmp`: 105780985856 available bytes; 94.10% used; 114349193 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
