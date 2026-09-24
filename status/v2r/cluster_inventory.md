# V2R cluster inventory

2026-09-24T06:50:37.575202+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324483362816 available bytes; 81.90% used; 112491460 free inodes.

server1 `/home`: 324483362816 available bytes; 81.90% used; 112491460 free inodes.

server1 `/tmp`: 324483362816 available bytes; 81.90% used; 112491460 free inodes.

server1 `/var/tmp`: 324483362816 available bytes; 81.90% used; 112491460 free inodes.

server1 `/mnt/raid5`: 517427503104 available bytes; 97.63% used; 337722863 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57872031744 available bytes; 96.77% used; 110431193 free inodes.

server2 `/home`: 57872031744 available bytes; 96.77% used; 110431193 free inodes.

server2 `/tmp`: 57872031744 available bytes; 96.77% used; 110431193 free inodes.

server2 `/var/tmp`: 57872031744 available bytes; 96.77% used; 110431193 free inodes.

server2 `/mnt/raid5`: 519080734720 available bytes; 96.41% used; 445191293 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126774722560 available bytes; 92.93% used; 114175142 free inodes.

server3 `/home`: 126774722560 available bytes; 92.93% used; 114175142 free inodes.

server3 `/data`: 139292020736 available bytes; 98.07% used; 225834945 free inodes.

server3 `/tmp`: 126774722560 available bytes; 92.93% used; 114175142 free inodes.

server3 `/var/tmp`: 126774722560 available bytes; 92.93% used; 114175142 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105804419072 available bytes; 94.10% used; 114349238 free inodes.

server4 `/home`: 105804419072 available bytes; 94.10% used; 114349238 free inodes.

server4 `/data`: 310481612800 available bytes; 95.71% used; 225368264 free inodes.

server4 `/tmp`: 105804419072 available bytes; 94.10% used; 114349238 free inodes.

server4 `/var/tmp`: 105804419072 available bytes; 94.10% used; 114349238 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
