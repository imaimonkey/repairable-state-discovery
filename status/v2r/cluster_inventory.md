# V2R cluster inventory

2026-09-24T06:52:10.618619+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324486901760 available bytes; 81.90% used; 112491449 free inodes.

server1 `/home`: 324486901760 available bytes; 81.90% used; 112491449 free inodes.

server1 `/tmp`: 324486901760 available bytes; 81.90% used; 112491449 free inodes.

server1 `/var/tmp`: 324486901760 available bytes; 81.90% used; 112491449 free inodes.

server1 `/mnt/raid5`: 517424824320 available bytes; 97.63% used; 337722846 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57871536128 available bytes; 96.77% used; 110431187 free inodes.

server2 `/home`: 57871536128 available bytes; 96.77% used; 110431187 free inodes.

server2 `/tmp`: 57871536128 available bytes; 96.77% used; 110431187 free inodes.

server2 `/var/tmp`: 57871536128 available bytes; 96.77% used; 110431187 free inodes.

server2 `/mnt/raid5`: 519027847168 available bytes; 96.41% used; 445191164 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126774308864 available bytes; 92.93% used; 114175142 free inodes.

server3 `/home`: 126774308864 available bytes; 92.93% used; 114175142 free inodes.

server3 `/data`: 139276161024 available bytes; 98.08% used; 225834912 free inodes.

server3 `/tmp`: 126774308864 available bytes; 92.93% used; 114175142 free inodes.

server3 `/var/tmp`: 126774308864 available bytes; 92.93% used; 114175142 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105804288000 available bytes; 94.10% used; 114349237 free inodes.

server4 `/home`: 105804288000 available bytes; 94.10% used; 114349237 free inodes.

server4 `/data`: 309383213056 available bytes; 95.72% used; 225368206 free inodes.

server4 `/tmp`: 105804288000 available bytes; 94.10% used; 114349237 free inodes.

server4 `/var/tmp`: 105804288000 available bytes; 94.10% used; 114349237 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
