# V2R cluster inventory

2026-09-24T00:09:17.490131+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325573332992 available bytes; 81.84% used; 112500817 free inodes.

server1 `/home`: 325573332992 available bytes; 81.84% used; 112500817 free inodes.

server1 `/tmp`: 325573332992 available bytes; 81.84% used; 112500817 free inodes.

server1 `/var/tmp`: 325573332992 available bytes; 81.84% used; 112500817 free inodes.

server1 `/mnt/raid5`: 1228867383296 available bytes; 94.36% used; 337735377 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41008316416 available bytes; 97.71% used; 110432411 free inodes.

server2 `/home`: 41008316416 available bytes; 97.71% used; 110432411 free inodes.

server2 `/tmp`: 41008316416 available bytes; 97.71% used; 110432411 free inodes.

server2 `/var/tmp`: 41008316416 available bytes; 97.71% used; 110432411 free inodes.

server2 `/mnt/raid5`: 533324111872 available bytes; 96.31% used; 445203938 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292600979456 available bytes; 83.67% used; 114209143 free inodes.

server3 `/home`: 292600979456 available bytes; 83.67% used; 114209143 free inodes.

server3 `/data`: 82263240704 available bytes; 98.86% used; 225844601 free inodes.

server3 `/tmp`: 292600979456 available bytes; 83.67% used; 114209143 free inodes.

server3 `/var/tmp`: 292600979456 available bytes; 83.67% used; 114209143 free inodes.
| server4 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106118647808 available bytes; 94.08% used; 114350955 free inodes.

server4 `/home`: 106118647808 available bytes; 94.08% used; 114350955 free inodes.

server4 `/data`: 292913045504 available bytes; 95.95% used; 225414568 free inodes.

server4 `/tmp`: 106118647808 available bytes; 94.08% used; 114350955 free inodes.

server4 `/var/tmp`: 106118647808 available bytes; 94.08% used; 114350955 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
