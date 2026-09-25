# V2R cluster inventory

2026-09-25T06:41:00.319040+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318873600000 available bytes; 82.21% used; 112480357 free inodes.

server1 `/home`: 318873600000 available bytes; 82.21% used; 112480357 free inodes.

server1 `/tmp`: 318873600000 available bytes; 82.21% used; 112480357 free inodes.

server1 `/var/tmp`: 318873600000 available bytes; 82.21% used; 112480357 free inodes.

server1 `/mnt/raid5`: 399790272512 available bytes; 98.17% used; 337561375 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22886088704 available bytes; 98.72% used; 110410542 free inodes.

server2 `/home`: 22886088704 available bytes; 98.72% used; 110410542 free inodes.

server2 `/tmp`: 22886088704 available bytes; 98.72% used; 110410542 free inodes.

server2 `/var/tmp`: 22886088704 available bytes; 98.72% used; 110410542 free inodes.

server2 `/mnt/raid5`: 357306843136 available bytes; 97.53% used; 445099058 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84449947648 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84449947648 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142531268608 available bytes; 98.03% used; 225813584 free inodes.

server3 `/tmp`: 84449947648 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84449947648 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639448576 available bytes; 94.10% used; 114350384 free inodes.

server4 `/home`: 105639448576 available bytes; 94.10% used; 114350384 free inodes.

server4 `/data`: 251128606720 available bytes; 96.53% used; 225018975 free inodes.

server4 `/tmp`: 105639448576 available bytes; 94.10% used; 114350384 free inodes.

server4 `/var/tmp`: 105639448576 available bytes; 94.10% used; 114350384 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
