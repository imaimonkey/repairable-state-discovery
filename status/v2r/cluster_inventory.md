# V2R cluster inventory

2026-09-26T05:21:17.282834+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318399565824 available bytes; 82.24% used; 112476279 free inodes.

server1 `/home`: 318399565824 available bytes; 82.24% used; 112476279 free inodes.

server1 `/tmp`: 318399565824 available bytes; 82.24% used; 112476279 free inodes.

server1 `/var/tmp`: 318399565824 available bytes; 82.24% used; 112476279 free inodes.

server1 `/mnt/raid5`: 295015993344 available bytes; 98.65% used; 337542607 free inodes.
| server2 | True | ['0'] | [] | reference_compatible=False |

server2 `/`: 22920368128 available bytes; 98.72% used; 110406203 free inodes.

server2 `/home`: 22920368128 available bytes; 98.72% used; 110406203 free inodes.

server2 `/tmp`: 22920368128 available bytes; 98.72% used; 110406203 free inodes.

server2 `/var/tmp`: 22920368128 available bytes; 98.72% used; 110406203 free inodes.

server2 `/mnt/raid5`: 277057507328 available bytes; 98.09% used; 445048947 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84088012800 available bytes; 95.31% used; 114166425 free inodes.

server3 `/home`: 84088012800 available bytes; 95.31% used; 114166425 free inodes.

server3 `/data`: 124360499200 available bytes; 98.28% used; 225824889 free inodes.

server3 `/tmp`: 84088012800 available bytes; 95.31% used; 114166425 free inodes.

server3 `/var/tmp`: 84088012800 available bytes; 95.31% used; 114166425 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106095177728 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106095177728 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 106992160768 available bytes; 98.52% used; 224929221 free inodes.

server4 `/tmp`: 106095177728 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106095177728 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
