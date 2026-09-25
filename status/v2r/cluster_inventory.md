# V2R cluster inventory

2026-09-25T06:16:48.038705+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318881124352 available bytes; 82.21% used; 112480346 free inodes.

server1 `/home`: 318881124352 available bytes; 82.21% used; 112480346 free inodes.

server1 `/tmp`: 318881124352 available bytes; 82.21% used; 112480346 free inodes.

server1 `/var/tmp`: 318881124352 available bytes; 82.21% used; 112480346 free inodes.

server1 `/mnt/raid5`: 401469841408 available bytes; 98.16% used; 337562629 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22891569152 available bytes; 98.72% used; 110410530 free inodes.

server2 `/home`: 22891569152 available bytes; 98.72% used; 110410530 free inodes.

server2 `/tmp`: 22891569152 available bytes; 98.72% used; 110410530 free inodes.

server2 `/var/tmp`: 22891569152 available bytes; 98.72% used; 110410530 free inodes.

server2 `/mnt/raid5`: 373011722240 available bytes; 97.42% used; 445100065 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84316643328 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84316643328 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142535901184 available bytes; 98.03% used; 225814020 free inodes.

server3 `/tmp`: 84316643328 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84316643328 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648627712 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105648627712 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 254635548672 available bytes; 96.48% used; 225023279 free inodes.

server4 `/tmp`: 105648627712 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105648627712 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
