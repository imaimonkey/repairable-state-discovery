# V2R cluster inventory

2026-09-25T06:20:49.816231+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318881878016 available bytes; 82.21% used; 112480351 free inodes.

server1 `/home`: 318881878016 available bytes; 82.21% used; 112480351 free inodes.

server1 `/tmp`: 318881878016 available bytes; 82.21% used; 112480351 free inodes.

server1 `/var/tmp`: 318881878016 available bytes; 82.21% used; 112480351 free inodes.

server1 `/mnt/raid5`: 401459335168 available bytes; 98.16% used; 337562161 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22892048384 available bytes; 98.72% used; 110410514 free inodes.

server2 `/home`: 22892048384 available bytes; 98.72% used; 110410514 free inodes.

server2 `/tmp`: 22892048384 available bytes; 98.72% used; 110410514 free inodes.

server2 `/var/tmp`: 22892048384 available bytes; 98.72% used; 110410514 free inodes.

server2 `/mnt/raid5`: 372890959872 available bytes; 97.42% used; 445099852 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84315893760 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84315893760 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142534778880 available bytes; 98.03% used; 225813969 free inodes.

server3 `/tmp`: 84315893760 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84315893760 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105648492544 available bytes; 94.10% used; 114350390 free inodes.

server4 `/home`: 105648492544 available bytes; 94.10% used; 114350390 free inodes.

server4 `/data`: 254607966208 available bytes; 96.48% used; 225022331 free inodes.

server4 `/tmp`: 105648492544 available bytes; 94.10% used; 114350390 free inodes.

server4 `/var/tmp`: 105648492544 available bytes; 94.10% used; 114350390 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
