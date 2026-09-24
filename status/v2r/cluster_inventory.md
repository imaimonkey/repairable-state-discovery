# V2R cluster inventory

2026-09-24T22:36:09.178317+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323947511808 available bytes; 81.93% used; 112481409 free inodes.

server1 `/home`: 323947511808 available bytes; 81.93% used; 112481409 free inodes.

server1 `/tmp`: 323947511808 available bytes; 81.93% used; 112481409 free inodes.

server1 `/var/tmp`: 323947511808 available bytes; 81.93% used; 112481409 free inodes.

server1 `/mnt/raid5`: 415362666496 available bytes; 98.09% used; 337619627 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23187841024 available bytes; 98.71% used; 110410914 free inodes.

server2 `/home`: 23187841024 available bytes; 98.71% used; 110410914 free inodes.

server2 `/tmp`: 23187841024 available bytes; 98.71% used; 110410914 free inodes.

server2 `/var/tmp`: 23187841024 available bytes; 98.71% used; 110410914 free inodes.

server2 `/mnt/raid5`: 488340434944 available bytes; 96.63% used; 445152718 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84379930624 available bytes; 95.29% used; 114156069 free inodes.

server3 `/home`: 84379930624 available bytes; 95.29% used; 114156069 free inodes.

server3 `/data`: 149196353536 available bytes; 97.94% used; 225801968 free inodes.

server3 `/tmp`: 84379930624 available bytes; 95.29% used; 114156069 free inodes.

server3 `/var/tmp`: 84379930624 available bytes; 95.29% used; 114156069 free inodes.
| server4 | True | ['0', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105801752576 available bytes; 94.10% used; 114348327 free inodes.

server4 `/home`: 105801752576 available bytes; 94.10% used; 114348327 free inodes.

server4 `/data`: 73221402624 available bytes; 98.99% used; 225221299 free inodes.

server4 `/tmp`: 105801752576 available bytes; 94.10% used; 114348327 free inodes.

server4 `/var/tmp`: 105801752576 available bytes; 94.10% used; 114348327 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
