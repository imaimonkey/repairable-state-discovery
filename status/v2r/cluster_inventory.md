# V2R cluster inventory

2026-09-24T10:53:07.213963+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324383526912 available bytes; 81.90% used; 112489087 free inodes.

server1 `/home`: 324383526912 available bytes; 81.90% used; 112489087 free inodes.

server1 `/tmp`: 324383526912 available bytes; 81.90% used; 112489087 free inodes.

server1 `/var/tmp`: 324383526912 available bytes; 81.90% used; 112489087 free inodes.

server1 `/mnt/raid5`: 499390799872 available bytes; 97.71% used; 337695074 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57703501824 available bytes; 96.78% used; 110430373 free inodes.

server2 `/home`: 57703501824 available bytes; 96.78% used; 110430373 free inodes.

server2 `/tmp`: 57703501824 available bytes; 96.78% used; 110430373 free inodes.

server2 `/var/tmp`: 57703501824 available bytes; 96.78% used; 110430373 free inodes.

server2 `/mnt/raid5`: 512100450304 available bytes; 96.46% used; 445174991 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85773901824 available bytes; 95.21% used; 114196327 free inodes.

server3 `/home`: 85773901824 available bytes; 95.21% used; 114196327 free inodes.

server3 `/data`: 164077215744 available bytes; 97.73% used; 225817768 free inodes.

server3 `/tmp`: 85773901824 available bytes; 95.21% used; 114196327 free inodes.

server3 `/var/tmp`: 85773901824 available bytes; 95.21% used; 114196327 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105735094272 available bytes; 94.10% used; 114348939 free inodes.

server4 `/home`: 105735094272 available bytes; 94.10% used; 114348939 free inodes.

server4 `/data`: 132786614272 available bytes; 98.16% used; 225258301 free inodes.

server4 `/tmp`: 105735094272 available bytes; 94.10% used; 114348939 free inodes.

server4 `/var/tmp`: 105735094272 available bytes; 94.10% used; 114348939 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
