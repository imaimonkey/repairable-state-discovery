# V2R cluster inventory

2026-09-25T02:22:16.179772+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318971088896 available bytes; 82.21% used; 112480505 free inodes.

server1 `/home`: 318971088896 available bytes; 82.21% used; 112480505 free inodes.

server1 `/tmp`: 318971088896 available bytes; 82.21% used; 112480505 free inodes.

server1 `/var/tmp`: 318971088896 available bytes; 82.21% used; 112480505 free inodes.

server1 `/mnt/raid5`: 416228528128 available bytes; 98.09% used; 337606851 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23016644608 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 23016644608 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 23016644608 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 23016644608 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 463017226240 available bytes; 96.80% used; 445114118 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84355325952 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84355325952 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145729613824 available bytes; 97.99% used; 225811206 free inodes.

server3 `/tmp`: 84355325952 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84355325952 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105896161280 available bytes; 94.09% used; 114351001 free inodes.

server4 `/home`: 105896161280 available bytes; 94.09% used; 114351001 free inodes.

server4 `/data`: 37810335744 available bytes; 99.48% used; 224970318 free inodes.

server4 `/tmp`: 105896161280 available bytes; 94.09% used; 114351001 free inodes.

server4 `/var/tmp`: 105896161280 available bytes; 94.09% used; 114351001 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
