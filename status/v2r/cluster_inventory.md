# V2R cluster inventory

2026-09-25T03:56:36.401614+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318929358848 available bytes; 82.21% used; 112480366 free inodes.

server1 `/home`: 318929358848 available bytes; 82.21% used; 112480366 free inodes.

server1 `/tmp`: 318929358848 available bytes; 82.21% used; 112480366 free inodes.

server1 `/var/tmp`: 318929358848 available bytes; 82.21% used; 112480366 free inodes.

server1 `/mnt/raid5`: 395066331136 available bytes; 98.19% used; 337595733 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22971838464 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 22971838464 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 22971838464 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 22971838464 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 464077467648 available bytes; 96.79% used; 445110802 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84343128064 available bytes; 95.29% used; 114156072 free inodes.

server3 `/home`: 84343128064 available bytes; 95.29% used; 114156072 free inodes.

server3 `/data`: 144163045376 available bytes; 98.01% used; 225816855 free inodes.

server3 `/tmp`: 84343128064 available bytes; 95.29% used; 114156072 free inodes.

server3 `/var/tmp`: 84343128064 available bytes; 95.29% used; 114156072 free inodes.
| server4 | True | ['0', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105682980864 available bytes; 94.10% used; 114350884 free inodes.

server4 `/home`: 105682980864 available bytes; 94.10% used; 114350884 free inodes.

server4 `/data`: 36950528000 available bytes; 99.49% used; 224964839 free inodes.

server4 `/tmp`: 105682980864 available bytes; 94.10% used; 114350884 free inodes.

server4 `/var/tmp`: 105682980864 available bytes; 94.10% used; 114350884 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
