# V2R cluster inventory

2026-09-25T07:52:06.098078+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318861365248 available bytes; 82.21% used; 112480371 free inodes.

server1 `/home`: 318861365248 available bytes; 82.21% used; 112480371 free inodes.

server1 `/tmp`: 318861365248 available bytes; 82.21% used; 112480371 free inodes.

server1 `/var/tmp`: 318861365248 available bytes; 82.21% used; 112480371 free inodes.

server1 `/mnt/raid5`: 394388275200 available bytes; 98.19% used; 337558110 free inodes.
| server2 | True | ['0'] | [] |

server2 `/`: 22848225280 available bytes; 98.73% used; 110410481 free inodes.

server2 `/home`: 22848225280 available bytes; 98.73% used; 110410481 free inodes.

server2 `/tmp`: 22848225280 available bytes; 98.73% used; 110410481 free inodes.

server2 `/var/tmp`: 22848225280 available bytes; 98.73% used; 110410481 free inodes.

server2 `/mnt/raid5`: 334446784512 available bytes; 97.69% used; 445095543 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84438396928 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84438396928 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142390902784 available bytes; 98.03% used; 225812354 free inodes.

server3 `/tmp`: 84438396928 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84438396928 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637208064 available bytes; 94.11% used; 114350351 free inodes.

server4 `/home`: 105637208064 available bytes; 94.11% used; 114350351 free inodes.

server4 `/data`: 249042575360 available bytes; 96.56% used; 225011046 free inodes.

server4 `/tmp`: 105637208064 available bytes; 94.11% used; 114350351 free inodes.

server4 `/var/tmp`: 105637208064 available bytes; 94.11% used; 114350351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
