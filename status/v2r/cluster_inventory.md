# V2R cluster inventory

2026-09-25T09:10:30.905744+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318836203520 available bytes; 82.21% used; 112480389 free inodes.

server1 `/home`: 318836203520 available bytes; 82.21% used; 112480389 free inodes.

server1 `/tmp`: 318836203520 available bytes; 82.21% used; 112480389 free inodes.

server1 `/var/tmp`: 318836203520 available bytes; 82.21% used; 112480389 free inodes.

server1 `/mnt/raid5`: 350409203712 available bytes; 98.39% used; 337556959 free inodes.
| server2 | True | ['5', '6'] | [] |

server2 `/`: 22839840768 available bytes; 98.73% used; 110410494 free inodes.

server2 `/home`: 22839840768 available bytes; 98.73% used; 110410494 free inodes.

server2 `/tmp`: 22839840768 available bytes; 98.73% used; 110410494 free inodes.

server2 `/var/tmp`: 22839840768 available bytes; 98.73% used; 110410494 free inodes.

server2 `/mnt/raid5`: 332248997888 available bytes; 97.70% used; 445092781 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84435587072 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84435587072 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142371983360 available bytes; 98.03% used; 225810992 free inodes.

server3 `/tmp`: 84435587072 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84435587072 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632739328 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105632739328 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 241765511168 available bytes; 96.66% used; 224998187 free inodes.

server4 `/tmp`: 105632739328 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105632739328 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
