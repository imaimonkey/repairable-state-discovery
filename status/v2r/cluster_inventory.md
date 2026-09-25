# V2R cluster inventory

2026-09-25T07:57:38.546028+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318861381632 available bytes; 82.21% used; 112480375 free inodes.

server1 `/home`: 318861381632 available bytes; 82.21% used; 112480375 free inodes.

server1 `/tmp`: 318861381632 available bytes; 82.21% used; 112480375 free inodes.

server1 `/var/tmp`: 318861381632 available bytes; 82.21% used; 112480375 free inodes.

server1 `/mnt/raid5`: 386629705728 available bytes; 98.23% used; 337557942 free inodes.
| server2 | True | ['0'] | [] | reference_compatible=False |

server2 `/`: 22844198912 available bytes; 98.73% used; 110410485 free inodes.

server2 `/home`: 22844198912 available bytes; 98.73% used; 110410485 free inodes.

server2 `/tmp`: 22844198912 available bytes; 98.73% used; 110410485 free inodes.

server2 `/var/tmp`: 22844198912 available bytes; 98.73% used; 110410485 free inodes.

server2 `/mnt/raid5`: 333766524928 available bytes; 97.69% used; 445095601 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84440621056 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84440621056 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142388305920 available bytes; 98.03% used; 225812240 free inodes.

server3 `/tmp`: 84440621056 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84440621056 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105625624576 available bytes; 94.11% used; 114350336 free inodes.

server4 `/home`: 105625624576 available bytes; 94.11% used; 114350336 free inodes.

server4 `/data`: 249042063360 available bytes; 96.56% used; 225010225 free inodes.

server4 `/tmp`: 105625624576 available bytes; 94.11% used; 114350336 free inodes.

server4 `/var/tmp`: 105625624576 available bytes; 94.11% used; 114350336 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
