# V2R cluster inventory

2026-09-24T11:46:29.530157+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324343259136 available bytes; 81.91% used; 112488818 free inodes.

server1 `/home`: 324343259136 available bytes; 81.91% used; 112488818 free inodes.

server1 `/tmp`: 324343259136 available bytes; 81.91% used; 112488818 free inodes.

server1 `/var/tmp`: 324343259136 available bytes; 81.91% used; 112488818 free inodes.

server1 `/mnt/raid5`: 426293968896 available bytes; 98.04% used; 337687411 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57644535808 available bytes; 96.78% used; 110429836 free inodes.

server2 `/home`: 57644535808 available bytes; 96.78% used; 110429836 free inodes.

server2 `/tmp`: 57644535808 available bytes; 96.78% used; 110429836 free inodes.

server2 `/var/tmp`: 57644535808 available bytes; 96.78% used; 110429836 free inodes.

server2 `/mnt/raid5`: 510132895744 available bytes; 96.48% used; 445172853 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85245784064 available bytes; 95.24% used; 114166894 free inodes.

server3 `/home`: 85245784064 available bytes; 95.24% used; 114166894 free inodes.

server3 `/data`: 163674963968 available bytes; 97.74% used; 225815945 free inodes.

server3 `/tmp`: 85245784064 available bytes; 95.24% used; 114166894 free inodes.

server3 `/var/tmp`: 85245784064 available bytes; 95.24% used; 114166894 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105727668224 available bytes; 94.10% used; 114348834 free inodes.

server4 `/home`: 105727668224 available bytes; 94.10% used; 114348834 free inodes.

server4 `/data`: 115387998208 available bytes; 98.41% used; 225257964 free inodes.

server4 `/tmp`: 105727668224 available bytes; 94.10% used; 114348834 free inodes.

server4 `/var/tmp`: 105727668224 available bytes; 94.10% used; 114348834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
