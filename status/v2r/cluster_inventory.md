# V2R cluster inventory

2026-09-25T01:09:59.722894+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319077429248 available bytes; 82.20% used; 112480767 free inodes.

server1 `/home`: 319077429248 available bytes; 82.20% used; 112480767 free inodes.

server1 `/tmp`: 319077429248 available bytes; 82.20% used; 112480767 free inodes.

server1 `/var/tmp`: 319077429248 available bytes; 82.20% used; 112480767 free inodes.

server1 `/mnt/raid5`: 416527208448 available bytes; 98.09% used; 337615298 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 23059513344 available bytes; 98.71% used; 110410766 free inodes.

server2 `/home`: 23059513344 available bytes; 98.71% used; 110410766 free inodes.

server2 `/tmp`: 23059513344 available bytes; 98.71% used; 110410766 free inodes.

server2 `/var/tmp`: 23059513344 available bytes; 98.71% used; 110410766 free inodes.

server2 `/mnt/raid5`: 498190934016 available bytes; 96.56% used; 445162249 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84352946176 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84352946176 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 148216647680 available bytes; 97.95% used; 225812699 free inodes.

server3 `/tmp`: 84352946176 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84352946176 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779490816 available bytes; 94.10% used; 114348300 free inodes.

server4 `/home`: 105779490816 available bytes; 94.10% used; 114348300 free inodes.

server4 `/data`: 53341839360 available bytes; 99.26% used; 225030808 free inodes.

server4 `/tmp`: 105779490816 available bytes; 94.10% used; 114348300 free inodes.

server4 `/var/tmp`: 105779490816 available bytes; 94.10% used; 114348300 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
