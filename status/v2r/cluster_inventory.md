# V2R cluster inventory

2026-09-24T04:50:06.262877+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324622278656 available bytes; 81.89% used; 112492809 free inodes.

server1 `/home`: 324622278656 available bytes; 81.89% used; 112492809 free inodes.

server1 `/tmp`: 324622278656 available bytes; 81.89% used; 112492809 free inodes.

server1 `/var/tmp`: 324622278656 available bytes; 81.89% used; 112492809 free inodes.

server1 `/mnt/raid5`: 469827891200 available bytes; 97.84% used; 337724582 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40768344064 available bytes; 97.73% used; 110430456 free inodes.

server2 `/home`: 40768344064 available bytes; 97.73% used; 110430456 free inodes.

server2 `/tmp`: 40768344064 available bytes; 97.73% used; 110430456 free inodes.

server2 `/var/tmp`: 40768344064 available bytes; 97.73% used; 110430456 free inodes.

server2 `/mnt/raid5`: 523891159040 available bytes; 96.38% used; 445195145 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292364652544 available bytes; 83.68% used; 114199658 free inodes.

server3 `/home`: 292364652544 available bytes; 83.68% used; 114199658 free inodes.

server3 `/data`: 24356929536 available bytes; 99.66% used; 225840603 free inodes.

server3 `/tmp`: 292364652544 available bytes; 83.68% used; 114199658 free inodes.

server3 `/var/tmp`: 292364652544 available bytes; 83.68% used; 114199658 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105835999232 available bytes; 94.09% used; 114349397 free inodes.

server4 `/home`: 105835999232 available bytes; 94.09% used; 114349397 free inodes.

server4 `/data`: 253373603840 available bytes; 96.50% used; 225366843 free inodes.

server4 `/tmp`: 105835999232 available bytes; 94.09% used; 114349397 free inodes.

server4 `/var/tmp`: 105835999232 available bytes; 94.09% used; 114349397 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
