# V2R cluster inventory

2026-09-25T11:56:05.317826+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319045984256 available bytes; 82.20% used; 112478827 free inodes.

server1 `/home`: 319045984256 available bytes; 82.20% used; 112478827 free inodes.

server1 `/tmp`: 319045984256 available bytes; 82.20% used; 112478827 free inodes.

server1 `/var/tmp`: 319045984256 available bytes; 82.20% used; 112478827 free inodes.

server1 `/mnt/raid5`: 364333486080 available bytes; 98.33% used; 337549113 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22898380800 available bytes; 98.72% used; 110409972 free inodes.

server2 `/home`: 22898380800 available bytes; 98.72% used; 110409972 free inodes.

server2 `/tmp`: 22898380800 available bytes; 98.72% used; 110409972 free inodes.

server2 `/var/tmp`: 22898380800 available bytes; 98.72% used; 110409972 free inodes.

server2 `/mnt/raid5`: 326419980288 available bytes; 97.74% used; 445081858 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84213084160 available bytes; 95.30% used; 114154982 free inodes.

server3 `/home`: 84213084160 available bytes; 95.30% used; 114154982 free inodes.

server3 `/data`: 142123311104 available bytes; 98.04% used; 225812700 free inodes.

server3 `/tmp`: 84213084160 available bytes; 95.30% used; 114154982 free inodes.

server3 `/var/tmp`: 84213084160 available bytes; 95.30% used; 114154982 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105593909248 available bytes; 94.11% used; 114350231 free inodes.

server4 `/home`: 105593909248 available bytes; 94.11% used; 114350231 free inodes.

server4 `/data`: 232572891136 available bytes; 96.79% used; 224973788 free inodes.

server4 `/tmp`: 105593909248 available bytes; 94.11% used; 114350231 free inodes.

server4 `/var/tmp`: 105593909248 available bytes; 94.11% used; 114350231 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
