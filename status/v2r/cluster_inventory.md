# V2R cluster inventory

2026-09-25T08:58:56.832604+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318838718464 available bytes; 82.21% used; 112480389 free inodes.

server1 `/home`: 318838718464 available bytes; 82.21% used; 112480389 free inodes.

server1 `/tmp`: 318838718464 available bytes; 82.21% used; 112480389 free inodes.

server1 `/var/tmp`: 318838718464 available bytes; 82.21% used; 112480389 free inodes.

server1 `/mnt/raid5`: 364197265408 available bytes; 98.33% used; 337556995 free inodes.
| server2 | True | ['5', '6'] | [] | reference_compatible=False |

server2 `/`: 22829830144 available bytes; 98.73% used; 110410492 free inodes.

server2 `/home`: 22829830144 available bytes; 98.73% used; 110410492 free inodes.

server2 `/tmp`: 22829830144 available bytes; 98.73% used; 110410492 free inodes.

server2 `/var/tmp`: 22829830144 available bytes; 98.73% used; 110410492 free inodes.

server2 `/mnt/raid5`: 332617723904 available bytes; 97.70% used; 445093154 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84438540288 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84438540288 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142374993920 available bytes; 98.03% used; 225811186 free inodes.

server3 `/tmp`: 84438540288 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84438540288 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105633120256 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633120256 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 243389440000 available bytes; 96.64% used; 225000020 free inodes.

server4 `/tmp`: 105633120256 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633120256 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
